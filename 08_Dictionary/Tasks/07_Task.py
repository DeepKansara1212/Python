data = {'Alice': 87, 'Bob': 91, 'Charlie': 91}

list = []

max_value = float('-inf')

for key, value in data.items():
    if data[key] > max_value:
        max_value = value
        list = [key]
    elif data[key] == max_value:
        list.append(key) 



print(list) 
print(type(list)) 






# list = [1, 2, 3, 4, 45, 10]

# max = list[0] 

# for i in range(1, len(list)):
#     if list[i] > max:
#         max = list[i] 


# max = 45
