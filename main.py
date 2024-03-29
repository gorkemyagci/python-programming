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

# Set - Union - Intersection - Difference

# difference() - Returns the difference between two sets
# intersection() - Returns the intersection of two sets - & operator
# union - Returns the union of two sets - | operator
# symmetric_difference() - Returns the symmetric difference between two sets - ^ operator

# difference
set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2)
# print(set1.difference(set2)) # {5}
# print(set2.difference(set1)) # {2}

# symmetric_difference
set1.symmetric_difference(set2)
# print(set1.symmetric_difference(set2)) # {2, 5}

# intersection
set1.intersection(set2) # {1,3} set1 & set2
# print(set1.intersection(set2))
# print(set1 & set2)

# union
set1.union(set2) # {1,2,3,5} set1 | set2
# print(set1.union(set2))


# iki kumenin kesisiminin bos olup olmadigini kontrol etme
# print(set1.isdisjoint(set2)) # False

# bir kumenin butun elemanlarinin baska bir kume icinde yer alip almadigini kontrol etme
# print(set1.issubset(set2)) # False

# bir kume diger kumenin alt kumesi mi
# print(set1.issuperset(set)) # False


# FUNCTIONS
print("a","b", sep = "=")

# How to define a function

def square(x):
    return x**2
    
print(square(5))

def calculate_sum(*args):
    return "Sum: " + str(sum(args))


calculate_sum(1,2,3,4,5,6,7,8,9,10)


# Ön tanımlı argümanlar

def sum(x = 0, y = 0):
    return x + y

print(sum(5,6))

# Arümanların sırası

def calculate(x,y,z):
    return (x + y) * z

# print(calculate(x = 5, y = 6, z = 7))

# When should we use functions?

# print((40+25)/90)

def calculate(x,y,z):
    return (x + y) / z

print(round(calculate(40,25,90),2))


x = calculate(40,25,90)
print(x*2)

# Local and Global Variables

x = 10 # Global variable
y = 20 # Global variable

def test(x, y):
    return x + y # Local variable

test(5,6) # 11

# how to access global variable in a function

x = [] # Global variable

def add_item(y):
    x.append(y) # Access the global variable
    return x

# CONTROL STRUCTURES

# True - False

max = 5000
max == 4000 # False
max == 5000 # True

# if - else - elif

age = 17
required_age = 18

if age >= required_age:
    print("You can vote")
elif age < required_age and age > 0:
    print("You can't vote")
else:
    print("Invalid age")
    
# mini_app
'''
max = 50000
store_name = input("Enter the store name: ")
store_sales = int(input("Enter the store sales: "))

if store_sales > max:
    print("You won a bonus")
elif store_sales == max:
    print("You won a bonus")
else:
    print("You didn't win a bonus")
'''
    
# LOOP - FOR

students = ["Görkem", "Ali", "Veli", "Mehmet"]

for student in students:
    print(student)
    
# For example

salary = [1000,2000,3000,4000,5000]
new_salary = []

for s in salary:
    new_salary.append(s * 1.2)
    
# print(new_salary)

# For with function

def calculateSalary(salary):
    return salary * 20/100 + salary

new_salary = []

for s in salary:
    new_salary.append(calculateSalary(s))
    
# print(new_salary)

# mini app
# if, for and function

salaries = [1000,2000,3000,4000,5000]

def new_salary(salary):
    if (salary < 3000):
        return salary * 1.5
    elif (salary >= 3000 and salary < 4000):
        return salary * 1.3
    else:
        return salary * 1.2
    
new_salaries = []

for s in salaries:
    new_salaries.append(new_salary(s))
    
print(new_salaries)

# break - continue

# Here is an advanced example of using break and continue in a loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# We will iterate over the list and perform different actions based on the number
for num in numbers:
    # If the number is 5, we will skip the rest of the loop and continue with the next number
    if num == 5:
        print("Skipping 5")
        continue
    # If the number is 8, we will break the loop entirely
    if num == 8:
        print("Breaking on 8")
        break
    # If neither condition is met, we will simply print the number
    print(num)
    
# while

number = 1

while number < 5:
    print(f"Number is {number}")
    number += 1
    

# Object Oriented Programming - OOP - Class

#class DataScientist:
#    print('This is a class')
    
# Class attributes
class DataScientist():
    department = ''
    sql = True
    years_of_experience = 0
    languages = []
    
DataScientist.sql
DataScientist.department
DataScientist.years_of_experience

# Changing the class attributes
DataScientist.department = 'Data'
# print(DataScientist.department)

# Class Instances
ds = DataScientist()
ds.department = 'Data'
ds.sql = True
ds.years_of_experience = 5
ds.languages.append('Python')
text = f"Department: {ds.department}, SQL: {ds.sql}, Years of Experience: {ds.years_of_experience}, Languages: {ds.languages}"
print(text)

class DataScientist():
    languages = []
    def __init__(self):
        self.department = ''
        self.sql = True
        self.years_of_experience = 0
        self.languages = []
        
print(DataScientist.languages)

class DataScientist():
    employees = []
    def __init__(self):
        self.languages = []
        self.department = ''
    def add_language(self, new_lang):
        self.languages.append(new_lang)
        
p1 = DataScientist()
p1.add_language('Javascript')
print(p1.languages) # Javascript

# Inheritance

class Employees():
    def __init__(self, firstName, lastName, address):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        
class DataScientists(Employees):
    def __init__(self, programming):
        self.programming = programming
        
        
class MarketingDp(Employees):
    def __init__(self, storyTelling):
        self.storyTelling = storyTelling
        
employee = Employees("John","Doe","Address")
print(f"{employee.firstName} {employee.lastName} {employee.address}")


# Fonksiyonel Programlama

# Pure Function
a = 5

def impure_sum(b):
    return b + a

def pure_sum(a,b):
    return a + b

impure_sum(6)
pure_sum(3,4)

class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []
        
    def read(self):
        self.lines = [line for line in self.file]
    
    def count(self):
        return len(self.lines)

lc = LineCounter('test.txt')
lc.read()
# print(lc.lines)
# print(lc.count())


def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

example_lines = read('test.txt')
lines_count = count(example_lines)
print(lines_count)

# Anonymous Functions

def old_sum(a, b):
    return a + b

old_sum(3,4)

new_sum = lambda a,b : a + b
new_sum(4,5)

list = [('b',3),('c',8),('a',12),('z',1)]

print(sorted(list, key = lambda x: x[1]))

# Vectorel Operations

a = [1,2,3,4]
b = [2,3,4,5]

ab = []

for i in range(0,len(a)):
    ab.append(a[i]*b[i])
    
# print(ab)

# FP

import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([2,3,4,5,6])
# print(a*b)

# map & filter & reduce

liste = [1,2,3,4,5]

for i in list:
    print(1+10)
    
# list(map(lambda x: x*10, liste))

# filter

liste = [1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x: x % 2 == 0, liste)))

# reduce

from functools import reduce

liste = [1,2,3,4]
print(reduce(lambda a,b: a + b, liste))

# Modul Olusturmak

import CalculateModule as cm

cm.new_salary(1000)
cm.new_salary(2000)

from CalculateModule import new_salary

new_salary(5000)

import CalculateModule as cm
cm.salaries

# Exceptions

a = 10
b = 0

try:
    print(a/b)
except ZeroDivisionError:
    print("ZeroDivisionError Error")
    
# type error

a = 10
b = "2"

try:
    print(a/b)
except TypeError:
    print("Type Error")