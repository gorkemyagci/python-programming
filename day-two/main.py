"""
age = 10 #Integer - int
height = 1.75 #Float - float
name = "Görkem" #String - str
"""

"""
fullName = input("Please enter your fullname: ")
age = int(input("Please enter your age: "))

print("Merhaba", fullName, "yaşınız", age, "dir.")
"""

firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height: "))
weight = float(input("Please enter your weight: "))

print("Benim adım {},  soyadım {}, yaşım {}, boyum {} ve kilom {}.".format(firstName, lastName, age, height, weight))
print(f"{firstName} {lastName} isimli kişinin yaşının { age } olduğunu biliyoruz. Boyu { height } ve kilosu { weight }.")