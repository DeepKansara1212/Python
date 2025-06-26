# 5 5 5 5 5 
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5



n = int(input("Enter no of rows: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(n, end=" ") 
    print("\n") 