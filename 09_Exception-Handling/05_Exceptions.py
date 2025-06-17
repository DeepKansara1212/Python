num = int(input("Enter a number: "))


try:
    result = 10 / num 
    print(result)  
except Exception as err:
    print("Error: ", err) 
except ValueError:
    print("Value Error")
else:
    print("This will run when there is no Exception.")
finally:
    print("This will be always executed")


print("Hello World") 
