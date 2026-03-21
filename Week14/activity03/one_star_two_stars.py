# **kwargs allows for an arbitrary number of keyword arguments to be passed to the function, which are then accessible as a dictionary within the function.
def func1(**kwargs):
    print(f"Received kwargs: {kwargs}")


# *args allows for an arbitrary number of positional arguments to be passed to the function, which are then accessible as a tuple within the function.
def func2(*args):
    print(f"Received kwargs: {args}")


param1 = {"a": 1, "b": 2, "c": 7}
param2 = [1, 2, 7]

print("Calling func1 - def func1(**kwargs) - with param1:")
func1(**param1)

print("\nCalling func1 - def func1(**kwargs) - with fixed value:")
func1(a=1, b=2, c=7)

print("\nCalling func2 - def func2(*args) - with param2:")
func2(*param2)

print("\nCalling func2 - def func2(*args) - with fixed value:")
func2(1, 2, 7)
