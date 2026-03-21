def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}\n")
        return result
    return wrapper


@log_decorator
def add(a, b):
    return a + b


@log_decorator
def multiply(a, b):
    return a * b


add(3, 5)
multiply(2, 6)
