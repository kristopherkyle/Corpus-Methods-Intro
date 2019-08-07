# -*- coding: utf-8 -*-
"""
This represents the code used in our python class on Day 5
(the first day of programming in Python)
Please refer to the Python tutorials for more detailed information
"""

print("Hello, World") #we can print strings
print(1.34564) #we can print numbers (integers and floats)
print(1 + 2) # we can add numbers
print("1" + "2") #we can add strings, too, but the result is different!
print("Hello" + " World")
print("Hello" + " " + "World")

blah = "blah blah blah" # we can define variables

print(blah)

blah_list = [1,2,3,"Python","is","awesome"] #we can make lists
print(blah_list)
print(blah_list[0]) #we can find specific items in our lists (or strings)
print(blah_list[3])
print(blah_list[-1])

type(blah) #check what kind of object this is

#turn blah into a list by splitting on spaces
blah_list = blah.split(" ")
print(blah_list)

awesome_list = "Python is awesome".split(" ") #we can create lists from strings
print(awesome_list)

#turn awesome list into string
awesome_string = " ".join(awesome_list) #we can create strings from lists
print(awesome_string)

comma_string = ",".join(awesome_list)
print(comma_string)

#open a file
file1 = open("small_sample/1.txt").read() #we can open files
print(file1)

text1_list = file1.split(" ")
print(text1_list)

for x in text1_list: #iterate through all list items
	if x[0] == "i": #if the first character is "i"
		print(x) #print that string

for x in text1_list: #iterate through all list items
	if x[0] != "i": #if the first character is NOT "i"
		print(x) #print that string

sample_dict = {} #we can create dictionaries
print(sample_dict)
sample_dict["Python"] = "awesome" #and add key - value pairs to dictionaries
print(sample_dict["Python"])
sample_dict["this"] = 2
sample_dict["this"]

for x in text1_list: #iterate through text1_list
	if x in sample_dict: #if the word is a key in the dictionary
		sample_dict[x] +=1 #add one to the count
	else: #if the word is not in the dictionary
		sample_dict[x] = 1 #create a new key value pair (with a frequency of 1)

print(sample_dict)

sample_dict = {}
for x in text1_list: #iterate through text1_list
	if x not in sample_dict: #if the word is not a key in the dictionary
		sample_dict[x] = 1 #make the value 1
	else: #if the word is  in the dictionary
		sample_dict[x] += 1 #add one to the frequency count to the word
print(sample_dict)

v = 0
print(v)
v += 1

### Writing Files
out_string = "This is a cool sentence.\nThis is a second cool sentence."
outf = open("sample_file.txt","w") #create new blank text file
outf.write(out_string)
outf.flush()
outf.close()

### read multiple files
import glob #import the python package "glob"
#create a list will all filenames in a folder that end in .txt
filenames = glob.glob("small_sample/*.txt") 
print(filenames)

freq_dict = {}

for filename in filenames: #iterate through each item in filenames
	print(filename)
	text = open(filename).read().lower()#open file as string (as lower case)
	word_list = text.split(" ") #turn string into list of words called word_list
	for x in word_list:
		if x not in freq_dict: #if the word is not a key in the dictionary
			freq_dict[x] = 1 #make the value 1
		else: #if the word is  in the dictionary
			freq_dict[x] += 1 #add one to the frequency count to the word

print(freq_dict)
