count = 1

while count <= 5:
    print(f"Count is: {count}")
    count = count + 1

print(f"Final count: {count}")

#countdown timer from 10 to 1
import time
number = 10
print("Countdown:")

while number > 0:
    print(f"{number}")
    time.sleep(1)
    number = number - 1

print("Blast off!")

#sum using while loop
total = 0
number = 1
print("Enter numbers to add (enter 0 to stop):")
while True:
    number = int(input("Enter a number: "))
    if number != 0:
        total = total + number
        print(f"Running total: {total}")
    else:
        break
print(f"Final sum: {total}")

#input validation using while loop
number =-1 # Initialize with invalid value
while number <= 0:
    number = int(input("Enter a positive number: "))
    if number <= 0:
        print("Error: Number must be positive!")

print(f"Thank you! You entered: {number}")


#using while loop with break and continue statements
count = 0
while count < 10:
    count = count + 1 #this is important to avoid infinite loop. When you use continue statement, you have to increment/decrement the counter before continue statement, otherwise it will cause infinite loop.
    if count % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {count}")

num = 1
while num <= 10:
    square = num * num
    print(f"The square of {num} is {square}")
    if square > 50:
        print("Square is greater than 50, stopping the loop.")
        break
    num = num + 1


#simple password checker
correct_password = "python123"
user_password = ""

while user_password != correct_password: # Continue until passwords match
    user_password = input("Enter the password: ")
    
    if user_password != correct_password:
        print("Wrong password! Try again.")

print("Access granted!")

#Exercise 1: Do it yourself
#Exercise 2: Do it yourself

#Exercise 3: Keep asking the user for positive numbers and add them to a total. Stop when they enter-1 and display the final sum
print('\nExercise 3\n')
total_sum = 0
while True:
    number = int(input("Enter a positive number (or -1 to stop): "))
    
    if number == -1:
        break  # Exit the loop if the user enters -1
    elif number > 0:
        total_sum += number  # Add the positive number to the total
    else:
        print("Please enter a positive number or -1 to stop.")
print(f"Final sum: {total_sum}")

#Exercise 4: Pick a secret number (like 7). Keep asking the user to guess until they get it right. Tell them ”Too high” or ”Too low” for wrong guesses
print('\nExercise 4\n')

secret_number = 7

while True:
    guess = int(input("Guess the secret number (1-10): "))
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Correct! You guessed the secret number.")
        break

#Exercise 4.1: Make the game more interesting by taking the secret number a random number between 1 to 30
print('\nExercise 4.1\n')
import random
secret_number = random.randint(1, 30)
while True:
    guess = int(input("Guess the secret number (1-30): "))
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Correct! You guessed the secret number.")
        break


#Exercise 5: Ask the user to solve multiplication problems (like 3 × 4). Keep giving new problems until they get one wrong. Count how many they got right.
print('\nExercise 5\n')
import random
correct_count = 0
while True:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 * num2
    
    user_answer = int(input(f"What is {num1} x {num2}? "))
    
    if user_answer == correct_answer:
        print("Correct!")
        correct_count += 1
    else:
        print(f"Wrong! The correct answer was {correct_answer}.")
        break

print(f"You got {correct_count} correct!")

'''Exercise 6: Power Calculator
Askfor a base number. Use awhileloop tocalculate and print its powers (base¹, base², base³, etc.)
until the result exceeds 1000.'''
print('\nExercise 6\n')
base = int(input("Enter a base number: "))
exponent = 1
while True:
    result = base ** exponent
    if result > 1000:
        break
    print(f"{base}^{exponent} = {result}")
    exponent += 1