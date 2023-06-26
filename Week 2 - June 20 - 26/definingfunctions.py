# Written by Kayla Waddy
# These are programs that are used for defining functions within Python

# Finding the area of a triangle program
def area_triangle(base, height):
    return base * height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))


# Converting to seconds
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

#Creating a custom greeting
def greeting(name):
    print("Welcome, " + name)
result = greeting("Christine")
print(result)