'''
Database activities 
Author: Zaw Min Tun
Description:
    This program is to demonstrate the basic ideas of using database to cater the following activity:

    Design an ER diagram based on the provided scenario for a clinic and develop an OOP project that meets the following requirements:
    1. List the full information of all patients who are classified as seniors in the clinic (age > 65 years).
    2. Display the total number of doctors who specialise in ophthalmology.
'''
import sqlite3

class DatabaseHandler:
    def __init__(self, DbName):
        import os
        #Getting the location of this Python file
        cur_dir = os.path.dirname(os.path.abspath(__file__))

        #Create a folder called 'data' side by side with this Python file (if there is no such folder yet)
        os.makedirs(f'{cur_dir}/data', exist_ok=True)

        #DbName will be used as data filename
        self.db_file = f'{cur_dir}/data/{DbName}.db'
        
        #For demonstration purpose, data will be cleared out with every execution
        if os.path.exists(self.db_file):
            os.remove(self.db_file)

    #A general function to run the DDL and DML scripts
    def run_db_script(self, db_script):
        cursor = self.__open_db_connection()
        cursor.execute(db_script)
        self.__close_db_connection()

    #A general function to do the data insert - not to copy and paste the whole INSERT statement repeatedly
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

    #A function to run a query and print out the results
    #result_are_records is to tell that the result are records (i.e. not a single-piece value)
    #result_label is just a label to come before the result
    def run_query_n_print_result(self, query, result_label = '', result_are_records = True):
        cursor = self.__open_db_connection()
        cursor.execute(query)
        if result_are_records: #If the result is a set of records, then print them all
            rows = cursor.fetchall()
            print(f"{result_label}")
            for row in rows:
                print(row)
        else: #If the result is NOT a set of records, then extract the single-piece info (if any) and print it out
            result = cursor.fetchone()
            if result:
                print(f"{result_label}{result[0]}")
            else:
                print(f"{result_label} -")

    #A private function to open DB connection
    def __open_db_connection(self):
        self.db_connection = sqlite3.connect(self.db_file) #Opening the database connection + Creating the database if not created yet
        cursor = self.db_connection.cursor() #Getting the cursor to return if the caller needs to use it
        return cursor
    
    #A private function to close DB connection
    #need_to_commit is to tell if all the DB activities prior to this call should be committed or not - Default is True
    def __close_db_connection(self, need_to_commit = True):
        if need_to_commit:
            self.db_connection.commit() #Committing all the actions done so far
        else:
            self.db_connection.rollback() #Doing rollback all the actions done so far

        self.db_connection.close() #Closing the database connection


def create_and_populate_doctor_table(db_handler):
    db_handler.run_db_script('''
        CREATE TABLE IF NOT EXISTS Doctor(
            Doctor_ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Email TEXT,
            Speciality TEXT)
        ''')
    col_names = ['Name', 'Email', 'Speciality']
    db_handler.run_db_insert('Doctor', col_names, ['James Rigby', 'rigby.james@yb.clinic.com', 'Family Medicine'])
    db_handler.run_db_insert('Doctor', col_names, ['Lucy Owens', 'owens.lucy@yb.clinic.com', 'Family Medicine'])
    db_handler.run_db_insert('Doctor', col_names, ['John Keith', 'keith.john@yb.clinic.com', 'Family Medicine'])
    db_handler.run_db_insert('Doctor', col_names, ['Daisy Mann', 'mann.daisy@yb.clinic.com', 'Pediatrics'])
    db_handler.run_db_insert('Doctor', col_names, ['Carlos Canes', 'canes.carlos@yb.clinic.com', 'Ophthalmology'])
    db_handler.run_db_insert('Doctor', col_names, ['Elvis Dean', 'dean.elvis@yb.clinic.com', 'Ophthalmologist'])
            
def create_and_populate_patient_table(db_handler):
    db_handler.run_db_script('''
        CREATE TABLE IF NOT EXISTS Patient(
            Patient_ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Email TEXT,
            Phone TEXT,
            Age INTEGER NOT NULL)
        ''')
    col_names = ['Name', 'Email', 'Phone', 'Age']
    db_handler.run_db_insert('Patient', col_names, ['Susan Rays', '-', '022 6789 888', 31])
    db_handler.run_db_insert('Patient', col_names, ['Richard Mills', 'mills.richard@outlook.com', '023 6729 338', 19])
    db_handler.run_db_insert('Patient', col_names, ['Sylvia Drew', 'sylvia_0101@gmail.com', '021 7789 988', 41])
    db_handler.run_db_insert('Patient', col_names, ['Owen Richards', '-', '023 8889 788', 71])
    db_handler.run_db_insert('Patient', col_names, ['Eleanor Stone', '-', '021 9781 388', 79])
    db_handler.run_db_insert('Patient', col_names, ['Drew Gui', 'gui.drew@yahoo.com', '029 9789 188', 21])
    db_handler.run_db_insert('Patient', col_names, ['Taka Hiro', 'hiro123@outlook.com', '022 7788 999', 44])
    db_handler.run_db_insert('Patient', col_names, ['Leon Hays', 'hays1979@gmail.com', '021 5589 778', 46])
    db_handler.run_db_insert('Patient', col_names, ['Selena Sims', 'sims.79@outlook.com', '023 5719 118', 45])
    db_handler.run_db_insert('Patient', col_names, ['Doris Lessing', '-', '022 6289 337', 81])

def main():
    try:
        #Initializing a handler which will help doing DB actions
        db_handler = DatabaseHandler("YB_Clinic_DB")

        #Preparing sample data to demonstrate
        create_and_populate_doctor_table(db_handler)
        create_and_populate_patient_table(db_handler)

        #Printing all the tables first, so the outcome can be verified
        db_handler.run_query_n_print_result("SELECT * FROM Doctor", "Doctors")
        db_handler.run_query_n_print_result("SELECT * FROM Patient", "\n\n========== ========== ==========\nPatients\n========== ========== ==========")
        
        print("\nDemonstrating info\n========== ========== ==========")
        #Listing all the senior patients (who are older than 65)
        db_handler.run_query_n_print_result(
            '''SELECT * FROM Patient WHERE Age > 65''', "Senior Patients\n========== ========== ==========")
        
        #Displaying the total number of doctors who are specialized in Ophthalmology
        db_handler.run_query_n_print_result(
            '''SELECT Count(Doctor_ID) FROM Doctor WHERE Speciality like \'%Ophthalm%\'''', "\n\n========== ========== ==========\nNo. of Doctors specialized in Ophthalmology: ", False)

        
    except Exception as x:
        print(f"Error while processing: {x}")

if __name__ == "__main__":
    main()