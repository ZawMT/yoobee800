import sqlite3


class DatabaseHandler:
    def __init__(self, DbName):
        import os
        # Getting the location of this Python file
        cur_dir = os.path.dirname(os.path.abspath(__file__))

        # Create a folder called 'data' side by side with this Python file (if there is no such folder yet)
        os.makedirs(f'{cur_dir}/data', exist_ok=True)

        # DbName will be used as data filename
        self.db_file = f'{cur_dir}/data/{DbName}.db'

        # For demonstration purpose, data will be cleared out with every execution
        if os.path.exists(self.db_file):
            os.remove(self.db_file)

    # A general function to run the DDL and DML scripts
    def run_db_script(self, db_script):
        cursor = self.__open_db_connection()
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

    # A function to run a query and print out the results
    # result_are_records is to tell that the result are records (i.e. not a single-piece value)
    # result_label is just a label to come before the result
    def run_query_n_print_result(self, query, result_label='', result_are_records=True):
        cursor = self.__open_db_connection()
        cursor.execute(query)
        if result_are_records:  # If the result is a set of records, then print them all
            rows = cursor.fetchall()
            print(f"{result_label}")
            for row in rows:
                print(row)
        # If the result is NOT a set of records, then extract the single-piece info (if any) and print it out
        else:
            result = cursor.fetchone()
            if result:
                print(f"{result_label}{result[0]}")
            else:
                print(f"{result_label} -")

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


def create_student_table(db_handler):
    db_handler.run_db_script('''
        CREATE TABLE IF NOT EXISTS Student(
            Student_ID INTEGER PRIMARY KEY,
            Name TEXT,
            Score INT)
        ''')


def main():
    try:
        # Creating dictionary - Key is ID, and Value is Name
        student_names = {'1': 'John', '2': 'Mary',
                         '3': 'Dylan', '4': 'Bob', '5': 'Alice'}

        # Creating dictionary - Key is ID, and Value is Score
        student_scores = {'1': 90, '2': 35, '3': 95, '4': 45, '5': 80}

        print("Names dictionary")
        print(student_names)
        print("\nScores dictionary")
        print(student_scores)

        # A simple merge and print
        student_succ = {** student_names, **student_scores}
        print(student_succ)

        # Merge the names and scores only when the score is equal or more than 50
        student_succ = {student_names[k]: student_scores[k]
                        for k, v in student_scores.items() if v >= 50}

       # The line `print("\Merged names and scores")` is attempting to print a string that says
       # "Merged names and scores". However, there seems to be a typo in the string. The backslash `\`
       # is an escape character in Python strings, so it should be escaped itself if you want to
       # include it in the output.
        print("\nMerged names and scores")
        print(student_succ)

        db_handler = DatabaseHandler("YB_Student_DB")
        create_student_table(db_handler)
        col_names = ['Student_ID', 'Name', 'Score']
        # Brining the data into the created table
        for k, v in student_scores.items():
            name = student_names[k]
            db_handler.run_db_insert('Student', col_names, [k, v, name])

        # Printing all the records
        print("\nPrinting the table")
        db_handler.run_query_n_print_result(
            "SELECT * FROM Student", "Students")

    except Exception as x:
        print(f"Error while processing: {x}")


if __name__ == "__main__":
    main()
