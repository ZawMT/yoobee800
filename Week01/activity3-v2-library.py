'''
Fibonacci series and factorial generator 
Author: Zaw Min Tun
Description:
    This program will ask for a number which will be taken as N
    Then it will generate a Fibonacci sequence of length N and factorial of N 
    This program is using SymPy library which can be installed by running this command or something according => pip install sympy 
'''

from sympy import factorial
from sympy import fibonacci

def main():
    print("This application will give a Fibonacci sequence of length N and factorial of N.")
    num = int(input("Give a positive integer number (N):"))
    print("Fibonacci sequence:", end=" ")
    fibonacci_seq = [fibonacci(i) for i in range(num)] or ["-"] #Just calling right away the fibonacci function provided by sympy
    print(*fibonacci_seq, sep=", ")

    print(f"Factorial: {factorial(num)}") #Just calling right away the factorial function provided by sympy

if __name__ == "__main__":
    main()