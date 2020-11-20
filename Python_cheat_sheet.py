from math import *
# Python cheat sheet
#search up the python functions
# things we know
# ctrl + shift + b = run
# Press f7 to open the command prompt
# Crtl q to end script

# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# CMD PYTHON INTERPRETER
#type in python3 into the CMD
#google how to add python3 to windows path variable
# help("modules") # for checking if you have the module in python

# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# CLASSES AND OBJECT
# __init__ is to initalize a new person
# you can have your student in another file, so you can
# from student import student (importing the class "student")

class student:
    def __init__(self, name, shirt, hat):
        self.name = name
        self.shirt = shirt
        self.hat = hat # So you can call the .hat in this student

        def spawn_yes(self):
            print ("yes!!!")
        # you call have functions in here too

student1 = student("hamantha", "pink","spiffy")
student2 = student("jimbo", "dead weight", "jolly")

Hammboyo = student("Hammboyo", "ugly","ugly") # Use to create new instance of class
print(student2.shirt) # prints the shirt of student 2

class behavior:

    def hungry (self):
        print ("grumble")

    def sleeping (self):
        print ("*is sleeping*")

    def karatin (self):
        print ("sharp!")

class dog(behavior): #dog inherits behavior # make sure you but the parent before the chidld

    def bark (self):
        print ("bork")

    def big_bark (self):
        print ("BORKKK")

    def karatin (self): # this is an override of the original karatin function
        print ("is s o f t")



mydog = dog()

mydog.bark()
mydog.big_bark()
mydog.sleeping()
mydog.karatin() # Override successfull

# Another thing that you can do, that I wont do, is make a multiple choice question quiz
# With the prompt and answer being stored in the class as data so that you could have questions
# Stored in the class with the question prompt and the correct question
# While running the code using a method




# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# MODULES
# When you import a file with, "import file_name", youll be able to call its functions
# ex. import useful_things
# print(useful_things.rolldice())
# this is just very useful compartmentalization
# We have to find the external libraries lib file
# to find the list

# to check: pip --version

# To download: pip install insert_thing
# to uninstall: pip uninstall insert_thing

# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# READ FILE

python_file = open("file.txt", "r")
# r is read
# w is write
# a is add
# r+ read and write
print(python_file.readable()) # Checks if it can actually read it
print(python_file.read()) #spits out the info
print(python_file.readline()) # spits out first line and ques next line
print(python_file.readline()) # spits out the next line
#print(python_file.readlines()[1]) # prints a line, or a range of lines
for line in python_file.readlines():
    print (line)
python_file.close()
# always remember to close your file

python_file = open("file.txt", "a")
python_file.write("\nyay for new things")
python_file.close()

# Writea new file with "w" and .write()

#python_file = open("file1.txt", "w")
#python_file.write("\nyay for new things")
#print (python_file)
#python_file.close()


# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# TRY EXCEPT
# you can nest everything in a try except block to catch errors
# ex. a string in a test funciton

puss= "shit"
boots=12
try:
     uvrays=puss+boots
except ZeroDivisionError:
    print ("you cant divide by zero")
except ValueError:
    print ("invalid input")
except:
    print ("wtf?")


# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# FOR

dogs = ["jim", "lacy", "karen"]
for dog in dogs:
    print(dog)

for letter in "green":
    print(letter)

cats = ["adaw", "vdc", "ajwdn", "sdfghj"]
for whatyoucall in cats: # The variable after "for" can be whatever you want.
    print(whatyoucall)
for indexnumber in range(len(cats)): # syn w/ range(3)
    if indexnumber == 0:
        print("first!")
    else: print ("not first... :(")
    print (cats[indexnumber])

for indexnumber in range(0,1): # syn w/ range(3)
    print (cats[indexnumber])

for numberthing in range(2, 10):
    print (numberthing)

# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# WHILE

while_var = 7
while while_var != 0:
    print("oh no #" + str(while_var))
    while_var-=1 # add one to x
    print ("done for a while")
print ("yay, ya done!")

# you can do a guess int game by using the "user input correct?" "guess= input("Enter guess:")"
#to limit that, you can make a guess count var, and guess limit var, and out of guesses var


# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# DICTIONARY

#they bump one thing into a bigger thing

dictionary_love = {"jan": "january","mar": "march","n":"new" }
# if key not valid; "none"
print (dictionary_love["mar"])
print (dictionary_love.get("mar")) # they do the same thing
print (dictionary_love.get("puss", "not a valid key")) # If not valid, itll return the second statement
# supposedly used for storing banks of data

# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# IF

is_green = True # Booleans have to be capitalized
is_thick = True
is_12 = 12
is_13 = 13

if is_green or is_fat:
    print("green and or fat")
elif not(is_green) and not(is_fat):
    print("not green, not hat")
elif is_12 >= is_13 or is_13 >= is_12:
    print("impossible!")
