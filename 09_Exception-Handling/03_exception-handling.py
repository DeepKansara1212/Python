num = int(input("Enter a number: "))

try:
    result = 10 / num
    print(result)
except Exception as err:
    print("Error: ", err)

else:
    print("Else block code")  

finally:
    print("This block is executes everytime.") 

