a = 10
b = 20

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#examples of a +=, a -=, a *=, a /=, a //=, a %=, a **=
a += 5
print(a)
a -= 3
print(a)
a *= 2
print(a)
a /= 4
print(a)
a //= 2
print(a)
a %= 3
print(a)

#user input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

#foramtted string
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f'Hello {name}, you are {age} years old.')

#print function using sep and end
print("Hello", "World", sep="-", end="!\n")

#Exercise 1: Write a program that takes two numbers as input and performs addition, subtraction, multiplication, and division on them. Print the results in a formatted way.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)


#Exercise 2: check if a number is even or odd
number = int(input("Enter a number: "))
print(f'{number} is even? {number % 2 == 0}')

#Exercise 4: Ask the user to input a word and a number. Print the word repeated that many times. Example: Input: Hello and 3 → Output: HelloHelloHello
word = input("Enter a word: ")
times = int(input("Enter a number: "))
print(word * times)

#try yourself: given total number of days, calculate the total years, months, weeks, and remaining days. Assume 1 year = 365 days, 1 month = 30 days, and 1 week = 7 days.
total_days = int(input("Enter the total number of days: "))
years = total_days // 365
remaining_days = total_days % 365
months = None #try yourself
weeks = None #try yourself
remaining_days = remaining_days % 7
print(f"Years: {years}, Months: {months}, Weeks: {weeks}, Days: {remaining_days}")