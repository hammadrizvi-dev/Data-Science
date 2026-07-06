# Conditional statements example
# if/elif/else helps the program make decisions.

age = 18

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")

# Match case example (Python 3.10+)
day = "Friday"

match day:
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("Weekend is near")
    case _:
        print("Another day")
