
# defines list[]
l = ["Bob", "Rolf", "Anne"]
# defines tuple(). The difference between tuple and list is that you cant modify a tuple, where you can add and remove items from a list 
t = ("Bob", "Rolf", "Anne")
# defines a set. you cant have duplicates in the set{bob,bob,arron} wouldnt be ok because you cat have more than one item. also the order isnt gaurenteed and can change at any momment
s = {"Bob", "Rolf", "Anne"}

# Access individual items in lists and tuples using the index.

print(l[0])
print(t[0])
# print(s[0])  # This gives an error because sets are unordered, so accessing element 0 of something without order doesn't make sense.

# Modify individual items in lists using the index.

l[0] = "Smith"
# t[0] = "Smith"  # This gives an error because tuples are "immutable".

print(l)
print(t)

# Add to a list by using `.append`

l.append("Jen")
print(l)
# Tuples cannot be appended to because they are immutable.

#remove from a list by using ".remove"
l.remove("Bob")
print(l)

# Add to sets by using `.add`

s.add("Jen")
print(s)

# Sets can't have the same element twice.

s.add("Bob")
print(s)


# List: Lists are just like dynamic sized arrays, declared in other languages (vector in C++ and ArrayList in Java). Lists need not be homogeneous always which makes it the most powerful tool in Python. The main characteristics of lists are – 

# The list is a datatype available in Python which can be written as a list of comma-separated values (items) between square brackets.
# List are mutable .i.e it can be converted into another data type and can store any data element in it.
# List can store any type of element.


# Tuple: Tuple is a collection of Python objects much like a list. The sequence of values stored in a tuple can be of any type, and they are indexed by integers. Values of a tuple are syntactically separated by ‘commas’. Although it is not necessary, it is more common to define a tuple by closing the sequence of values in parentheses. The main characteristics of tuples are – 

# Tuple is an immutable sequence in python.
# It cannot be changed or replaced since it is immutable.
# It is defined under parenthesis().
# Tuples can store any type of element.


# Set: In Python, Set is an unordered collection of data type that is iterable, mutable, and has no duplicate elements. The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. The main characteristics of set are –

# Sets are an unordered collection of elements or unintended collection of items In python.
# Here the order in which the elements are added into the set is not fixed, it can change frequently.
# It is defined under curly braces{}
# Sets are mutable, however, only immutable objects can be stored in it.




