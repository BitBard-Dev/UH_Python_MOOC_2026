###### GETTING STARTED
### EMOTICON
print(":-)")

### SEVEN BROTHERS
print("Aapo")
print("Eero")
print("Juhani")
print("Lauri")
print("Simeoni")
print("Timo")
print("Tuomas")

### ROW ROW ROW YOUR BOAT
print("Row, row, row your boat,")
print("Gently down the stream.")
print("Merrily, merrily, merrily, merrily,")
print("Life is but a dream.")

### MINUTES IN A YEAR
minInYear = 365 * 24 * 60
print(f"There are {minInYear} minutes in a year")

### PRINT SOME CODE
print('print("Hello there!")')





###### INFORMATION FROM THE USER
### NAME TWICE
name = input("What is your name?")
print(name)
print(name)

### NAME AND EXCLAMATION MARKS
name = str(input("What is your name?"))
print("!"+name+"!"+name+"!")

### NAME AND ADDRESS
firstName = str(input("Given name: "))
lastName = str(input("Family name: "))
streetAddress = str(input("Street address: "))
cityPostalCode = str(input("City and postal code: "))

print(firstName + " " + lastName)
print(streetAddress)
print(cityPostalCode)

### UTTERANCES
part1 = input("The 1st part: ")
part2 = input("The 2nd part: ")
part3 = input("The 3rd part: ")
print(part1 + "-" + part2 + "-" + part3 + "!")

### STORY
name = str(input("Please type in a name:"))
year = str(input("Please type in a year:"))
print(f"{name} is a valiant knight, born in the year {year}. One morning {name} woke up to an awful racket: a dragon was approaching the village. Only {name} could save the village's residents.")





##### MORE ABOUT VARIABLES
### EXTRA SPACE
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old")
print(f"\nmy skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})")
print(f"\nI am looking for a job with a salary of {lower}-{upper} euros per month")

### ARITHMETICS
x = 27
y = 15
print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} / {y} = {x/y}")

### PRINT A SINGLE LINE
print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4, end="")





##### ARITHMETIC OPERATIONS
### TIMES FIVE
number = int(input("Please type in a number:"))
print(f"{number} times 5 is {number * 5}")

### NAME AND AGE
name = str(input("What is your name?"))
year = int(input("Which year were you born?"))
print(f"Hi {name}, you will be {2021 - year} years old at the end of the year 2021")

### SECONDS IN A DAY
#days = flt(input("How many days?"))
print(f"Seconds in that many days: {(int(input('How many days?'))) * 86400}")

### PRODUCT
product = 0
number = int(input("Please type in the first number: "))
product = number

number = int(input("Please type in the second number: "))
product *= number

number = int(input("Please type in the third number: "))
product *= number

# product = number * number * number

print("The product is", product)

### SUM AND PRODUCT
num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
print(f"The sum of the numbers: {num1 + num2}")
print(f"The product of the numbers: {num1 * num2}")

###SUM AND MEAN
list = []
entries = 4
for i in range(entries):
    num = int(input(f"Number {i + 1}"))
    list.append(num)

summation = sum(list)
mean = summation / entries

print(f"The sum of the numbers is {summation} and the mean is {mean}")
#n1 = int(input("Number 1:"))
#n2 = int(input("Number 2:"))
#n3 = int(input("Number 3:"))
#n4 = int(input("Number 4:"))

### FOOD EXPENDITURE
caf_visits = int(input("How many times a week do you eat at hte student cafeteria?"))
student_lunch_price = float(input("The price of a typical student lunch?"))
weekly_groceries_cost = float(input("How much money do you spend on groceries in a week?"))
caf_weekly_cost = caf_visits * student_lunch_price
tot_weekly_cost = caf_weekly_cost + weekly_groceries_cost

print(f"Average foof expenditure:\nDaily: {tot_weekly_cost / 7} euros\nWeekly: {tot_weekly_cost} euros")

### STUDENTS IN GROUPS
tot_students = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))

if tot_students % group_size == 0:
    num_groups = int(tot_students / group_size)
else: num_groups = int((tot_students // group_size) + 1)

print(f"Number of groups formed: {num_groups}")





##### CONDITIONAL STATEMENTS
### ORWELL
x = int(input("Please type in an integer:"))
if x == 1984:
    print("Orwell")

### ABSOLUTE VALUE
x = int(input("Please type in an integer:"))

if x < 0:
    x = abs(x)

print("The absolute value of this number is", x)

### SOUP OR NO SOUP
name = str(input("Please tell me your name:"))
soup_price = 5.90

if name != "Jerry":
    portions = int(input("How many portions of soup?"))
    print(f"The total cost is {portions * soup_price}")

print("Next please!")

### ORDER OF MAGNITUDE
num = int(input("Please type in a number:"))

if num < 1000:
    print("This number is smaller than 1000")
if num < 100:
    print("This number is smaller than 100")
if num < 10:
    print("This number is smaller than 10")
print("Thank you!")

### CALCULATOR
num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
operation = str(input("Operation:"))

if operation == "add":
    print(f"{num1} + {num2} = {num1 + num2}")
if operation == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")
if operation == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")
if operation == "divide":
    print(f"{num1} / {num2} = {num1 / num2}")

### TEMPERATURES
temp_f = int(input("Please type in a temperature (F):"))
temp_c = (temp_f - 32) / 1.8

print(f"{temp_f} degrees Fahrenheit equals {temp_c} degrees Celsius")
if temp_c < 0:
    print("Brr! It's cold in here!")

### DAILY WAGES
hr_wage = float(input("Hourly wage:"))
hr_worked = int(input("Hours worked:"))
day_of_week = str(input("Day of the week:"))

if day_of_week == "Sunday":
    hr_wage *= 2

print(f"Daily wages: {hr_wage * hr_worked} euros")

### LOYALTY BONUS
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
elif points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")

### WHAT TO WEAR TOMORROW
print("What is the weather forecast for tomorrow?")
temp_c = int(input("Temperature:"))
rain = str(input("Will it rain(yes/no):"))

if temp_c <= 100:
    print("Wear jeans and a T-shirt")
if temp_c <= 20:
    print("I recommend a jumper as well")
if temp_c <= 10:
    print("Take a jacket with you")
if temp_c <= 5:
    print("Make it a warm coat, actually\nI think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")

### SOLVING A QUADRATIC EQUATION
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))

zero1 = (((b * -1) + sqrt((b**2)- (4 * a * c)))/(2 * a))
zero2 = (((b * -1) - sqrt((b**2)- (4 * a * c)))/(2 * a))

print(f"The roots are {zero1} and {zero2}")





##### END PART1