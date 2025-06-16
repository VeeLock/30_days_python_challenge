print("hei")
print(len('hello world'))
print(type("hello world"))
print(str(10))
input("What is your name?: ")


# Example of valid variable names
# firstname
# lastname
# age
# country
# city
# first_name
# last_name
# capital_city
# _if  # if we want to use reserved word as a variable
# year_2021
# year2021
# current_year_2021
# birth_year
# num1
# num2

# Variables in Python
first_name = 'Vilde'
last_name = 'Numme'
country = 'Norway'
city = 'Oslo'
age = 31
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Vilde',
    'lastname': 'Numme',
    'country': 'Norway',
    'city': 'Oslo'
}

print("First Name:", first_name)
print("First name length: ", len(first_name))
print("Last name: ", last_name)
print("Last name length: ", len(last_name))
print("Country: ", country)
print("City: ", city)
print("Age: ", age)
print("Married: ", is_married)
print("Skills: ", skills)
print("Person information: ", person_info)


print(first_name, last_name, country, age, is_married)

first_name = input("What is your name: ")
age = input("How old are you? ")

print(first_name)
print(age)

# int to float
num_int = 10
print("num_int", num_int)
num_float = float(num_int)
print("num_float:", num_float)

# float to int
gravity = 9.81
print(int(gravity))

# int to str
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str)

# str to int or float
num_str = "10.6"
num_float = float(num_str)
print("num_float", float(num_str))
num_int = int(num_float)
print("num_int", int(num_int))

# str to list
first_name = "Vilde"
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)
