#Write a Python program to create a PDF file containing a list of names.
file = open("names.pdf", "w")
file.write("James, " "John, " "Paul, " "George, " "Ringo\n")

#append names to the file
file = open("names.pdf", "a")
file.write("Yoko, " "Linda, " "Cynthia\n")    
file.write("These are some power couples: " "John and Yoko, " "Paul and Linda, " "George and Cynthia\n")
file.write("These are some solo artists: " "John, " "Paul, " "George, " "Ringo, " "Yoko, " "Linda, " "Cynthia\n")

#Read a single line from the file
file = open("names.pdf", "r")
line = file.readline()
print(line)

#Read all lines from the file - shows as an array
file = open("names.pdf", "r")
lines = file.readlines()
print(lines)

#Read a specific line from the file
file = open("names.pdf", "r")
lines = file.readlines()
print(lines[2]) #prints the third line

#Read the entire file
file = open("names.pdf", "r")
content = file.read()
print(content)

#ERROR HANDLING - try and except blocks if the file does not exist
try:
    file = open("non_existent_file.pdf", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file does not exist please check file name/path and try again")

#Read an image file
file = open("restaurant10.jpg", "rb")
content = file.read()
print(content[:100]) #prints the first 100 bytes of the image file
file.close()

