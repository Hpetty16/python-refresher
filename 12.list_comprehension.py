numbers = [1, 3, 5]
squares = [x * 2 for x in numbers]

# list comp. are usually in one line. How to build a list comp. is what you want to put into your new list (X*2), for the variable youre using (for x), in #'s (in numbers)

# -- Dealing with strings --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)


# -- Can make a new list of friends whose name starts with S --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)

#this is the example of how do the second example into a list comp.

# it is also important to rember that when we use list comp. a new list is created.


# -- List comprehension creates a _new_ list --

friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]  # same as above

print(friends)
print(starts_s)
print(friends is starts_s) #shows as false in the terminal
print("friends: ", id(friends), " starts_s: ", id(starts_s))

# id is relates to the memory address in which the lists are stored.


# Append in Python is a pre-defined method used to add a single item to certain collection types. Without the append method, developers would have to alter the entire collection's code for adding a single value or item.