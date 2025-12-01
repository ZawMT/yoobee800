'''
Temperature converter
Author: Zaw Min Tun
Description:
    This program will convert Fahrenheit input to Celsius and vice versa
'''

import re #To use regular expression to evaluate and hanlde user input data

#Class to get input, convert to Fahrenheit / Celsius and display the result
class TemperatureConverter:
    def __init__(self):
        print("Give the temperature in Celsius (e.g. C100) or in Fahrenheit (e.g. F100). \nThe input will be converted to the other equivalent temperature.")
        self.celsius = None
        self.fahrenheit = None
        self.user_input = "" #To keep the user input as exactly as given by the user

    
    def get_input(self):
        expected_pattern = r'^[fFcC](\d+\.?\d*)$' #Input should start with f/F/c/C and followed by an integer or a float (e.g. 100 or 100.11)
        while self.celsius == None and self.fahrenheit == None:
            self.user_input = input("Temperature: ")
            re_match = re.fullmatch(expected_pattern, self.user_input)
            if re_match: #Input is correctly typed in such as c100, C100.1, f123, f123.11
                if self.user_input[0] in ['f', 'F']: #Input is Fahrenheit
                    self.fahrenheit = float(re_match.group(1))
                else: #Input is Celsius
                    self.celsius = float(re_match.group(1))
            else:
                print("Invalid input. Please enter the temperature with the correct \'C\' or \'F\' prefix.")


    def convert_n_display_output(self):
        if self.fahrenheit: #Fahrenheit is given by user
            self.celsius = (self.fahrenheit - 32) / 1.8
            print(f'{self.user_input} degrees Fahrenheit is converted to {self.celsius:.2f} degrees Celsius.')
        else: #Celsius is given by user
            self.fahrenheit = (self.celsius * 1.8) + 32
            print(f'{self.user_input} degrees Celsius is converted to {self.fahrenheit:.2f} degrees Fahrenheit.')


def main():
    temperature_converter = TemperatureConverter() #Initialize the class
    temperature_converter.get_input() #Getting user input
    temperature_converter.convert_n_display_output() #Dispay the output


if __name__ == "__main__":
    main()