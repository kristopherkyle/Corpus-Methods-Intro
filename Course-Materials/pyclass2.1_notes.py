#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 10:35:41 2019
Code run in the second Python class (this mostly came from the tutorial I wrote)
@author: kkyle2
"""

import glob

def load_corpus(dir_name, ending = '.txt', lower = True): #this function takes a directory/folder name as an argument, and returns a list of strings (each string is a document)
	master_corpus = [] #empty list for storing the corpus documents
	filenames = glob.glob(dir_name + "/*" + ending) #make a list of all ".txt" files in the directory
	for filename in filenames: #iterate through the list of filenames
		if lower == True:
			master_corpus.append(open(filename).read().lower()) #open each file, lower it and add strings to list
		else:
			master_corpus.append(open(filename).read())#open each file, (but don't lower it) and add strings to list

	return(master_corpus) #output list of strings (i.e., the corpus)

corpus_lower = load_corpus("small_sample") #load the corpus into memory with the default settings
print(corpus_lower[0]) #print the first document in the corpus

corpus_sample = load_corpus("small_sample", lower = False) #load the corpus into memory with the default settings
print(corpus_sample[0]) #print the first document in the corpus

text1 = "This is a silly string."
text2 = text1.replace("silly","sample")
clean_text = text2.replace(".","")

default_punct_list = [",",".","?","'",'"',"!",":",";","(",")","[","]","''","``","--"] #we can add more items to this if needed
default_space_list = ["\n","\t","  ","   ","   "]

def tokenize(corpus_list, remove_list = default_punct_list, space_list = default_space_list, split_token = " "):
	master_corpus = [] #holder list for entire corpus

	for text in corpus_list: #iterate through each string in the corpus_list
		for item in remove_list:
			text = text.replace(item,"") #replace each item in list with "" (i.e., nothing)
		for item in space_list:
			text = text.replace(item," ")

		#then we will tokenize the document and add it to the corpus
		tokenized = text.split(split_token) #split string into list using the split token (by default this is a space " ")

		master_corpus.append(tokenized) #add tokenized text to the master_corpus list

	return(master_corpus)

corpus_lower = load_corpus("small_sample") #load the corpus into memory with the default settings
tokenized = tokenize(corpus_lower) #tokenize the corpus documents

print(corpus_lower[0])
print(tokenized[0])

tokenized2 = tokenize(load_corpus("small_sample"))
print(tokenized2[0])

def load_lemma(lemma_file): #this is how we load a lemma_list
	lemma_dict = {} #empty dictionary for {token : lemma} key : value pairs
	lemma_list = open(lemma_file).read() #open lemma_list
	lemma_list = lemma_list.replace("\t->","") #replace marker, if it exists
	lemma_list = lemma_list.split("\n") #split on newline characters
	for line in lemma_list: #iterate through each line
		tokens = line.split("\t") #split each line into tokens
		if len(tokens) <= 2: #if there are only two items in the token list, skip the item (this fixed some problems with the antconc list)
			continue
		lemma = tokens[0] #the lemma is the first item on the list
		for token in tokens[1:]: #iterate through every token, starting with the second one
			if token in lemma_dict:#if the token has already been assigned a lemma - this solved some problems in the antconc list
				continue
			else: 
				lemma_dict[token] = lemma #make the key the word, and the lemma the value
	
	return(lemma_dict)

lemma_dict = load_lemma("antbnc_lemmas_ver_003.txt")

def lemmatize(tokenized_corpus,lemma): #takes a list of lists (a tokenized corpus) and a lemma dictionary as arguments
	master_corpus = [] #holder for lemma corpus
	for text in tokenized_corpus: #iterate through corpus documents
		lemma_text = [] #holder for lemma text

		for word in text: #iterate through words in text
			if word in lemma: #if word is in lemma dictionary
				lemma_text.append(lemma[word]) #add the lemma for to lemma_text
			else:
				lemma_text.append(word) #otherwise, add the raw word to the lemma_text

		master_corpus.append(lemma_text) #add lemma version of the text to the master corpus

	return(master_corpus) #return lemmatized corpus

lemmatized = lemmatize(tokenized,lemma_dict)
print(lemmatized[0])
