set1 = {10, 20, 30, 40, 50}
set2 = {40, 50, 60, 70}

# print(dir(set))

# set.add(45)
# set.pop()
# set.remove(45)


# UNION
# union = set1.union(set2)
union = set1 | set2
print("Union: ", union)


# INTERSECTION
# intersection = set1.intersection(set2)
intersection = set1 & set2
print("Intersection: ", intersection)


# DIFFERNECE
# difference = set1.difference(set2)
difference = set1 - set2
print("Difference: ", difference)


print(set1.issubset(set2)) 