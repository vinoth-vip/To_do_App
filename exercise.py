import math

# ranking = ['John', 'Sen', 'Lisa']
# index = ranking.index(input("Enter person name: ")) + 1
# print(index)

#--------------------------------------------------------------------------------------
# mood = "AYIR"
# strength = 2.17
# rank = 50
# print(type(mood), type(strength), type(rank))

#--------------------------------------------------------------------------------------
# color_codes = (
#     ('red', 255, 0),
#     ('green', 0, 255),
#     ('blue', 0, 0, 255)
# )
# print(type(color_codes))

#--------------------------------------------------------------------------------------
# serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
# print(serials[3])

#--------------------------------------------------------------------------------------
# seconds = [1.23, 1.45, 1.02]
# current = 1.11
# seconds.append(current)
# print(seconds)

#--------------------------------------------------------------------------------------
# filenames = ['document', 'report', 'presentation']
# for a, b in enumerate(filenames):
#     row = f"{a}.{b.capitalize()}.txt"
#     print(row)

#---------------------------------------------------------------------------------
# name = "jana"
# comp = "wipro"
# file = f"I'm {name} 134868 %*&@(*@ working in {comp}."
# print(file)

#--------------------------------------------------------------------------------------
# ips = ['100.122.133.105', '100.122.133.111']
# Index = int(input("Enter the index of the IP you want: ")) - 1
# chosen_ip = ips[Index]
# print(f"You chose {chosen_ip}")

#--------------------------------------------------------------------------------------
# file = open("task.txt", 'r')
# text = file.read()
# print(text)

#--------------------------------------------------------------------------------------

# file = open("task.txt")
# text = file.read()
# print(text.title())

#--------------------------------------------------------------------------------------
# file = open("task.txt")
# text = file.read()
# print(text.__len__())


#--------------------------------------------------------------------------------------
# file = 'essay.txt'
# file = open(file, 'w')
# text = file.write("thunder")
# print(text)

#--------------------------------------------------------------------------------------
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# for files in filenames:
#     files = open(files, 'w')
#     files.write("Hello")
#     files.close()

#--------------------------------------------------------------------------------------

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# for files in filenames:
#     files = open(files, 'r')
#     content = files.read()
#     print(content)
#     files.close()

#------------------------------------------------------------------------------------------

# names = ["john smith", "jay santi", "eva kuki"]
# capital = [name.title() for name in names]
# print(capital)

#-----------------------------------------------------------------------------------------

# names = ["john smith", "jay santi", "eva kuki"]
# capital = [name.__len__() for name in names]
# print(capital)

#------------------------------------------------------------------------------------------

# user_entries = ['10', '19.1', '20']
# capital = [float(name) for name in user_entries]
# print(capital)

#----------------------------------------------------------------------------------------------

# user_entries = ['10', '19.1', '20']
# capital = [float(name) for name in user_entries]
# adding_list = sum(capital)
# print(adding_list)

#-------------------------------------------------------------------------------------------

# temperatures = [10, 12, 14]
# temperatures = [str(i) + '\n' for i in temperatures]
# file = open("file.txt", 'w')
#
# file.writelines(temperatures)

#-------------------------------------------------------------------------------------------

# numbers = [10.1, 12.3, 14.7, "kjd"]
# numbers = [type(item) for item in numbers]
# print(numbers)

#---------------------------------------------------------------------------------------------

# password = input("Enter the password: ")
#
# if len(password) > 7:
#     print("Great password there!")
# else:
#     print("Your password is weak.")

#------------------------------------------------------------------------------------------------

# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#     calculate = value/total_value * 100
#     print(f"That is {calculate}%")
#
# except ValueError:
#     print("You need to enter the number. Run the program.")

# ---------------------------------------------------------------------------------------------------

# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#     calculate = value/total_value * 100
#     print(f"That is {calculate}%")
#
# except ZeroDivisionError:
#     print("Your total value cannot by zero.")

# -----------------------------------------------------------------------------------------------------

# colors = [11, 34, 98, 43, 45, 54, 54]
# for i in colors:
#     if i > 50:
#         print(i)

# -------------------------------------------------------------------------------------------------------

# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     value = max(grades)
#     return value
#
#
# print(get_max())

# ---------------------------------------------------------------------------------------------------------

