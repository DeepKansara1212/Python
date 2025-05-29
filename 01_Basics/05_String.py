greet = "Hello, How are you?"

print(greet[7])
print(greet[-6])


# String Slicing
# Syntax: string[start : end : step]

print(greet[0 : 5 : 1]) 
print(greet[0 : 5 : 2]) 

print(greet[7 : 14])

print(greet[7 :])

print(greet[: 15])


print(greet[::2])           # Print every second character

print(greet[::])            # Print the entire string

print(greet[::-1])          # Print the string in reverse order



char = "a"
print(ord(char))  # Get the ASCII value of the character 'a'
print(chr(97))    # Get the character corresponding to ASCII value 97


emoji = "🍔"
print(emoji)  # Print the emoji
print(ord(emoji))