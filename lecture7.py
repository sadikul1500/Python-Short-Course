s1 = 'Hello'
s2 = "World"
s3 = '''This is
a multi-line
string'''

print(type(s1))
print(s1 + " " + s2)
print(s3)

text = "Hello World"
print(len(text))

word = " Python "
print(word.strip())

sentence = "\n Hello World \t" # \n = new line, \t = tab
print(sentence.strip())

#string replacement
greeting = "Hello, World!"
new_greeting = greeting.replace("World", "Python")
print(new_greeting)

#concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

#repetition
laugh = "Ha"
print(laugh * 3)

#access character by index
text = "Hello"
print(text[0]) # Output: H
print(text[1]) # Output: e

#slicing
print(text[1:4]) # Output: ell
print(text[:3]) # Output: Hel
print(text[2:]) # Output: llo

#negative indexing
print(text[-4:-1]) # Output: ell
print(text[-3:-1]) # Output: el

#splitting string
sentence = "Hello World"
words = sentence.split()
print(words) # Output: ['Hello', 'World']

#finding substring
text = "Hello World"
index = text.find("World")
print(index) # Output: 6

if "World" in text:
    print("Found 'World' in the text!")

if "Python" not in text:
    print("Did not find 'Python' in the text!")

if text.startswith("Hello"):
    print("The text starts with 'Hello'")
if text.endswith("World"):
    print("The text ends with 'World'")

if text.find("o") != -1:
    print("Found 'o' in the text!")

#counting occurences
text = "Hello World"
count = text.count("o")
print(count) # Output: 2

#change case
text = "Hello World"
print(text.upper()) # Output: HELLO WORLD
print(text.lower()) # Output: hello world

#title case, swap case 
print(text.title()) # Output: Hello World
print(text.swapcase()) # Output: hELLO wORLD


#Exercise 1: Try Yourself

'''Exercise 2: Given a list of filenames, write a program to print only those filenames that start with "data" and
end with ".csv"'''

print("\nExercise 2")
filenames = ["data1.csv", "data2.csv", "report.docx", "data_analysis.xlsx", "data_summary.csv"]
for filename in filenames:
    if filename.startswith("data") and filename.endswith(".csv"):
        print(filename)

#Exercise 3: Try Yourself

'''Exercise 4: Custom Hashtag Generator
Write a program that takes a sentence from the user and generates a hashtag version of it by:
• Removing leading/trailing spaces,
• Converting all letters to lowercase,
• Replacing spaces between words with underscores _,
• Addinga#atthe beginning'''

print('\n Exercise 4 is important for exam')

sentence = input("Enter a sentence: ")
hashtag = "#" + sentence.strip().lower().replace(" ", "_")
print(hashtag)

'''Exercsise 5: Write a program that asks the user for a password and checks if:
• It starts with a letter (use startswith() with all letters as options),
• Endswith anumber(use endswith() with digits 0-9 as options).
Print appropriate messageslike"Valid start","Valid end",or"Invalid password"depending
on the conditions.'''

print("\nExercise 5")
password = input("Enter a password: ")
if password and password[0].isalpha():
    print("Valid start")
else:
    print("Invalid password")

if password and password[-1].isdigit():
    print("Valid end")
else:
    print("Invalid password")

'''Practice yourself: Create a list of 5 sentences and print the number of words in each sentence'''
