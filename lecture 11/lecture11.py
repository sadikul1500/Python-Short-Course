# file = open('use.txt', 'r')
# print(file.read())

# for line in file:
#     print(line.strip())

# file.close()


# try:
#     file = open('usei.txt', 'r')
#     print(file.read())
# except FileNotFoundError:
#     print('the file des not exist')
# except:
#     print('An unknown error occured')
# print('comon space sentence')

# file = open("output.txt", "w")
# file.write("This is the first line.\n")
# file.write("This is the second line.")
# file.close()

# source_file = open('output.txt', 'r')
# content = source_file.read()
# source_file.close()

# destination_file = open('output_copy.txt', 'w')
# destination_file.write(content)
# destination_file.close()

# file = open("output.txt", "a")
# file.write("\nThis is the append line.")
# file.write("\nThis is another append line.")
# file.close()

# with open('use.txt', 'r') as file:
#     for line in file:
#         print(line.strip())

# import os

# print(os.listdir())

# files = os.listdir('.')
# for file in files:
#     print(file)

# import os

# if os.path.exists("use.txt"):
#     print("The file exists.")
# else:
#     print("File not found.")

# import os
# files = os.listdir()

# txt_files = []

# for file in files:
#     if file.endswith('.txt'):
#         txt_files.append(file)

# print(txt_files)

# Exercise 1
# file = open('use.txt', 'r')
# content = file.read()
# print(len(content.split()))

# Exercise 2
# try:
#     source_file = open('use.txt', 'r')
#     content = source_file.read()
#     destination_file = open('backup.txt', 'w')
#     destination_file.write(content)
# except:
#     print('File not found')

# Exercise 3
# import os

# files = os.listdir('./docuemnts/')
# txt_files = []

# for file in files:
#     if(file.endswith('.txt')):
#         txt_files.append(file)

# for txt_file in txt_files:
#     print(txt_file)


# Exercise 4
# import os

# folder_path = './csv_files/'
# output_file = 'combined.csv'

# csv_files = []

# for file in os.listdir(folder_path):
#     if file.endswith('.csv'):
#         csv_files.append(file)

# with open(output_file, 'w') as outfile:
#     for i in range(len(csv_files)):
#         filename = csv_files[i]
#         file_path = os.path.join(folder_path, filename)

#         content = open(file_path, 'r')
#         if i == 0:
#             outfile.write(content.read())
#         else:
#             next(content)
#             outfile.write(content.read())
#         outfile.write('\n')

# print(f"Successfully merged {len(csv_files)} files into {output_file}")

# Exercise 5
# import os

# txt_files = []

# files = os.listdir('.')
# for file in files:
#     if file.endswith('.txt'):
#         txt_files.append(file)

# total_count = 0
# for txt_file in txt_files:
#     file = open(txt_file, 'r')
#     content = file.read()
#     total_count += content.count('secret')
# print(total_count)
