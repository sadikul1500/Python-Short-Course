#variable name and value assignment
message = "Hello, World!"
print(message)

num = 100
print(num)

a, b, c = 1, 2 ,3
print(a, b, c)

a = b = c = 10
print(a, b, c)

#data types
print(type(message))
print(type(num))

a = 10.6
b = 2.5
print(type(a))

print(a + b)
print(a - b)
print(a * b)
print(a / b)

x = 8
y = 2
print(x / y)
print(type(x / y))

#complex number
c1 = 2 + 3j
c2 = 1 - 4j

print(c1 + c2)
print(c1 * c2)
print(type(c1))

a = True
b = False
print(a)
print(b)
print(type(a))
print(not a)
print(a and b)

print(3 > 2)
print(3 < 2)
print(7 != 10)


print(True + False)
print(True * 5 )

#type casting
num_str = "100"
num_int = int(num_str)
print(num_int)
print(type(num_int))

num_str = "3.14"
num_float = float(num_str)
print(num_float)
print(type(num_float))

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Hello"))
print(bool([]))

#Excercise 1
language = "Python"
number = 2026
print(language, type(language))
print(number, type(number))

#Excercise 2
a = 15
b = 4.2
sum_result = a + b
subtraction_result = a - b
multiplication_result = a * b
division_result = a / b
print(sum_result, type(sum_result))
print(subtraction_result, type(subtraction_result))
print(multiplication_result, type(multiplication_result))
print(division_result, type(division_result))

#Excercise 3
x = True
y = False
print(x and y)
print(x or y)
print(not x)

#Excercise 4
#We will see using input() function in the next lecture
input1 = "100"
input2 = "20.5"
input3 = "False"

num_int = int(input1)
num_float = float(input2)
bool_value = bool(input3)

print(input1, type(input1))
print(input2, type(input2))
print(input3, type(input3))

#Exercise 5
a, b, c = 5, 10.5, "Hello"
x = y = z = 20
print(a, b, c)
print(x, y, z)