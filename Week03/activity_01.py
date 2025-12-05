import os

class FileTest:
    def __init__(self):
        self.no_of_searching_char = 0
    

    def open_n_print(self, filename):
        try:
            self.convert_line_endings(filename) #Need to do this because file contents need to be adjusted to read in Mac
            with open(filename, 'r', encoding='utf-8-sig') as data:  #'utf-8-sig' handles BOM
                for line in data:
                    self.count_char(line, '*')
                    print(line.rstrip('\r\n'))  #Strip all line endings
        except Exception as x:
            print(f'Error in open_n_print: {x}')


    def convert_line_endings(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8-sig') as data:
                lines = data.readlines()
            with open(filename, 'w', encoding='utf-8') as data:
                data.writelines([line.rstrip('\r\n') + '\n' for line in lines])
            print("Line endings converted to Unix style.")
        except Exception as x:
            print(f'Error in convert_line_endings: {x}')

    
    def count_char(self, line, char_to_count):
        self.no_of_searching_char = self.no_of_searching_char + line.count(char_to_count)
            
def main():
    current_working_directory = os.getcwd()
    file_test = FileTest()
    file_test.open_n_print(current_working_directory + "/demo_file.txt")
    print(f"No. of * in this text: {file_test.no_of_searching_char}")


if __name__ == "__main__":
    main()