# def get_max():
#     grades = [-9.6, 9.2, 9.7]
#     Values = f'Max: {max(grades)}, Min: {min(grades)}'
#     return Values
#
#
# print(get_max())

# ----------------------------------------------------------------------------------------------------------

# def liters_to_m3(liters):
#     # Conversion factor: 1000 liters = 1 cubic meter
#     cubic_meters = liters / 1000
#     return cubic_meters
#
# print(liters_to_m3(4))
# -----------------------------------------------------------------------------------------------

# def strength(password):
#     # Check if the password meets the specified conditions
#     if len(password) >= 8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
#         return "Strong Password"
#     else:
#         return "Weak Password"
#
#
# print(strength("sdjjs"))

# -----------------------------------------------------------------------------------------------------------

# def calculate_average(lst):
#     # Check if the list is not empty
#     if len(lst) > 0:
#         # Calculate the average by dividing the sum of elements by the number of elements
#         average = sum(lst) / len(lst)
#         return average
#     else:
#         # Return 0 if the list is empty to avoid division by zero
#         return 0
#
#
# lst = [10,20,30,40]
# print(calculate_average(lst))

#--------------------------------------------------------------------------------------------------

# def person(name):
#     value = f'Hi {name}'
#     return value
#
#
# name = input("Enter the name: ")
# print(person(name))

# --------------------------------------------------------------------------------------------------

# def write_work(path, task_arg, type="false"):
#     Value = path + task_arg + type
#     return Value
#
#
# print(write_work("./pythonProject", "sum.txt", "True"))
# ---------------------------------------------------------------------------------------------------

# def person(name):
#     value = name
#     return "Hi " + value.capitalize()
#
#
# name = input("enter: ")
# print(person(name))

# ------------------------------------------------------------------------------------------------------

# def get_age(year_of_birth, current_year=2024):
#     calculate = current_year - year_of_birth
#     return calculate
#
#
# year_of_birth = int(input("Enter the year_of_birth: "))
# print(get_age(year_of_birth))

# ----------------------------------------------------------------------------------------------------------

# def get_nr_items(one="john,lisa, teresa"):
#     number_of_items = len(one.split(","))
#     return number_of_items
#
#
# print(get_nr_items())

# -----------------------------------------------------------------------------------------------------------

# def area_of_square(foo):
#     square = foo * foo
#     return square
#
#
# foo = int(input("Enter the number: "))
# print(area_of_square(foo))

# --------------------------------------------------------------------------------------------------------

# def climate(temperature):
#     if temperature > 7:
#         return "warm"
#     elif temperature <= 7:
#         return "cold"
#
#
# temperature = int(input("Enter the temperature: "))
# print(climate(temperature))

# ------------------------------------------------------------------------------------------------------

# def length(foo):
#     if len(foo) < 8:
#         return False
#     elif len(foo) >= 8:
#         return True

# --------------------------------------------------------------------------------------------------------

# def water_state(temperature):
#     if temperature <= 0:
#         return "Solid"
#     elif temperature > 0 & temperature < 100:
#         return "Liquid"
#     elif temperature >= 100:
#         return "Gas"

# -------------------------------------------------------------------------------------------------------

# FREEZING_POINT = 0
# BOILING_POINT = 100
#
#
# def water_state(temperature):
#     if temperature <= FREEZING_POINT:
#         return "Solid"
#     elif FREEZING_POINT < temperature < BOILING_POINT:
#         return "Liquid"
#     else:
#         return "Gas"

# ---------------------------------------------------------------------------------------------

# def climate(temparature):
#     if temparature > 25:
#         return "Hot"
#     elif 15 <= temparature <= 25:
#         return "Warm"
#     elif temparature < 15:
#         return "Cold"

# ---------------------------------------------------------------------------------------------------
# import random
#
# lowerBond = int(input("Enter the lowerbond: "))
# upperBond = int(input("Enter the upperBond: "))
#
# rand = random.randint(lowerBond, upperBond)
#
# print(rand)

# -----------------------------------------------------------------------------------------------

# def liquid(fluids):
#     millilieters = 29.57353
#     liquid = fluids * millilieters
#     return liquid
#
#
# fluid = int(input("enter the fluid: "))
#
# print(liquid(fluids=fluid))
#
# exit()

# --------------------------------------------------------------------------------------------------------------------------------------

