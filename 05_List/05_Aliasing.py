P = [10, 20, 30, 40, 50] 
print("List of P: ", P)

Q = P 

print("After aliasing, Value of Q: ", Q) 


print("------------------------------------------------")

Q[2] = 'Python'

print("P: ", P)
print("Q: ", Q) 