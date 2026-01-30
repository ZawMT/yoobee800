'''
Author: Zaw Min Tun
Date: 2026-01-25
Description:
    This application is created for homework assignment below:
        Develop a project that meets all of the following requirements 
        (OOP development is mandatory and you can eliminate the user access level):
            Include a requirements.txt file listing all project dependencies
            Provide a clear and well-structured README.md file
            Design and implement the backend architecture and database schema
            Implement robust error handling and logging for monitoring and debugging
'''

import logging
import os

from logger_config import setup_app_logging
from currency import CurrencyService
from database_handler import DatabaseHandler

setup_app_logging()
logger = logging.getLogger(__name__)


# Preparing the tables and the exchange rates data
def prepare_required_tables_and_data(db_handler):
    db_handler.run_db_script('''
        PRAGMA foreign_keys = ON; -- To ensure the foreign key relationship
        ''')

    db_handler.run_db_script('''
        CREATE TABLE IF NOT EXISTS currency_names (
            currency_id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency_code TEXT NOT NULL CHECK(length(currency_code) = 3),
            currency_name TEXT NOT NULL,
            last_updated DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(currency_code)
        );
        ''')
    col_names = ['currency_code', 'currency_name']
    db_handler.run_db_insert('currency_names', col_names, [
                             'NZD', 'New Zealand Dollar'])
    db_handler.run_db_insert('currency_names', col_names, [
                             'MMK', 'Myanmar Kyat'])
    db_handler.run_db_insert('currency_names', col_names, [
                             'USD', 'United States Dollar'])

    db_handler.run_db_script('''
        CREATE TABLE IF NOT EXISTS exchange_rates (
            rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
            base_currency_code TEXT NOT NULL,
            target_currency_code TEXT NOT NULL,
            exchange_rate REAL NOT NULL,
            exchange_rate_source TEXT NOT NULL,
            last_updated DATETIME DEFAULT CURRENT_TIMESTAMP,
            
            -- Foreign Key constraints
            FOREIGN KEY (base_currency_code) REFERENCES currency_names(currency_code) 
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (target_currency_code) REFERENCES currency_names(currency_code) 
                ON UPDATE CASCADE ON DELETE CASCADE,
            
            -- To ensure NOT to have duplicate pairs
            UNIQUE(base_currency_code, target_currency_code)
        );
        ''')
    col_names = ['base_currency_code', 'target_currency_code',
                 'exchange_rate', 'exchange_rate_source']
    db_handler.run_db_insert('exchange_rates', col_names, [
                             'NZD', 'MMK', 2000, 'GlobalMarket'])
    db_handler.run_db_insert('exchange_rates', col_names, [
                             'NZD', 'USD', 0.61, 'GlobalMarket'])
    db_handler.run_db_insert('exchange_rates', col_names, [
                             'MMK', 'NZD', 0.00052, 'GlobalMarket'])
    db_handler.run_db_insert('exchange_rates', col_names, [
                             'MMK', 'USD', 0.000248, 'GlobalMarket'])
    db_handler.run_db_insert('exchange_rates', col_names, [
                             'USD', 'NZD', 1.65, 'GlobalMarket'])
    db_handler.run_db_insert('exchange_rates', col_names, [
                             'USD', 'MMK', 4025, 'GlobalMarket'])


def show_info(currencies, rates):
    # Display all supported currencies
    idx = 1
    print("--- Supported Currencies ---")
    for c in currencies:
        print(f"{idx}. {c.code} ({c.name})")
        idx += 1

    # Display all rates
    idx = 1
    print("\n--- Exchange Rates ---")
    for obj in rates.values():
        print(f"{idx}. {obj.base} to {obj.target}: {obj.rate} ({obj.source})")
        idx += 1


def start_application(service, currencies, rates):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        show_info(currencies, rates)

        print("\n" + "-"*40)
        print("Enter conversion details (or type 'q' to quit)")

        base = input("Base Currency Code (e.g., NZD): ").upper().strip()
        if base == 'Q':
            break

        if service.is_supported_currency(base) is False:
            print(f"Currency {base} is not supported.")
            input("\nPress Enter to continue...")
            continue
        target = input("Target Currency Code (e.g., MMK): ").upper().strip()
        if target == 'Q':
            break

        if service.is_supported_currency(target) is False:
            print(f"Currency {target} is not supported.")
            input("\nPress Enter to continue...")
            continue

        try:
            amount_str = input("Amount to convert: ")
            if amount_str.lower() == 'q':
                break
            amount = float(amount_str)

            # Perform calculation using the service
            result = service.convert(base, target, amount)

            print(
                f"\n>> RESULT: {amount:,.2f} {base} = {result:,.2f} {target}")
            input("\nPress Enter to continue...")

        except ValueError as ve:
            print(f"INPUT ERROR: {ve}")
            logger.warning(f"User input error: {ve}")
        except Exception as e:
            logger.error(f"ERROR: Could not complete conversion. {e}")
            print(f"ERROR: Could not complete conversion. {e}")

    logger.info("Application terminated.")
    print("\nThank you for using YB Currency Converter. Goodbye!")


def main():  # Entry point of the application
    try:
        logger.info("Application YB Currency Converter started.")

        # Initialize the DB handler
        db_handler = DatabaseHandler("YB_ExchangeRate_DB")
        prepare_required_tables_and_data(db_handler)

        # Initialize the CurrencyService
        service = CurrencyService(db_handler)

        # Sycn the exchange rates first of all
        service.sync_exchange_rates()

        # Get all currencies
        currencies = service.get_all_currencies()

        # Get all rates
        rates = service.get_all_rates()

        start_application(service, currencies, rates)
    except Exception as e:
        # Any error while doing the process
        logger.error(f"CRITICAL ERROR: {e}")
        print(f"CRITICAL ERROR: {e}")


if __name__ == "__main__":
    main()
