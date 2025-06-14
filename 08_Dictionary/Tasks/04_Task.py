d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}


copy_dict = d1

# print(copy_dict)

for key, value in d2.items():
    if key in copy_dict:
        # print("Key Exists")
        copy_dict[key] += value
    else:
        copy_dict[key] = value


print(copy_dict)
