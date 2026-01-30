import logging
import os
import sqlite3

logger = logging.getLogger(__name__)


class DatabaseHandler:
    def __init__(self, DbName):
        logger.info("Initializing DatabaseHandler")
        # Getting the location of this Python file
        cur_dir = os.path.dirname(os.path.abspath(__file__))

        # Create a folder called 'data' side by side with this Python file (if there is no such folder yet)
        os.makedirs(f'{cur_dir}/data', exist_ok=True)

        # DbName will be used as data filename
        self.db_file = f'{cur_dir}/data/{DbName}.db'

        # For demonstration purpose, data will be cleared out with every execution
        if os.path.exists(self.db_file):
            os.remove(self.db_file)
        logger.info("Successfully initialized DatabaseHandler")

    # A general function to run the DDL and DML scripts
    def run_db_script(self, db_script, params=None):
        cursor = self.__open_db_connection()
        if params:
            cursor.execute(db_script, params)
        else:
            cursor.execute(db_script)
        self.__close_db_connection()

    # A general function to do the data insert - not to copy and paste the whole INSERT statement repeatedly
    def run_db_insert(self, table, list_of_columns, list_of_values):
        cursor = self.__open_db_connection()
        db_script_1 = f'INSERT INTO {table} ('
        db_script_2 = 'VALUES ('
        for col in list_of_columns:
            db_script_1 = f'{db_script_1}{col},'
            db_script_2 = f'{db_script_2}?,'

        db_script = f'{db_script_1[:-1]}) {db_script_2[:-1]});'
        params = []
        params.append(list_of_values)
        cursor.executemany(db_script, params)
        self.__close_db_connection()

    # A function to run a query and return all the results
    def fetch_all(self, query):
        cursor = self.__open_db_connection()
        cursor.execute(query)
        rows = cursor.fetchall()
        self.__close_db_connection()
        return rows

    # A function to run a query with given parameters and return one record
    def fetch_one(self, query, params):
        cursor = self.__open_db_connection()
        cursor.execute(query, params)
        row = cursor.fetchone()
        self.__close_db_connection()
        return row

    def run_db_upsert(self, table, column_names, values):
        placeholders = ', '.join(['?' for _ in values])
        columns = ', '.join(column_names)
        sql = f"INSERT OR REPLACE INTO {table} ({columns}) VALUES ({placeholders})"
        self.run_db_script(sql, values)

    # A private function to open DB connection
    def __open_db_connection(self):
        # Opening the database connection + Creating the database if not created yet
        self.db_connection = sqlite3.connect(self.db_file)
        # Getting the cursor to return if the caller needs to use it
        cursor = self.db_connection.cursor()
        return cursor

    # A private function to close DB connection
    # need_to_commit is to tell if all the DB activities prior to this call should be committed or not - Default is True
    def __close_db_connection(self, need_to_commit=True):
        if need_to_commit:
            self.db_connection.commit()  # Committing all the actions done so far
        else:
            self.db_connection.rollback()  # Doing rollback all the actions done so far

        self.db_connection.close()  # Closing the database connection
