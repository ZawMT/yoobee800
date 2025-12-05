import os

class FileTest:
    def __init__(self):
        self.no_of_searching_char = 0
        

    def open_n_print_simple(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8-sig') as data:
                lines = data.readlines()
                for line in lines:
                    print(line)
                    self.count_char(line, '*')
        except Exception as x:
            print(f'Error in convert_line_endings: {x}')
        
    
    def count_char(self, line, char_to_count):
        self.no_of_searching_char = self.no_of_searching_char + line.count(char_to_count)
            
def main():
    current_working_directory = os.getcwd()
    file_test = FileTest()
    file_test.open_n_print_simple(current_working_directory + "/demo_file.txt")
    print(f"No. of * in this text: {file_test.no_of_searching_char}")
    

if __name__ == "__main__":
    main()