# Error handling example
# try/except helps your program handle mistakes safely.

try:
    number = int("abc")
except ValueError:
    print("That is not a valid integer")
else:
    print("Conversion was successful")
finally:
    print("This block always runs")
