data = ['a5', 'a2', 'b1', 'b3', 'c2']
sorted_data = sorted(data)
print(sorted_data)
sorted_data = sorted(data, key=lambda x: (x[0], int(x[1:])))
print(sorted_data)
data = ['a51', 'a25', 'b15', 'b32', 'c24']
sorted_data = sorted(data)
print(sorted_data)
sorted_data = sorted(data, key=lambda x: (x[0], int(x[1:])))
print(sorted_data)
