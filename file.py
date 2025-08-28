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

#Task Requirements:
#Create a file called input.txt and write at least five lines of text into it.
#Write a Python script to:
# Read the contents of input.txt.
# Count the number of words in the file.
# Convert all text to uppercase.
# Write the processed text and the word count to a new file called output.txt.
# Print a success message once the new file is created.

#Create and write to input.txt
input_file = open("input.txt", "w")
input_file.write("Hello, my name is James, Bond. JAMES BOND.\n")
input_file.write("I am a secret agent working for MI6.\n")
input_file.write("My mission is to save the world from evil villains.\n")
input_file.write("I have a license to kill and I always ensure I do a thorough job.\n")
input_file.write("In my line of work, discretion is key, and I always stay one ahead of my enemies. They never see me coming\n")
input_file.write("I always have a gadget or two up my sleeve, and I never leave home without my trusty Walther PPK.\n")


#Read from input.txt, process the text, and write to output.txt
input_file = open("input.txt", "r")
content = input_file.read()
print(content)
word_count = len(content.split()) #splits the content into words based on spaces and counts them
print(f"Word Count: {word_count}")  
uppercase_content = content.upper() #converts the content to uppercase
print(uppercase_content)

#Write to output.txt
output_file = open("output.txt", "w")
output_file.write(uppercase_content) #writes the uppercase content to output.txt
output_file.write(f"\nWord Count: {word_count}\n") #writes the word count to output.txt
output_file.close()

#Opening the output file to verify its contents
output_file = open("output.txt", "r")
content_two = output_file.read()  #reads the content of output.txt
print(f"This is the newly created file output.txt: \n{content_two}")
print("output.txt has been created successfully with the processed upper-case text and word count from input.txt.")
