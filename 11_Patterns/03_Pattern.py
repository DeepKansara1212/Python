# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


# i = 0 1 2 3 4 

n = int(input("Enter no. of rows: "))


# Outer For loop -> To print the no of rows
for i in range(n):
    # Inner For Loop -> To print the elements in a single row
    for j in range(i+1):
        print(i+1, end=" ")
    print("\n") 
    