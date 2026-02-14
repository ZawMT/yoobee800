from random import randint

# example 1
for i in range(1, 20):
    if i == 20:
        print(f"You got it!")

# Describe the problem - Write your answers as comments:
# 1. what is the loop doing?
# Nothing
# 2. When is the function meant to print "You got it!"?
# When i is 20
# 3. What are your assumptions about the value of i?
# From 1 to 19

# example 2
dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 6)  # Should be 0, 5
print(dice_images[dice_num])

# example 3
year = int(input("What is your year of birth?"))

if year > 1980 and year < 1994:  # There should be equal like "year <= 1994"
    print("You are a Millennial")
elif year > 1994:
    print("You are a Gen Z")
# "else" should be handled with an informative message like "You are neither Millenial nor Gen Z"

# example 4
word_per_page = 0
pages = int(input("Number of pages: "))
# The operator is wrong. It should be "="
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page

print(f"We have {total_words} in total.")

# example 5


def add(a1, a2):
    return a1 + a2


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += randint(1, 3)
        new_item = add(new_item, item)
    b_list.append(new_item)  # This line should be in the loop
    print(b_list)


a_demo_list = [1, 2, 3, 5, 1, 21, 4, 35]
mutate(a_demo_list)
