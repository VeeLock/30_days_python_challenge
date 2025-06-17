import math

print("Day 2: 30 Days of python programming")
first_name = "Vilde"
last_name = "Numme"
full_name = "Vilde Numme"
country = "Norway"
city = "Sørumsand"
age = (int("31"))
year = "1993"
is_married = False
is_light_on = True
skills = ["html", "css", "python"]

# Checking datatypes
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(skills))

# Length of first name vs last name
print(len(first_name))
print(len(last_name))

# Declade 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

total = num_one + num_two
print(total)

diff = num_two - num_one
print(diff)

product = num_two * num_one
print(product)

division = num_one / num_two
print(division)

remainder = num_two % num_one
print(remainder)

exp = num_two ** num_one
print(exp)

floor_division = num_two // num_one
print(floor_division)

radius = 30
area_of_circle = math.pi * radius ** 2
print(area_of_circle)

circum_of_circle = 2 * math.pi * radius
print(circum_of_circle)

first_name = input("What is your name? ")
print(first_name)
last_name = input("What's your last name?")
print(last_name)
country = input("Where are you from?")
print(country)
age = int(input("How old are you?"))
print(age)
