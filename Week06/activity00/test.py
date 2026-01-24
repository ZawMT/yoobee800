def process_order(customer_name, *items, **details):
    print(f"Customer: {customer_name}")

    # *args is a tuple of all items passed
    print("\nItems ordered:")
    for item in items:
        print(f"- {item}")

    # **kwargs is a dictionary of additional labeled info
    print("\nShipping & Discounts:")
    for key, value in details.items():
        # title is for changing "TesTING" to "Testing", "It's true" to "It'S True"
        print(f"{key.replace('_', ' ').title()}: {value}")


def greet(name, age):
    print(f"Hello {name}, you are {age}")


def my_function(**abc):
    # Here, 'abc' is a DICTIONARY containing everything passed in.
    print(abc)


# Calling the function
process_order(
    "Alex",                  # Regular argument
    "Laptop", "Mouse", "Mat",  # *args (Positional)
    shipping="Express",      # **kwargs (Keywords)
    discount_code="SAVE20",  # **kwargs
    gift_wrap=True           # **kwargs
)

data = {"name": "Alice", "age": 30}
greet(**data)  # Naming matching here - parameter name and the key name must be the same

my_function(x=1, y=2)  # Results in abc = {'x': 1, 'y': 2}


def pack_items(*abc):
    print(f"The container type is: {type(abc)}")
    print(f"The contents are: {abc}")


# We send 3 separate strings...
pack_items("Apple", "Banana", "Cherry")


def greet(first, second, third):
    print(f"Hello {first}, {second}, and {third}!")


my_list = ["Alice", "Bob", "Charlie"]

# Instead of greet(my_list[0], my_list[1], my_list[2])...
greet(*my_list)  # Length must be exactly 3

# ** is for "keyword argument unpacking"

# * works for Tuples, Lists, String, Sets, etc.

# In function definition, it's packing, and in function call, it is unpacking
