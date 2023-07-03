# Help with Quiz 3
# Written by Kayla Waddy
# July 3, 2023
# Description: Figuring out the infinite loop within
# the practice quiz
num1 = 0
num2 = 0
for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3
print(num1 + num2)