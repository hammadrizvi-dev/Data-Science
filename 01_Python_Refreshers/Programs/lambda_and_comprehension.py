# Lambda and list comprehension example
# These are short ways to write simple operations.

add = lambda a, b: a + b
print("Lambda result:", add(3, 5))

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

squares_comp = [x * x for x in range(1, 6)]
print("List comprehension:", squares_comp)

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", even_numbers)
