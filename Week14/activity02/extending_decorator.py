import time
import logging

shift_logger = logging.getLogger("shift")
shift_logger.setLevel(logging.INFO)
shift_logger.addHandler(logging.FileHandler("shift_operations.log"))

traditional_logger = logging.getLogger("traditional")
traditional_logger.setLevel(logging.INFO)
traditional_logger.addHandler(
    logging.FileHandler("traditional_operations.log"))


def applied_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}\n")
        return result
    return wrapper


@applied_decorator
def add(a, b):
    result = a + b
    traditional_logger.info("add(%s, %s) = %s", a, b, result)
    return result


@applied_decorator
def subtract(a, b):
    result = a - b
    traditional_logger.info("subtract(%s, %s) = %s", a, b, result)
    return result


@applied_decorator
def multiply(a, b):
    result = a * b
    traditional_logger.info("multiply(%s, %s) = %s", a, b, result)
    return result


@applied_decorator
def divide(a, b):
    start = time.time()
    try:
        result = a / b
    except ZeroDivisionError:
        traditional_logger.error("divide(%s, %s) => ZeroDivisionError", a, b)
        print("ERROR: cannot divide by zero")
        return None
    elapsed = time.time() - start
    print(f"  divide() execution time: {elapsed:.6f}s")
    traditional_logger.info(
        "divide(%s, %s) = %s  [%.6fs]", a, b, result, elapsed)
    return result


@applied_decorator
def left_shift(a, b):
    start = time.time()
    result = a << b
    elapsed = time.time() - start
    print(f"  left_shift() execution time: {elapsed:.6f}s")
    shift_logger.info(
        "left_shift(%s, %s) = %s  [%.6fs]", a, b, result, elapsed)
    return result


@applied_decorator
def right_shift(a, b):
    start = time.time()
    result = a >> b
    elapsed = time.time() - start
    print(f"  right_shift() execution time: {elapsed:.6f}s")
    shift_logger.info(
        "right_shift(%s, %s) = %s  [%.6fs]", a, b, result, elapsed)
    return result


add(10, 3)
subtract(10, 3)
multiply(10, 3)
divide(10, 3)
divide(10, 0)

print("Efficiency Comparison: Shifting vs Division:")
print("Left Shift (12321 << 2):")
right_shift(12321, 2)
print("Divide (12321 << 2):")
divide(12321, 2)
