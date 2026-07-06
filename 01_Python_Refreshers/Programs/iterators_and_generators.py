# Iterators and generators example
# Generators create values one by one and save memory.

numbers = [1, 2, 3]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))


def square_numbers(limit):
    for i in range(limit):
        yield i * i


for value in square_numbers(5):
    print(value)
