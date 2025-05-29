a = 5
b = 5
c = 10

# a = a + 10
a += 10          # 15
a -= 10         # 5
a *= 2         # 10    

# print(a) 


print(a is not b)
print(a is b)


# Operators Precedence & Associativity
# Precedence: Determines the order of operations
# Associativity: Determines the order of operations with the same precedence order

# ()        -> left to right
# / * %     -> left to right
# + -       -> left to right

Eq = 10 + (20 * 30) / 50 + 45 % 2 
# Eq = 10 + 600 / 50 + 45 % 2
# Eq = 10 + 12 + 45 % 2
# Eq = 10 + 12 + 1
# Eq = 23
print(Eq)