# Delcaring and initializing the variables of different types
Name = "John Doe" # Data type is string
Age = 28 # An integer
Skills = ["Python", "SQL", "Power BI"] # Data type is list which can hold different data types
Education = ("BSc Computer Science", 2020) # Data type is tuple which can hold different data types
ContactDetails = {"email": "johndoe@jd.com", "phone": "022 123 456"} # Data type is dictionary 
Certifications = {"Azure", "AWS", "Azure"} # Data type is set - Final effective value will be {"Azure", "AWS"}

# Printing the variables in a table
print("Component           |   Data Type   |   Example")
print("-----------------------------------------------")
print(f"Name                |   String      |   {Name}")
print(f"Age                 |   Integer     |   {Age}")
print(f"Skills              |   List        |   {Skills}")
print(f"Education           |   Tuple       |   {Education}")
print(f"Contact Details     |   Dictionary  |   {ContactDetails}")
print(f"Certifications      |   Set         |   {Certifications}")