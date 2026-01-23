###### PROGRAMMING TERMINOLOGY
### FIX THE SYNTAX
number = int(input("Please type in a number: "))
if number > 100:
    print("The number was greater than one hundred")
    number -= 100
    print("Now its value has decreased by one hundred")
    print("Its value is now", number)

print(number, "must be my lucky number!")
print("Have a nice day!")

### NUMBER OF CHARACTERS
string = str(input("Please type in a word:"))
length = len(string)

if length > 1:
    print(f"There are {length} letters in the word {string}")
print("Thank you!")

### TYPECASTING
x = float(input("Please type in a number:"))

integer = int(x)
decimal = x - integer

print(f"Integer part: {integer}")
print(f"Decimal part: {decimal}")





###### MORE CONDITIONALS
### AGE OF MATURITY
age = int(input("How old are you?"))

if age < 18:
    print("You are not of age!")
else:
    print("You are of age!")

### GREATER THAN OR EQUAL TO
num1 = int(input("Please type in the first number:"))
num2 = int(input("Please type in another number:"))

if num1 > num2:
    print(f"The greater number was {num1}")
elif num2 > num1:
    print(f"The greater number was {num2}")
else:
    print("The numbers are equal!")

### THE ELDER
# Person 1
name1 = str(input("Person 1 name:"))
age1 = int(input("Person 1 age:"))

# Person 2
name2 = str(input("Person 2 name:"))
age2 = int(input("Person 2 age:"))

if age1 > age2:
    print(f"The elder is {name1}")
elif age2 > age1:
    print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are the same age")

### ALPHABETICALLY LAST
word1 = str(input("Please type in the 1st word:"))
word2 = str(input("Please type in the 2nd word:"))

if word1 > word2:
    print(f"{word1} comes alphabetically last.")
elif word2 > word1:
    print(f"{word2} comes alphabetically last.")
else:
    print("You game the same word twice.")





###### COMBINING CONDITIONS
### AGE CHECK
age = int(input("What is your age?"))

if age >= 5 and age < 120:
    print(f"Ok, you're {age} years old")
elif age >= 0 and age < 5:
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")

### NEPHEWS
name = str(input("Please type in your name:"))

#if name == "Huey" or name == "Dewey" or name == "Louie":
#    print("I think you might be one of Donald Duck's nephews.")
#elif name == "Morty" or name == "Ferdie":
#    print("I think you might be one of Mickey Mouse's nephews.")
#else:
#    print("You're not a nephew of any character I know of.")

donald = ["Huey", "Dewey", "Louie"]
mickey = ["Morty", "Ferdie"]

if name in donald:
    print("I think you might be one of Donald Duck's nephews.")
elif name in mickey:
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")

### GRADES AND POINTS
points = int(input("How many points []:"))

if points < 0 or points > 100:
    print("Grade: impossible!")
elif points >= 0 and points < 50:
    print("Grade: fail")
elif points >= 50 and points < 60:
    print("Grade: 1")
elif points >= 60 and points < 70:
    print("Grade: 2")
elif points >= 70 and points < 80:
    print("Grade: 3")
elif points >= 80 and points < 90:
    print("Grade: 4")
elif points >= 90 and points <= 100:
    print("Grade: 5")

### FIZZBUZZ
num = int(input("Number:"))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")

### LEAP YEAR
year = int(input("Please type in a year:"))

leap_year = False

if year % 100 == 0:
    if year % 400 == 0:
        leap_year = True
elif year % 4 == 0:
    leap_year = True

if leap_year == True:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

### ALPHABETICALLY IN THE MIDDLE
first = str(input("1st letter:"))
second = str(input("2nd letter:"))
third = str(input("3rd letter:"))

if first < second and first < third:
    if second < third:
        print(f"The letter in the middle is {second}")
    else:
        print(f"The letter in the middle is {third}")
elif second < first and second < third:
    if first < third:
        print(f"The letter in the middle is {first}")
    else:
        print(f"The letter in the middle is {third}")
elif third < first and third < second:
    if first < second:
        print(f"The letter in the middle is {first}")
    else:
        print(f"The letter in the middle is {second}")

# print(f"the letter in the middle is {}")

### GIFT TAX CALCULATOR
value = int(input("Value of gift:"))
lower_lim = 0
rate = 0
floor = 0
tax = 0

if value < 5000:
    tax = 0
elif value >= 5000 and value < 25000:
    lower_lim = 100
    rate = 0.08
    floor = 5000
elif value >= 25000 and value < 55000:
    lower_lim = 1700
    rate = 0.10
    floor = 25000
elif value >= 55000 and value < 200000:
    lower_lim = 4700
    rate = 0.12
    floor = 55000
elif value >= 200000 and value < 1000000:
    lower_lim = 22100
    rate = 0.15
    floor = 200000
elif value >= 1000000:
    lower_lim = 142100
    rate = 0.17
    floor = 1000000

tax = lower_lim + (value - floor) * rate

if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")





###### SIMPLE LOOPS
### SHALL WE CONTINUE?
while True:
    print("hi")
    prompt = str(input("Shall we continue?"))
    if prompt == "no":
        print("okay then")
        break

### INPUT VALIDATION
while True:
    num = int(input("Please type in a number:"))
    
    if num == 0:
        print("Exiting...")
        break
    
    if num > 0:
        print(sqrt(num))
    else:
        print("Invalid number")

### FIX THE CODE: COUNTDOWN
print("Countdown!")
number = 5
while True:
  print(number)
  number -= 1
  if number == 0:
    break

print("Now!")

### REPEAT PASSWORD
pw = str(input("Password:"))

while True:
    repeat_pw = str(input("Repeat password:"))

    if pw == repeat_pw:
        print("User account created!")
        break

    print("They do not match!")

### PIN AND NUMBER OF ATTEMPTS
attempts = 0

while True:
    code = int(input("PIN:"))
    attempts += 1

    if code == 4321:
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break
    
    print("Wrong")

### THE NEXT LEAP YEAR
year = int(input("Year: "))
leap_year = year + 1
while True:
    if leap_year % 400 == 0:
        break
    if leap_year % 4 == 0 and leap_year % 100 != 0:
        break
    leap_year += 1

print(f"The next leap year after {year} is {leap_year}")

### STORY
story = ""
last_word = ""

while True:
    word = str(input("Please type in a word: "))

    if word == "end":
        break
    
    if last_word == word:
        break
    
    story += word + " "
    last_word = word

print(story)

### WORKING WITH NUMBERS
count = 0
summation = 0
pos = 0
neg = 0

print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number:"))
    
    if num == 0:
        break
    
    summation += num
    count += 1
    if num < 0:
        neg += 1
    elif num > 0:
        pos += 1

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {summation}")
print(f"The mean of the numbers is {summation / count}")
print(f"Positive numbers {pos}")
print(f"Negative numbers {neg}")





###### END PART2