# Loops example
# Loops repeat actions many times.

for i in range(3):
    print("For loop value:", i)

count = 1
while count <= 3:
    print("While loop value:", count)
    count += 1

for number in range(6):
    if number == 3:
        continue
    print("Number:", number)
