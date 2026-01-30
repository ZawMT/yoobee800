data = []

for i in range(5):
    data.append(lambda a,  i=i*2: i*a)

print("data\n")
print(data)
print("\n\nTrying some of data\n")
print(data[0](10))
print(data[1](10))
print(data[4](10))
