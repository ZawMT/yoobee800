# Creating dictionary - Key is ID, and Value is Name
student_names = {'1': 'John', '2': 'Mary',
                 '3': 'Dylan', '4': 'Bob', '5': 'Alice'}

# Creating dictionary - Key is ID, and Value is Score
student_scores = {'1': 90, '2': 35, '3': 95, '4': 45, '5': 80}

print(student_names)
print(student_scores)

# A simple merge and print
student_succ = {** student_names, **student_scores}
print(student_succ)

# Merge the names and scores
student_succ = {student_names[k]: student_scores[k]
                for k, v in student_scores.items() if v >= 50}

print(student_succ)
