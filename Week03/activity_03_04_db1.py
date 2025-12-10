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


def create_and_populate_teacher_table(db_handler):
    db_handler.run_db_script('''
        CREATE TABLE IF NOT EXISTS Teacher(
            Teacher_ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Email TEXT,
            Degrees TEXT)
        ''')
    db_handler.run_db_script('''INSERT INTO Teacher (Name, Email, Degrees) 
            VALUES (\'John Smith\', \'john.smith@yb.com\', \'Ph.D (Computer Science)\')''')
    db_handler.run_db_script('''INSERT INTO Teacher (Name, Email, Degrees) 
            VALUES (\'Alex Green\', \'alex.green@yb.com\', \'Ph.D (Quantum Computing)\')''')
    db_handler.run_db_script('''INSERT INTO Teacher (Name, Email, Degrees) 
            VALUES (\'Cathy Dane\', \'cathy.dane@yb.com\', \'Ph.D (Computing Mathematics)\')''')


def create_and_populate_student_table(db_handler):
    db_handler.run_db_script('''
        CREATE TABLE IF NOT EXISTS Student(
            Student_ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Email TEXT)
        ''')
    db_handler.run_db_script('''INSERT INTO Student (Name, Email) 
            VALUES (\'Peter Sawyer\', \'peter.sawyer99@gmail.com\')''')
    db_handler.run_db_script('''INSERT INTO Student (Name, Email) 
        VALUES (\'Neil Erickson\', \'gamer-neil@gmail.com\')''')
    db_handler.run_db_script('''INSERT INTO Student (Name, Email) 
        VALUES (\'Selena Cannon\', \'selena2025@gmail.com\')''')
    db_handler.run_db_script('''INSERT INTO Student (Name, Email) 
        VALUES (\'Arthur Baker\', \'arthur.baker@yahoo.com\')''')
    db_handler.run_db_script('''INSERT INTO Student (Name, Email) 
        VALUES (\'Claire Boone\', \'claire.boone@outlook.com\')''')
    db_handler.run_db_script('''INSERT INTO Student (Name, Email) 
        VALUES (\'Amelia Nelson\', \'amelia@nelson.com\')''')    


def create_and_populate_course_table(db_handler):
    db_handler.run_db_script('''
        CREATE TABLE IF NOT EXISTS Course(
            Course_ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Credit INTEGER)
        ''')
    db_handler.run_db_script('''INSERT INTO Course (Name, Credit) 
            VALUES (\'MSE800\', 30)''')
    db_handler.run_db_script('''INSERT INTO Course (Name, Credit) 
            VALUES (\'MSE801\', 30)''')
    db_handler.run_db_script('''INSERT INTO Course (Name, Credit) 
            VALUES (\'MSE802\', 20)''')
    db_handler.run_db_script('''INSERT INTO Course (Name, Credit) 
            VALUES (\'MSE803\', 25)''')
    
def create_and_populate_delivery_table(db_handler):
    db_handler.run_db_script('''
        CREATE TABLE IF NOT EXISTS CourseDelivery(
            CourseDelivery_ID INTEGER PRIMARY KEY,
            Teacher_ID INTEGER NOT NULL,
            Course_ID INTEGER NOT NULL,
            FOREIGN KEY (Teacher_ID) REFERENCES Teacher(Teacher_ID),
            FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID))
        ''')
    db_handler.run_db_script('''INSERT INTO CourseDelivery (Teacher_ID, Course_ID) 
            VALUES (1, 1)''')
    db_handler.run_db_script('''INSERT INTO CourseDelivery (Teacher_ID, Course_ID) 
            VALUES (1, 2)''')
    db_handler.run_db_script('''INSERT INTO CourseDelivery (Teacher_ID, Course_ID) 
            VALUES (2, 2)''')
    db_handler.run_db_script('''INSERT INTO CourseDelivery (Teacher_ID, Course_ID) 
            VALUES (2, 3)''')
    db_handler.run_db_script('''INSERT INTO CourseDelivery (Teacher_ID, Course_ID) 
            VALUES (3, 3)''')
    db_handler.run_db_script('''INSERT INTO CourseDelivery (Teacher_ID, Course_ID) 
            VALUES (3, 4)''')

def create_and_populate_assign_table(db_handler):
    db_handler.run_db_script('''
        CREATE TABLE IF NOT EXISTS CourseAssign(
            CourseAssign_ID INTEGER PRIMARY KEY,
            Student_ID INTEGER NOT NULL,
            Course_ID INTEGER NOT NULL,
            FOREIGN KEY (Student_ID) REFERENCES Teacher(Student_ID),
            FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID))
        ''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (1, 1)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (1, 2)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (1, 3)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (1, 4)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (2, 1)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (2, 2)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (3, 1)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (3, 2)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (3, 3)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (4, 1)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (4, 2)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (4, 4)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (5, 3)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (5, 4)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (6, 2)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (6, 3)''')
    db_handler.run_db_script('''INSERT INTO CourseAssign (Student_ID, Course_ID) 
            VALUES (4, 4)''')
            

def main():
    try:
        #Initializing a handler which will help doing DB actions
        db_handler = DatabaseHandler("YB_DB")

        #Preparing sample data to demonstrate
        create_and_populate_teacher_table(db_handler)
        create_and_populate_student_table(db_handler)
        create_and_populate_course_table(db_handler)
        create_and_populate_delivery_table(db_handler)
        create_and_populate_assign_table(db_handler)

        #Printing all the tables first, so the outcome can be verified
        db_handler.run_query_n_print_result("SELECT * FROM Teacher", "Teachers")
        db_handler.run_query_n_print_result("SELECT * FROM Student", "\n========== ========== ==========\nStudents")
        db_handler.run_query_n_print_result("SELECT * FROM Course", "\n========== ========== ==========\nCourses")
        db_handler.run_query_n_print_result('''SELECT T.Name, C.Name 
            FROM CourseDelivery CD
            JOIN Teacher T ON T.Teacher_ID = CD.Teacher_ID
            JOIN Course C ON C.Course_ID = CD.Course_ID
            ''', "\n========== ========== ==========\nCourse Delivery")
        db_handler.run_query_n_print_result('''SELECT S.Name, C.Name 
            FROM CourseAssign CA
            JOIN Student S ON S.Student_ID = CA.Student_ID
            JOIN Course C ON C.Course_ID = CA.Course_ID
            ''', "\n========== ========== ==========\nCourse Assign")
        
        print("\nDemonstrating info\n========== ========== ==========")
        #Showing the number of students for MSE800 course
        db_handler.run_query_n_print_result(
            '''SELECT COUNT(*) FROM CourseAssign
            WHERE Course_ID = (SELECT Course_ID FROM Course WHERE Name = \'MSE800\')''', "No. of students for MSE800: ", False)

        #Listing all the teachers who teach MSE801
        db_handler.run_query_n_print_result(
            '''SELECT * FROM Teacher
            WHERE Teacher_ID IN (
                SELECT Teacher_ID FROM CourseDelivery 
                WHERE Course_ID = (SELECT Course_ID FROM Course WHERE Name = \'MSE801\')
            )''', "\nThe teachers for MSE801")

        
    except Exception as x:
        print(f"Error while processing: {x}")

if __name__ == "__main__":
    main()