# Arrays

employees = ["Görkem", "Mehmet", "Ali"]
employees_age = [25, 30, 35]
print(employees)

# Dictionary

employee = {
    "name": "Ahmet",
    "age": 25,
    "height": 1.75,
    "weight": 75
}

print(employee.get("name"))
# or
print(employee["name"])


# Set

persons = set(["Ahmet", "Mehmet", "Ali"])
print(persons)
print(type(persons))

# Tuple

person = ("Ahmet", "Mehmet", "Ali")
print(person)

# Get rectangle dimensions from user
length = float(input("Please enter the length of the rectangle: "))
width = float(input("Please enter the width of the rectangle: "))

# Calculate and print the perimeter
perimeter = 2 * (length + width)
print("The perimeter of the rectangle is: {}".format(perimeter))

# Get circle radius from user
radius = float(input("Please enter the radius of the circle: "))

# Calculate and print the circumference
pi = 3.14
circumference = 2*pi*radius
print("The circumference of the circle is: {:.2f}".format(circumference))

# Calculate and print the area
area = pi*(radius**2)
print("The area of the circle is: {}".format(area))

# Kullanıcıdan alınan 3 sayının toplamı, çarpımı ve ortalamasını hesaplayan algoritma

num1 = int(input("Enter first number."))
num2 = int(input("Enter second number."))
num3 = int(input("Enter third number."))
total = num1 + num2 + num3
product = num1 * num2 * num3
average = total / 3
print(f"Total: {total}, Product: {product}, Average: {average}")

# Kullanıcıdan %30 not ağırlığına sahip 2 vize ve %40 not ağırlığına sahip final notu alarak ortalama hesaplayan algoritma

vize1 = int(input("Enter first midterm exam grade."))
vize2 = int(input("Enter second midterm exam grade."))
final = int(input("Enter final exam grade."))

average = (vize1*0.3) + (vize2*0.3) + (final*0.4)

print(f"Average: {average}")