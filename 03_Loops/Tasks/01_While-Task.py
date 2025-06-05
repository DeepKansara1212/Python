# Separate each digit of a number and print it on the new line.

n = int(input("Enter a number: ")) 

while n > 0:
    rem = n % 10
    print(rem, end='')
    n = n // 10

