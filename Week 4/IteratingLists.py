animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))
#Introducing the enumerating function
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}". format(index+1, person))

# Making email addresses using enumerate by defining the function
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name,email))
    return result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))

# Creating a list in a shorter way
multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)

#List comprehension
multiples = [x*7 for x in range(1,11)]
print(multiples)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)
z = [x for x in range(0, 101) if x % 3 == 0]
print(z)

filenames = ["program.c", "stdio.hpp"]
newfilenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new = filename.replace("hpp", "h")
        newfilenames.append(new)
    else:
        newfilenames.append(filename)
print(newfilenames)

# Making a pig latin ending with splitting and combining
# new words together
def pig_latin(text):
    say = ""
    words = text.split()
    for word in words:
        say += word[1:] + word[0] + "ay "
    return say
print(pig_latin("hello how are you"))
print(pig_latin("programming in python is fun"))