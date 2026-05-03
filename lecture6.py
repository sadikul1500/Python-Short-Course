fruits = ["apple", "banana", "cherry"]

print(fruits[0]) # Output: apple (first item)
print(fruits[1]) # Output: banana (second item)
print(fruits[2]) # Output: cherry (third item)

print(fruits[-1])

print(fruits[4])


fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange" # Change banana to orange
print(fruits) # Output: ['apple', 'orange', 'cherry']
fruits.append("mango")
fruits.insert(1, "grape") # Insert grape at index 1
print(fruits)

fruits.remove("apple") # Remove 'apple' by value, so list becomes ['grape', 'orange', 'cherry', 'mango']
del fruits[0] # Remove item at index 0.. so the first item gets removed (grape)
print(fruits)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

numbers = [2, 12, 4, 7, 2, 9, 5, 35, 3]

print(len(numbers))
# Output: 5 (number of elements)
print(max(numbers))
# Output: 9 (largest value)
print(min(numbers))
# Output: 2 (smallest value)
print(sum(numbers))


numbers = [4, 7, 2, 9, 5]

# Slice from index 1 to 3 (4 is excluded)
sublist = numbers[1:4]
print(sublist)

sublist = numbers[:3]
print(sublist)

sublist = numbers[2:]
print(sublist)

#negative indexing
sublist = numbers[-4:-1]
print(sublist)


#Tuples are immutable, meaning they cannot be changed after they are created. They are defined using parentheses () instead of square brackets [].
info = ("Alice", 25, "Engineer")
print(info[0])
# Output: Alice
print(len(info))

for item in info:
    print(item)

#tuple pcking & unpacking
# Packing
person = ("Bob", 30, "Doctor")

# Unpacking
name, age, job = person
print(name) # Output: Bob
print(age)
print(job)

#creating & accessing dictionaries
person = {
    "name": "Charlie",
    "age": 28,
    "job": "Designer"
}
print(person["name"]) # Output: Charlie
print(person["age"]) # Output: 28
print(person["job"]) # Output: Designer
print(person.get("name")) # Output: Charlie

#modifying dictionaries
person["age"] = 29
print(person["age"]) # Output: 29

#add new key-value pair
person["city"] = "Rome"
print(person)

for key, value in person.items():
    print(f"{key} => {value}")


print(person.keys())
print(person.values())

'''Class Taksk:  Create a dictionary for a book with keys: title, author, and year. Add a new key publisher
and print each key-value pair using a loop'''
book = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}

book["publisher"] = "Scribner"
for key, value in book.items():
    print(f"{key} => {value}")


#Exercise 1, 2: Do by yourself

'''Exercise 3: Create a dictionary for a student with keys: name, id, and marks. Add a key called result and set
its value to "Pass" if marks ≥ 40, else "Fail"'''

student = {
    "name": "Alice",
    "id": 12345,
    "marks": 45
}

if student["marks"] >= 40:
    student["result"] = "Pass"
else:
    student["result"] = "Fail"

for key, value in student.items():
    print(f"{key} => {value}")

#Exercise 4: Create a list of 7 numbers and print the last 3 using slicing
numbers = [10, 20, 30, 40, 50, 60, 70]
last_three = numbers[-3:]
print(last_three) # Output: [50, 60, 70]


#Exercise 5 is very important, try to do it by yourself first, then check the solution below
'''Exercise 5: Create a dictionary with two students. Each student should be another dictionary with name, id,
and department. Print all information using loops'''
students = {
    "student1": {
        "name": "Alice",
        "id": 12345,
        "department": "Computer Science"
    },
    "student2": {
        "name": "Bob",
        "id": 67890,
        "department": "Mathematics"
    }
}

for student_key, student_info in students.items():
    print(f"{student_key}:")
    for key, value in student_info.items():
        print(f"  {key} => {value}")

'''Practice to test youself: Create a list of 5 dictionaries, each representing a book with 
keys: title, author, and year. Print the title of each book using a loop.'''