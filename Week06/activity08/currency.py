import csv
import logging
import os

logger = logging.getLogger(__name__)


class Currency:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __repr__(self):
        return f"Currency(code='{self.code}', name='{self.name}')"


class ExchangeRate:
    def __init__(self, base_currency, target_currency, rate, source):
        self.base = base_currency
        self.target = target_currency
        self.rate = rate
        self.source = source

    def __repr__(self):
        return f"ExchangeRate(base='{self.base}', target='{self.target}', rate={self.rate}, source='{self.source}')"


class CurrencyService:
    def __init__(self, db_handler):
        # Passing the DB tool into the logic tool
        self.db = db_handler

        # To load later all the rates
        self.rates_cache = {}

        self.supported_codes = []

    def is_supported_currency(self, code):
        return code in self.supported_codes

    # Fetches the current list of valid codes from the DB.
    def get_all_supported_currency_codes(self):
        query = "SELECT currency_code FROM currency_names"
        results = self.db.fetch_all(query)
        return [row[0] for row in results]

    def get_all_currencies(self):
        data = self.db.fetch_all(
            "SELECT currency_code, currency_name FROM currency_names")
        return [Currency(row[0], row[1]) for row in data]

    def get_all_rates(self):
        query = "SELECT base_currency_code, target_currency_code, exchange_rate, exchange_rate_source FROM exchange_rates"
        results = self.db.fetch_all(query)
        for row in results:
            rate_obj = ExchangeRate(row[0], row[1], row[2], row[3])

            # Create a unique key for the pair and save it for later calculation
            cache_key = f"{rate_obj.base}-{rate_obj.target}"
            self.rates_cache[cache_key] = rate_obj
        return self.rates_cache

    def sync_exchange_rates(self, file_path="rates.csv"):
        # Get the current list of supported codes from the DB
        self.supported_codes = self.get_all_supported_currency_codes()

        # Overwrite the fixed presets
        if os.path.exists(file_path):
            self._import_from_csv(file_path)

    def _import_from_csv(self, file_path):
        with open(file_path, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                base = row['BaseCurrency']
                target = row['TargetCurrency']
                rate = row['Rate']
                source = row['Source']

                # Skip if data is not fully provided
                if base is None or target is None or rate is None or source is None:
                    # Inform the reason for skipping
                    print(
                        f"Skipping: {base} to {target}: Information is not fully provided.")
                    continue

                # Update, if existing, or insert the rate into database
                if base in self.supported_codes and target in self.supported_codes:
                    self.db.run_db_upsert(
                        'exchange_rates',
                        ['base_currency_code', 'target_currency_code',
                            'exchange_rate', 'exchange_rate_source'],
                        [base, target, rate, source]
                    )
                else:
                    # Inform the reason for skipping
                    if base not in self.supported_codes:
                        print(
                            f"Skipping: {base} to {target}: {base} currency not supported.")
                    if target not in self.supported_codes:
                        print(
                            f"Skipping: {base} to {target}: {target} currency not supported.")

    def convert(self, base_code, target_code, amount):
        # Create the key exactly so the info can be found back in the prepared / loaded rates
        cache_key = f"{base_code}-{target_code}"

        # Find back the rates
        rate_obj = self.rates_cache.get(cache_key)

        # If not found, error
        if not rate_obj:
            logger.error(f"Conversion failed: {cache_key} not in cache.")
            raise ValueError(
                f"No rate info found for {base_code} to {target_code}")

        # Calculate as per rate info
        return amount * float(rate_obj.rate)
