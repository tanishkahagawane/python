# Data Structures
# - stores multiple values together

# Lists: Like a shopping list (ordered items)
# Dictionaries: Like a phone book (name > number)
# Tuples: Like coordinates (fixed values)
# Sets: Like a bag of unique items

#Lists
fruits = ["apple", "banana", "orange"]

# Get items
print(fruits[0])    # "apple" (first item)
print(fruits[1])    # "banana"
print(fruits[-1])   # "orange" (last item)
print(fruits[-2])   # "banana" (second to last)

# Slicing
print(fruits[0:2])  # ["apple", "banana"]
print(fruits[1:])   # ["banana", "orange"]

fruits = ["apple", "banana", "orange"]
###############
# Changing lists
#  Change an item
fruits[0] = "mango"
print(fruits)  # ["mango", "banana", "orange"]

# Add items
fruits.append("grape")      # Add to end
print(fruits) 
fruits.insert(1, "kiwi")    # Insert at position
print(fruits) 

# Remove items
fruits.remove("banana")     # Remove by value
print(fruits) 
last = fruits.pop()        # Remove and return last
print(fruits) 
del fruits[0]              # Remove by index
print(fruits) 
##################################################################################
##################################################################################
# Dictionaries:

person = {"name": "Alice", "age": 30, "city": "New York"}

# Get values by key
print(person["name"])       # "Alice"
print(person["age"])        # 30
#print(person["job"])        #error 

# Safer with get()
print(person.get("job"))    # None (no error)
print(person.get("job", "Unknown"))  # "Unknown" (default)

##################################################################################
##################################################################################
# Tuples:
#Works with immutable sequence

# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = (42)  # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20

point = (3, 5)
colors = ("red", "green", "blue")

# Get items
print(point[0])      # 3
print(colors[-1])    # "blue"

# Slicing works too
print(colors[0:2])   # ("red", "green")

##################################################################################
##################################################################################
# sets:
# Work with unique collections

# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}