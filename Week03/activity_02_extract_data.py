import os

class FileTest:
    def __init__(self):
        pass
        

    def extract_data(self, filename):
        try:
            empty_line_found = False
            no_of_lines_after_empty_line = 0
            with open(filename, 'r', encoding='utf-8-sig') as data:
                lines = data.readlines()
                for line in lines:
                    line = line.strip(' ')
                    if len(line) == 0:
                        empty_line_found = True
                    
                    if not empty_line_found: #No need to do anything until an empty line is found
                        continue
                    
                    no_of_lines_after_empty_line = no_of_lines_after_empty_line + 1

                    if no_of_lines_after_empty_line <= 2: #2 more lines need to be skipped after the empty line
                        continue

                    if len(line) > 0:
                        data = line.split(',')

        except Exception as x:
            print(f'Error in convert_line_endings: {x}')
        
        self.no_of_searching_char = self.no_of_searching_char + line.count(char_to_count)
            
def main():
    current_working_directory = os.getcwd()
    file_test = FileTest()
    file_test.extract_data(current_working_directory + "/demo_file.txt")
    

if __name__ == "__main__":
    main()