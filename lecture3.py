temperature = 30

if temperature > 25:
    print("It's a warm day!")
    print("Perfect weather for swimming.")


score = 85

if score >= 80:
    print("Excellent work!")
    print("You passed with distinction.") 
print("This line always executes regardless of the score.")


age = 16

if age >= 18:
    print("You are eligible to vote.")
    print("Please register if you haven't already.")
else:
    print("You are not yet eligible to vote.")
    print(f"You can vote in {18 - age} years.")

temperature = 15

if temperature > 30:
    print("It's hot outside!")
    print("Stay hydrated and seek shade.")
elif temperature > 20:
    print("It's warm and pleasant.")
    print("Great weather for outdoor activities.")
elif temperature > 10:
    print("It's cool but comfortable.")
    print("You might want a light jacket.")
else:
    print("It's cold outside!")
    print("Bundle up and stay warm.")

#OR Operator
a = 12
if a % 5 == 0 or a % 3 == 0:
    print('a either a multiple of 3 or 5')
else:
    print('a is not a multple of 3 or 5')

#Combining multiple logical operators: and, or and not
a = 12
if (a % 5 == 0 or a % 3 == 0) and a > 10:
    print('a is either a multiple of 3 or 5 and greater than 10')
else:
    print('a does not satisfy the condition')

#nested conditional statements
age = 25
if age >= 18:
    if age < 21:
        print("You can vote but cannot drink alcohol.")
    else:
        print("You can vote and drink alcohol.")
else:
    print("You are not yet eligible to vote or drink alcohol.")


#Exercise 1: Do by Yourself

#Exercise 2: Take a number from the user and determine whether it’s positive, negative, or zero.
print('Exercise 2')
number = float(input("Enter a number to determine positive, negative or zero: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#Exercise 3: Take three numbers as input and print the largest one using if-elif-else
print('Exercise 3')
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is: {num2}")
else:
    print(f"The largest number is: {num3}")

#Exercise 4: Do by Yourself

'''Exercise 5: Take a year as input and determine whether it’s a leap year or not. A leap year is divisible by 4, but not by 100 unless it’s also divisible by 400.'''
print('Exercise 5')
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")