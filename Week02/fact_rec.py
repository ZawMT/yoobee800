def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  


def fibonacci(n, lst_resulted = None):
    #Preparing a blank array at first
    if lst_resulted is None:
        lst_resulted = n * [0]

    #Starting with 1 is preferable
    '''
    if n == 1:
        lst_resulted[0] = 1
        return lst_resulted
    elif n == 2:
        lst_resulted[0], lst_resulted[1] = 1, 1
        return lst_resulted     
    '''
    
    if n <= 0:
        return lst_resulted
    elif n == 1:
        lst_resulted[0] = 0
        return lst_resulted
    elif n == 2:
        lst_resulted[0], lst_resulted[1] = 0, 1
        return lst_resulted 
    else:
        if lst_resulted[n-1] == 0:
            fibonacci(n-1, lst_resulted)
            lst_resulted[n-1] = lst_resulted[n-2] + lst_resulted[n-3]
        return lst_resulted   


def get_input(for_factorial: bool):
    if for_factorial:
        return int(input("Give a positive integer:"))
    return int(input("Give a positive integer for length of Fibonacci sequence:"))


if __name__ == "__main__":
    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        ans = factorial((get_input(True)))
    elif choice == "2":
        ans = fibonacci(get_input(False))
    else:
        ans = "Invalid choice"

    print("\nFinal result:", ans)