else: print("IDK dude. error.")
# if: and, or, not(), =, =>, !=
# elif is just another "if" on top


# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# FUNCTIONS

def say_hi(insert_one, insert_two, insert_three):
    # all code in this indent is a part= of the functions
    print(insert_one+" "+insert_two+ " orange "+str(insert_three))
say_hi("yes", "twelve", 3) # calls function
say_hi("no", "eleven", 7) # calls function

# if you call something and then print it and it returns "none", you need to use a return/

def cubed(num):
    return num*num*num
print (cubed(3))

def power_to(base, power):
    result = 1
    for number in range(power):
        result = result*base
    return result

print ("raised to power " + str(power_to(3,4)) + "!")
# this is some clever code that reads the power and multiplies it by how many times

def letter_replacer(phrase):
    replacement = ""
    for letter in phrase:
        if letter.lower() in "green":
            if replacement.isupper():
                replacement = replacement + "*"
            else: replacement = replacement + "^"
        else: replacement = replacement + letter
    return replacement
# im assuming that itll run through each letter,
# check if its a letter in green, and replace it in the replace value, to print at the end

# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# LISTS

list_two = ["green", "yellow", "black", "seven", "yellow"]
list_one = ["jim", "john", 2, 58, "are"]
print (list_one) # prints whole list
print (list_two)
print (list_one[2]) # Prints list indexed
list_yay = list_two.copy()
print("\n")

# you can put a billion things in a list

print(list_one.extend(list_two)) # puts list two on the end of list one
print(list_two.append("brown")) # adds brown onto the end # you can add a whole buncha shit to lists with append
print(list_two.insert(1, "aubergine")) # places aubergine and pushes everything else bacl
print(list_one.pop()) # pops off the end
print("\n")

print(list_two.index("yellow")) # where yellow is indexed
print(list_two.count("yellow")) # how many yellows are there
print (list_one.reverse()) # none?
print (list_two.sort()) # none?
print("\n")


print(list_two.remove("green")) # none? (removes part of list)
print(list_one.clear()) # none? empties list
print("\n")


# TUPLE

coordinates = (2, 5)
# Theyre just lists you dont and cant change
Coordinated = [(2,5),(3,7),(3,7,8)] # a list of tupples
green = [[2,3,7],[2,6,9]]

# GRID LISTS
# if you put lists in lists, you can access them like a battleship grid

grid = [
    ["a",'b','c','d','e','f'],
    ['g','h','j','k','l','m'],
    ['n','o','p','q','r','s'],
    ['t','u','v','w','x','y'],
    ['z']
    ]
print (grid[2][1]) # Prints "o" in column 2, index 1

# NESTED LOOPS FOR GRIDS

for row in grid:
    print (row)
    for letter in row:
         print(letter)
# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# USER FUNCTIONS

#name = input("enter your name: ")
#print ("Hey whats up " + name + "!")
# if youre doing things with the input, covert it to int() or float()
# because it starts as string

# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# NUMBER FUNCTIONS

number_one = (10 % 3) # prints the pemainder of 10/3, which is 1
print (str(number_one)) # converts string to number for concatenation
print (abs(-2 + number_one)) # abs is absolute vsalue
print (pow(2,5)) # 2^5
print (round(2.7)) # to 3

print (max(3,4)) # picks 4
print (min(3,4)) # picks 3

    # Math imports
print ("floor: " + str(floor(2.9))) # chops down to 2
print ("ceil: " + str(ceil(2.9))) # 3
print ("sqrt: " + str(sqrt(2))) # root 2




# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# STRING FUNCTIONS

green = "giraffe academy"
print (green.replace("giraffe", "orange"))

phrase = "hello \n \"world\"" # n/ is "new line")
print (phrase)

phrase_one = "Green is the best"
print ("replace: " + phrase_one.replace("Green", "yellow")) # replaces green with yellow
print (phrase_one.index("the")) # finds the index of the string
print (phrase_one.upper().isupper()) # makes capital and asks if its true
print (phrase_one.islower()) # checks lowercase
print ("length" + str(len(phrase_one))) # prints the lenth of phrase one
print ("0 index: " + phrase_one[0]) # prints the letter of the index
# to prit numbers by strings, you need to convert these vslues to strings str()

# \\
#  \\
#   \\
#   //
#  //
# //
# \\
#  \\
#   \\
#   //
#  //
# //
# JENNA NOTES

teeth = 19
melons = 27
bannanas = "fear Batman"

# you can use commas to put variables in spaces
print (teeth,"teeth",teeth,"teeth")

# Use {} and .format() to replace each {} with a format fill
print ("Oranges {}, {}, and {}, are turning the friggin frogs gay!!!".format(teeth, melons, bannanas, "yes"))

# use f to place these values inside the brackets
print (f"god is imaginary ({melons}), and god is {teeth}. {bannanas}")
