# PYTHON PROGRAMMING

# Numbers
9 # Integer
9.2 # Float

#Strings
"Hello World" # String

# type function

type(9) # int

# Print function

# print("Hello World")

# STRING METHODS

# len
a = "HELLO WORLD"
len(a) # 11

# upper & lower
a.upper() # HELLO WORLD
a.lower() # hello world
# print(a.upper(), a.lower())

a.islower() # False
a.isupper() # True

# replace
a.replace("WORLD", "PYTHON") # HELLO PYTHON


# strip
text = "   Hello World   "
text.strip() # Hello World # Remove spaces
text = "***Hello World***"
text.strip("*") # Hello World # Remove * characters

# dir
dir(a) # List of methods

a.capitalize() # Hello world
a.title() # Hello World


# Substrings
a[0] # H
a[0:5] # HELLO
# print(a[:3]) # HEL
# print(a[3:7]) # LO W

# Variables

name = "John"
surname = "Doe"
age = 30
hobbies = ["Python", "JavaScript", "React"]
person = "{0} {1} is {2} years old and likes {3}".format(name, surname, age, hobbies)
# print(person)

# type conversion

#first_number = input("Enter a number: ")
#second_number = input("Enter another number: ")
#result = int(first_number) + int(second_number)
#print(result)


int("9") # 9
float("9.2") # 9.2
float(9)
type(str(9)) # str

# print()
# print("Hello", "World", sep = '_', end= "!\n")

# Data Structures

# Lists []

nots = [90,80,70] 
# print(type(nots))

list = ["John", 30, True, 9.2, ["Python", "JavaScript", "React"]]
# print(type(list))
# print(len(list))

# Indexing
list[0] # John
type(list[1])

# concatenation

all_list = [nots, list]
# print(all_list[1])

list[:3] # ['John', 30, True]
all_list[1][4][1] # JavaScript
all_list[:1] # [[90, 80, 70]]
# print(all_list[:1][0][0])

# List Methods

list = ["Ali", "Veli", "Görkem"]
list[1] = "Ahmet" # Change the value

list[:len(list)] = "Burak", "Mehmet", "Kemal" # Change the values

# Append
list.append("Veli") # Add to the end of the list
list = list + ["Görkem"] # Add to the end of the list

# print(dir(list))

list.append('Python')
list.remove('Python') # Remove the first occurrence of a value

# Insert & Pop

list.insert(0,'Javascript') # Insert a value to a specific index
list.pop(1) # Remove a value from a specific index

list.insert(10, "React") # If the index is greater than the length of the list, the value is added to the end of the list
list.insert(len(list), "Test") # Add to the end of the list

# count
list.count("Veli") # Count the number of occurrences of a value
# print(list.count("Veli"))

# copy 

copy_list = list.copy() # Shallow copy
print(copy_list)

# extend
list.extend(["a","b",10]) # Add multiple values to the end of the list
print(list)

# index - find the index of a value

list.index("Veli")
# print(list.index("Veli"))

# reverse 

list.reverse() # Reverse the list
# print(list)

# sort
numbers = [9,2,5,1,7,3,4,6,8]
numbers.sort() # Sort the list
print(numbers)

# clear
list.clear() # Remove all items from the list
print(list)

# Tuples - Immutable

t = ("Ali",1,2,3,[10,20])
# print(t)

t = ("item")
t_1 = ("item",)
print(type(t)) # str
print(type(t_1)) # tupl

# Dictionaries

person = {
    "name": "John",
    "surname": "Doe",
    "age": 30,
    "hobbies": ["Python", "JavaScript", "React"]
}

# Dictionary - Choose a value

person["name"] # John
person.get("name") # John
# print(person.get("hobbies")[0]) # Python

# Dictionary - Add a value - Update a value

person["job"] = "Developer" # Add a value
person["name"] = "Görkem" # Update a value
# print(person)

# Data Structures - Set

l = ["a","b",123]
s = set(l)

 # tuple to set
 
t = ("a","ali")
s = set(t)

text = "ali_ali2_ali3"
print(set(text))

# set does't allow indexing

# Set - Add a value - Remove a value

l = ["gelecegi", "yazanlar"]
s = set(l)

s.add("ile")
s.add("2024")
# print(s)

s.add("ile") # Doesn't add the same value

s.remove("ile") # Remove a value - If the value does not exist, it gives an error
s.discard("ile") # Remove a value - If the value does not exist, it does not give an error
