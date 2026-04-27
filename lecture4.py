number_sequence = range(6)
print(number_sequence)
print(type(number_sequence))

print('Starts from zero and ends at 5 (6 is not included)')
for i in range(5):
    print(f"Current number: {i}")

print('Starts from 1 and ends at 5 (6 is not included)')
for number in range(1, 8):
    print(f"Number: {number}")

print('Starts from 1, ends at 20, with a step of 3')
for number in range(1, 20, 3):
    print(f"Number: {number}")

print("Even numbers:")
for even in range(2, 11, 2):
    print(f"Even number: {even}")


total_sum = 0
print("Adding numbers 1 to 10:")

for num in range(1, 11):
    total_sum = total_sum + num
    print(f"Adding {num}, running total: {total_sum}")

print(f"Final sum: {total_sum}")


#use of break statement
print("Finding the first number divisible by 7 between 22 and 40:")
for num in range(22, 41):
    if num % 7 == 0:
        print(f"The first number divisible by 7 is: {num}")
        break

print("Loop finished")

#use of continue statement
print("Printing odd numbers between 1 and 10:")
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(f"Odd number: {num}")

#nested loops
print("Multiplication table for numbers 1 to 3:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Print a new line after each row of the multiplication table


#drawing pattern- triangle
print("\nDrawing a triangle pattern:\n")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()  # Print a new line after each row of the triangle

#exercise 1: Sum of even number from 1 to 100
print('\nExercise 1\n')
even_sum = 0
for num in range(1, 101):
    if num % 2 == 0:
        even_sum += num

print(f"The sum of even numbers from 1 to 100 is: {even_sum}")

#Exercise 2: Take a number as input and print its multiplication table from 1 to 10
print('\nExercise 2\n')
number = int(input("Enter a number to see its multiplication table: "))
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print('end')


#Exercise 3: Pattern printing- number triangle
print('\nExercise 3\n')
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()  # Print a new line after each row of the number triangle


#Exercise 4: Letter staircase pattern
print('\nExercise 4\n')
for i in range(1, 6):
    for j in range(65, 65 + i):
        print(chr(j), end="")
    print()  # Print a new line after each row of the letter staircase pattern


#Exercise 5: Sum of Digits of a Number
print('\nExercise 5\n')
number = int(input("Enter a number to find the sum of its digits: "))
digit_sum = 0
for digit in str(number):
    digit_sum += int(digit)
print(f"The sum of the digits of {number} is: {digit_sum}")

print('\n---- End of Lecture 4 ----')