##### LOOPS WITH CONDITIONS
### PRINT NUMBERS
num = 2

while num <= 30:
    print(num)
    num += 2

### FIX THE CODE: COUNTDOWN
print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
    print(number)
    number -= 1

print("Now!")

### NUMBERS
u_limit = int(input("Upper limit:"))

num = 1

while num < u_limit:
    print(num)
    num += 1

### POWERS OF TWO
u_limit = int(input("Upper limit: "))
num = 1

while num <= u_limit:
    print(num)
    num *= 2

### POWERS OF BASE N
u_limit = int(input("Upper limit: "))
base = int(input("Base: "))
num = 1

while num <= u_limit:
    print(num)
    num *= base

### THE SUM OF CONSECUTIVE NUMBERS, VERSION 1
lim = int(input("Limit: "))
num = 1
sum = 0

while sum < lim:
    sum += num
    num += 1

print(sum)

### THE SUM OF CONSECUTIVE NUMBERS, VERSION 2
lim = int(input("Limit: "))
num = 1
summation = 1
numbers = "1"

while summation < lim:
    num += 1
    summation += num
    numbers += f" + {num}"

print(f"The consecutive sum: {numbers} = {summation}")





##### WORKING WITH STRINGS
### STRING MULTIPLIED
string = str(input("Please type in a string: "))
times = int(input("Please type in an amount: "))

print(string * times)

### THE LONGER STRING
string1 = str(input("Please type in string 1: "))
string2 = str(input("Please type in string 2: "))

length1 = len(string1)
length2 = len(string2)

if length1 > length2:
    print(f"{string1} is longer")
elif length2 > length1:
    print(f"{string2} is longer")
else:
    print("The strings are equally long")

### END TO BEGINNING
string = str(input("Please type in a string: "))
index = -1

while index >= len(string) * -1:
    print(string[index])
    index -= 1

### SECOND AND SECOND TO LAST CHARACTERS
string = str(input("Please type in a string: "))

sec_char = string[1]
#print(sec_char)
sec_last_char = string[len(string)-2]
#print(sec_last_char)

if sec_char == sec_last_char:
    print(f"The second and the second to last characters are {string[1]}")
elif sec_char != sec_last_char:
    print("The second and the second to last characters are different")
else:
    print("Error")

### A LINE OF HASHES
width = int(input("Width: "))
pound = "#"

print(width * pound)

### A RECTANGLE OF HASHES
width = int(input("Width: "))
height = int(input("Height: "))
pound = "#"
count = 1

while count <= height:
    print(width * pound)
    count += 1

### UNDERLINING
while True:
    string = str(input("Please type in a string"))
    if string == "":
        break
    print(string)
    print("-" * len(string))

### RIGHT-ALIGNED
string = str(input("Please type in a string: "))

remainder = 20 - len(string)

print((remainder * "*") + string)

### A FRAMED WORD
string = str(input("Word: "))
length = 28
length -= len(string)
# print(length)

first_space = " " * ((length) // 2)
# print("first", len(first_space))
length -= len(first_space)
sec_space = " " * length
# print("second", len(sec_space))

print("*" * 30)
print("*" + first_space + string + sec_space + "*")
print("*" * 30)

### SUBSTRINGS, PART 1
string = str(input("Please type in a string: "))

# length = len(str(input("Please type in a string: ")))
#print(length) #####
index = 0

for i in range(len(string) + 1):
    print(string[0:i])
    index += 1

### SUBSTRINGS, PART 2
string = str(input("Please type in a string: "))
length = len(string) - 1

while length >= 0:
    print(string[length:])
    length -= 1

### DOES IT CONTAIN VOWELS?
string = str(input("Please type in a string: "))
# string = "aeiou"
if "a" in string:
    print("a found")
else:
    print("a not found")
if "e" in string:
    print("e found")
else:
    print("e not found")
if "o" in string:
    print("o found")
else:
    print("o not found")

### FIND THE FIRST SUBSTRING
word = str(input("Please type in a word: "))
char = str(input("Please type in a character: "))
# word = "fantastical"
# char = "i"

index = word.find(char)
# print(index)
# substring_end = index + 3
# print(substring_end)

if index >= 0 and (index + 3) <= len(word):
    print(word[index:index + 3])

### FIND ALL THE SUBSTRINGS
word = str(input("Please type in a word: "))
letter = str(input("Please type in a character: "))
#word = "absolutelyimpossible"
#letter = "o"
#print(len(word))
#print(word.find("o"))

index = word.find(letter)

while index + 3 <= len(word) and index != -1 and len(word) > 0:
    offset = index + 1
    print(word[index:index + 3])
    index = word.find(letter, offset)

### THE SECOND OCCURRENCE





##### MORE LOOPS





##### DEFINING FUNCTIONS





##### END OF PART3





##### 






