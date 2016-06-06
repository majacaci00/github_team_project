##### This script is created to run drafts ####
name = 'Hello module world!'
print name 

## x != y       ## x is not equal to y ​
#x > y        ## x is greater than y ​
#x < y        ## x is less than y  ​
#x >= y       ## x is greater than or equal to y ​
#x <= y       ## x is less than or equal to y  ​
#x is y       ## x is the same as y  ​
#x## Dealing with string variables
print 'The Begining of new chapter'

name = 'Mario Javier Carrillo'
print name

print 'from the book'
index = 0 
while index < len(fruit):
    letter = fruit[index]
    print letter
    index = index + 1
    
len(fruit)  ## command gives me the length, works only on interactive

letter = fruit[0]   ## accessing the 1st character of the word
print letter
se_lett = fruit[6]
print se_lett

lenght = len(fruit)  ## need to define length 1st
#last = fruit[length -1]  #print last word of string 
#print last

# Printing the last word of the string
ot_last = fruit[-1]
print ot_last



len(fruit)  ## command gives me the length, works only on interactive

letter = fruit[0]   ## accessing the 1st character of the word
print letter
se_lett = fruit[6]
print se_lett

lenght = len(fruit)  ## need to define length 1st
#last = fruit[length -1]  #print last word of string 
#print last

# Printing the last word of the string
ot_last = fruit[-1]
print ot_last

# Traversal through string with a loop
index = 0 
while index < len(fruit):
    letter = fruit[index]
    print letter
    index = index + 1
    
    
print 'exercise from the book'
index = -1
while index < len(fruit):
    letter = fruit[index]  # Need to do something with this
    print letter
    index = index - 1


# String slices
s = 'Monty Python'
print s[0:5]
print s[6:13]
print fruit[ :5] # slides starts at the begining
print fruit[6:] 
print s[13:13]
print s[ : ]
print fruit[:] # it means that you need the command will print 
# the entire word

## Strings are immutable CONCATENATION
greeting = 'Hello World'
# greeting[0] = 'J' this command wont work
new_greeting = greeting[0:5] + ' Javier'
print new_greeting

## Looping and counting
word = 'Elena Guadalupe'
count = 0
noncount = 0
for letter in word:
    if letter == 'a':
        count = count + 1
    elif letter == 'L':
        noncount = noncount +1
print count
print noncount is not y   ## x is not the same as y”


## Looping and counting
word = 'Elena Guadalupe'
count = 0
noncount = 0
for letter in word:
    if letter == 'a':
        count = count + 1
    elif letter == 'L':
        noncount = noncount +1
print count
print noncount

# Defining a function ideas from chapter 4
def hello():
    print 'Hello'
    print 'Fun'
hello()
print 'Zip'
hello()


# Exercise 6.3 Defining a Function
def count (word):
    count = 0
    noncount = 0
    for letter in word:
        if letter == 'e':
            count = count + 1
            #return count 
        elif letter == 'l':
            noncount = noncount +1
            #return noncount 
    print 'number of letters e in your word are: ',count
    print 'number of letters l in your word are: ',noncount
#print type (count)

word = raw_input('Enter a word')
count(word)
#print count('e')
#print count ('l')

## 6.7 The in operator
'E' in 'Elena'  # this option works on interactive mode  
## 6.8 String Comparisons 
print 'First Excercise'
word = raw_input('Enter your name: ') 

if word == 'mami':
    print 'words match'
elif word == 'Elena':
    print 'you got it'
print 'Done' 

print 'Second Excercise'
if word < 'Elena':
    print 'Your name, ' + word +', comes before Elena'
elif word > 'Elena':
    print 'Your name, ' + word +', comes after Elena' 
else:
    print 'All rights, Elena.'
    
## In Python all te upper case letters are read before the lower case letter
# 6.9 String Methods
# In Python you can call the function dir, list the methods available in the object
print 'What is going on'
testing = 'Hello World'
type (testing)
dir(testing)
help(str.capitalize)

word = 'samba'
new_word = word.capitalize()

print word + ' ' + new_word


# Exercise 6.3 Defining a Function
print 'The begining'
word = raw_input('Enter your name: ')
#word = 'Javier' # I like the idea of one entering the name or word
print word.find('J',0) # this command is not working the way it supposed to be
print word.count('na', 2, -2)

## Using the methods
# 6.10 Parsing strings
print 'Excersice 6.10'
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
print line
atpos = line.find('@')
print atpos

sppos = line.find(' ',atpos)
print sppos

host = line[atpos+4:sppos]
print host
 





 
    






















