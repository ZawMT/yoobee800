'''
Fibonacci series and factorial generator 
Author: Zaw Min Tun
Description:
    This program will ask for a number which will be taken as N
    Then it will generate a Fibonacci sequence of length N and factorial of N 
'''

#Function to generate Fibonacci sequence
#Reference: https://en.wikipedia.org/wiki/Fibonacci_sequence
def get_fibonacci(len):
    if len <= 0:
        return "-"
    if len == 1:
        return "0"

    fibonacci_list = [0, 1]
    i = 2
    while len > i:
        next_num = fibonacci_list[-2] + fibonacci_list[-1] #Next number is the addition of the last and the second last entries
        fibonacci_list.append(next_num)
        i = i + 1
    return ", ".join(map(str, fibonacci_list))


#Function to calculate factorial
#Reference: https://en.wikipedia.org/wiki/Factorial
def get_factorial(num):
    if num < 0:
        return "-"
    if num == 0:
        return "1"
    factorial = 1
    while num > 1:
        factorial = factorial * num #Start with the number itself
        num = num - 1 #Next number to multiply is reduced by 1
    return f"{factorial}" 


def main():
    print("This application will give a Fibonacci sequence of length N and factorial of N.")
    num = int(input("Give a positive integer number (N):"))
    print(f"Fibonacci sequence: {get_fibonacci(num)}") 
    print(f"Factorial: {get_factorial(num)}")


if __name__ == "__main__":
    main()