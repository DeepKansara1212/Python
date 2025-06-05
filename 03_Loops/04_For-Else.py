n = int(input("Enter a number: "))

for i in range(1, n+1):
    if i == 25:
        print("break statement executed")
        break
    print(i) 

else:
    print("break statement was not executed")
