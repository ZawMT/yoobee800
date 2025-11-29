'''
Fibonacci series and factorial generator 
Author: Zaw Min Tun
Description:
    This program will ask for a number which will be taken as N
    Then it will generate a Fibonacci sequence of length N and factorial of N 
'''

#Function to generate Fibonacci sequence
#Reference: https://en.wikipedia.org/wiki/Fibonacci_sequence
def fibonacci_recursive(n):
    if n <= 1:
        return n
    
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    

def fibonacci_series(n):
    return [fibonacci_recursive(i) for i in range(n)]


#Function to calculate factorial
#Reference: https://en.wikipedia.org/wiki/Factorial
def get_factorial_recursive(num):
    if num > 1:
        return num * get_factorial_recursive(num - 1)    
    
    return 1


def main():
    print("This application will give a Fibonacci sequence of length N and factorial of N.")
    num = int(input("Give a positive integer number (N):"))
    print(f"Fibonacci sequence: {fibonacci_series(num)}") 
    print(f"Factorial: {get_factorial_recursive(num)}")


if __name__ == "__main__":
    main()