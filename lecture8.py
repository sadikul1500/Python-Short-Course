def greet():
    print("Hello, welcome to the lecture!")

greet()

#the add function is static, it always adds the same two numbers. We can make it more flexible by allowing it to take parameters.
def add():
    num1 = 10
    num2 = 12
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is: {sum}")
          
add()

def greet(name):
    print(f"Hello, {name}! Welcome to the lecture!")

greet("Alice")
greet("Bob")

def square(x):
    return x * x

#This add function takes two parameters and returns their sum. We can call it with different numbers to get different results.
def add(num1,  num2):
    print('add 1')
    return num1 + num2

def add(num1=10, num2=15, num3 = 20):
    print('add 2')
    return num1 + num2 + num3

add(12, 23, 30)

#return multiple values
def get_coordinates():
    x = 10
    y = 20
    return x, y

coords = get_coordinates()
print(coords)

print(coords[0])
print(coords[1])

def get_person_info():
    return {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
info = get_person_info()
print(info["name"]) # Output: Alice
print(info["age"])
print(info["city"])

#using dictionary as a parameter of function
def print_person_info(person):
    print(f'Name: {person["name"]}')
    print(f'Age: {person["age"]}')
    print(f'City: {person["city"]}')

print_person_info({
    "name": "Alice",
    "age": 30,
    "city": "New York"
})

def describe_pet(name, animal):
    print(f"I have a {animal} named {name}.")

describe_pet(animal="dog", name="Buddy")

#variable length arguments
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4, 5)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

#document string``
def sumofFourNumbers(a, b, c, d):
    """This function takes four numbers as input and returns their sum."""
    return a + b + c + d

help(sumofFourNumbers)


#Exercise 1: Do it yourself
#Exercise 2: Do it yourself

#Exercise3: write a function for calculating factorial of a number. factorial 5 = 1 * 2 * 3 * 4 * 5 = 120

def factorial(n):
    print('\nExercise 3\n')
    mult = 1
    for i in range(1, n+1):
        mult *= i
    return mult

print(f'factorial(6) = {factorial(6)}')

#Exercise 4: Palindrome check function
def palindrome_check(s):
    print('\nExercise 4\n')
    return s[::-1]

print("\nPalindrome Check Examples:")
print(f"'racecar' is palindrome: {palindrome_check('racecar')}")  # True
print(f"'hello' is palindrome: {palindrome_check('hello')}")      # False
print(f"'madam' is palindrome: {palindrome_check('madam')}")    #True

#Exercise 5: FizzBuzz function
def fizz_buzz(n):
    """
    Print numbers from 1 to n with the following rules:
    - Multiples of 3: print "Fizz"
    - Multiples of 5: print "Buzz"
    - Multiples of both 3 and 5: print "FizzBuzz"
    - Otherwise: print the number
    """
    print('\nExercise 5: FizzBuzz\n')
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    
    print(", ".join(result))

fizz_buzz(15)

