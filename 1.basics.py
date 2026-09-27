##Variable
name ="Alice"
age = 25
name ="Dave"
is_student = True
print(name)

##DataTypes

#1. Integer 
total =  10-7

#2. String
first_name = "Alice"
last_name = "Sa"
full_name  = first_name + " " + last_name

print(full_name)

my_long_string = """
My name is Tanishka
I'm 25
"""

print(my_long_string)

long_dash="-"*30
print(long_dash)
print(len(long_dash))

# 3.Booleans

age = 25
has_license  =  True
drunk = True

can_drive =  age >= 16  and has_license and not drunk
print(can_drive)


# string manipulation - f string
name = "Ray"
string = f"Hi There, my name is {name}!"
print(string)

# String methods
text = "Python ProgramMing"

print(text.lower())      # "python programming"
print(text.upper())      # "PYTHON PROGRAMMING"
print(text.title())      # "Python Programming"


# Control Flow

temperature = 35

if temperature > 30:
    print("Its very hot!")
elif temperature > 25:
    print("Its hot!")
else:
    print("Its nice weather!")

# Loops

#for loop

for i  in range(5):
    print(i)

# Count from 1 to 5
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# Count by 2s
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8
