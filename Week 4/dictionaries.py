# This file will be looking at how to make dictionaries
# and the practice quiz for the module will be stored
# within this particular code at the end

# Starting with simply creating a dictionary
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts) # It's okay to mix and match data types
print(file_counts["txt"])
file_counts["cfg"] = 8
file_counts["csv"] = 17
print(file_counts)
del file_counts["cfg"]
print(file_counts)

# iterating over the contents of a dictionary
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension)
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))
for value in file_counts.values():
    print(value)

# Example of counting how many times letters appear in a text
def count_letters(text):
    result = {} # Intializing an empty dictionary
    for letter in text: # Going through each letter in the given string
        if letter not in result: # For each letter check if it's already
            result[letter] = 0 # in the dictionary
        result[letter] += 1
    return result

print(count_letters("a long string with a lot of letters"))
# You can also iterate through dictionaries using the .items() method
# the .items() method creates a tuple that uses the first value
# as the key and the second as a value
# If you only wish to access keys in a dictionary use .keys() values = .values()

def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(user+"@"+domain)
    return emails

print(email_list({"gmail.com": ["clark.kent", "diana.prince"]}))

def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():
        for user in users:
            if user in user_groups:
                user_groups[user].append(group)
            else:
                user_groups[user] = [group]
    return user_groups
print(groups_per_user({"local": ["admin", "userA"], "public":["admin", "userB"]}))