# Tuples and sets example
# Tuples are fixed collections, sets store unique values.

point = (10, 20)   # tuple
print("Point:", point)
x, y = point
print("x:", x, "y:", y)

numbers = {1, 2, 2, 3, 4}   # duplicates are removed
print("Unique numbers:", numbers)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
