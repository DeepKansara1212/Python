data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

dict = {}

for i in data:
    # print(i)
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)


# dict = {
#     'apple': 2,
#     'banana': 3,
#     'orange': 1

# }