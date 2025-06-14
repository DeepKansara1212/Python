data = {'A': [1, 2, 3], 'B': [2, 3, 4], 'C': [4, 5]}

unique_values = set()

for i in data.values():
    unique_values.update(i)

print(unique_values) 