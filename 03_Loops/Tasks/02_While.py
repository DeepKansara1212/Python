n = int(input("Enter a number: ")) 

copy = n

rev = 0

while n > 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10 

if copy == rev:
    print(f"{copy} is a palindrome")
else:
    print(f"{copy} is not a palindrome")

'''
n = 12345

rem = 5
rev = 0 + 5 = 5
n = 1234

rem = 4
rev = 5*10 + 4 = 54
n = 123

rem = 3
rev = 54*10 + 3 = 543
n = 12

rem = 2
rev = 543 * 10 + 2 = 5432
n = 1

rem = 1
rev = 5432 * 10 + 1 = 54321
n = 0
'''