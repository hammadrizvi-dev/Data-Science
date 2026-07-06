# Python Refresher

Python is one of the best languages for data science because it is easy to read, powerful, and has many useful libraries. This guide explains the main Python ideas with short examples.

> Each topic below has a matching Python example file in this folder.

---

## 1. Variables
Variables are containers used to store values.

```python
name = "Ali"
age = 25
print(name)
print(age)
```

What this means:
- `name` stores text
- `age` stores a number
- Variables make your code easier to read and reuse

---

## 2. Data Types
Python has different data types for different kinds of values.

```python
age = 25          # int
price = 19.99     # float
name = "John"     # str
active = True     # bool
```

Common types:
- `int` for whole numbers
- `float` for decimal numbers
- `str` for text
- `bool` for True/False

---

## 3. Operators
Operators perform actions on values.

```python
print(10 + 3)
print(10 > 3)
print(True and False)
```

Examples:
- `+` adds values
- `>` compares values
- `and` checks two conditions together

---

## 4. Operator Precedence
Python follows an order when many operators appear in one expression.

```python
print(10 + 3 * 2)      # multiplication first
print((10 + 3) * 2)    # parentheses first
```

Important rule:
- Parentheses `()` are evaluated first

---

## 5. Taking Input
You can get input from the user with `input()`.

```python
name = input("Enter your name: ")
print("Hello", name)
```

If needed, convert input values:
```python
age = int(input("Enter your age: "))
```

---

## 6. Conditional Statements
These help your program make decisions.

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Child")
```

You can also use `elif`:
```python
marks = 75

if marks >= 90:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("C")
```

### Match Case
`match` and `case` are useful when you want to compare a value with several options. This is similar to `switch` in some other languages.

```python
day = "Friday"

match day:
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("Weekend is near")
    case _:
        print("Another day")
```

> `match`/`case` is available in Python 3.10 and newer.

---

## 7. Iterating Statements
Loops repeat code multiple times.

```python
for i in range(3):
    print(i)
```

```python
count = 1
while count <= 3:
    print(count)
    count += 1
```

---

## 8. Strings
Strings are used for text.

```python
message = "Python is fun"
print(message.upper())
print(message[0])
```

Strings are useful for names, messages, and data cleaning.

---

## 9. String Methods
Python provides built-in methods to work with strings.

```python
text = " hello world "
print(text.strip())
print(text.upper())
print(text.replace("world", "Python"))
```

Common methods:
- `upper()` changes to uppercase
- `lower()` changes to lowercase
- `strip()` removes spaces
- `replace()` changes text

---

## 10. String Formatting
Formatting makes output cleaner.

```python
name = "Ali"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

`f-strings` are the easiest way to format text.

---

## 11. Lists
Lists store many values in one variable.

```python
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits)
```

Lists are useful for storing collections of data.

---

## 12. Dictionaries
Dictionaries store data as key-value pairs.

```python
student = {"name": "Sara", "age": 20}
print(student["name"])
```

This is very helpful for structured information.

---

## 13. Tuples
Tuples are similar to lists, but they cannot be changed after creation.

```python
point = (10, 20)
print(point[0])
```

Use tuples when data should stay fixed.

---

## 14. Sets
Sets store unique values.

```python
numbers = {1, 2, 2, 3, 4}
print(numbers)
```

Sets are helpful when you want to remove duplicates.

---

## 15. File Handling
Python can read and write files.

```python
with open("demo_file.txt", "w") as file:
    file.write("Hello")
```

This is useful for saving data and reading it later.

---

## 16. Functions
Functions help you reuse code.

```python
def greet(name):
    return f"Hello {name}"

print(greet("Ali"))
```

Functions make programs cleaner and easier to maintain.

---

## 17. Lambda Functions
Lambda functions are short anonymous functions.

```python
add = lambda a, b: a + b
print(add(2, 3))
```

They are useful for quick operations.

---

## 18. OOP Concepts
Object-Oriented Programming (OOP) helps you organize code using classes and objects.

- A class is a blueprint for creating objects.
- An object is an instance of a class.
- A method is a function inside a class.
- Inheritance lets one class reuse features from another class.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof")

my_dog = Dog("Buddy")
my_dog.bark()
```

This is helpful when building larger programs such as games, dashboards, or machine learning projects.

---

## 18. List Comprehension
List comprehension is a shorter way to create lists.

```python
squares = [x * x for x in range(1, 6)]
print(squares)
```

This is a compact and Pythonic style.

---

## 19. Modules and Imports
Python modules help you reuse code written by others.

```python
import math
print(math.sqrt(16))
```

This is very useful in data science because many libraries are already available.

---

## 20. Error Handling
Error handling helps your program deal with problems safely.

```python
try:
    value = int("abc")
except ValueError:
    print("This is not a valid integer")
```

This makes your code more reliable.

---

## 21. Iterators and Generators
Generators create values one by one and can save memory.

```python
def square_numbers(limit):
    for i in range(limit):
        yield i * i

for value in square_numbers(5):
    print(value)
```

These are helpful when working with large data.

---

## 22. Summary
Python is a strong choice for data science because it is:
- easy to learn
- powerful for analysis
- supported by many libraries
- popular in the real world

Practice each topic little by little, and your coding skills will improve quickly.
