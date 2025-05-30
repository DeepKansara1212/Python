# EXPLICIT TYPE CONVERSION
# int(), str(), bool(), float()
# FALSY VALUES: 0, 0.0, "", [], (), False
# TRUTHY VALUES: All other values

a = 12

# print(type(a)) 

# a = str(a)
# a = bool(a)
a = float(a)
# print(a)
# print(type(a))


b = "asd"
# print(type(b))
# b = int(b)
# print(b)


c = [10, 20]
c = bool(c)
# print(c)



# IMPLICIT TYPE CONVERSION
# Python automatically converts types when necessary

print(type(12 / 4))