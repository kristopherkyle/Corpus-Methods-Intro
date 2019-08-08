#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 09:30:00 2019
Code run at the beginning of the second Python class
@author: kkyle2
"""

translation = {}

translation["word"] = "daneo"
print(translation["word"])

translation["restaurant"] = "sikdang"
print(translation)

translation["boat"] = "bae"
translation["pear"] = "bae"

print(translation)

translation["boat"] = "seonbak"
print(translation)

favorite = {}
favorite["Kris"] = "The Matrix"
print(favorite)
print(favorite["Kris"])

nl1 = [1,2,3,4,5,6,7,8,9,10]

def add_number(num_list,number):
	out_list = []
	
	for x in num_list:
		out_list.append(x + number)
	
	return(out_list)

nl2 = add_number(nl1,3)	
print(nl2)

verbs = "walk talk work change dance like play".split(" ")

def inflector(word_list,suffix):
	out_list = []
	
	#iterate through word list
	for x in word_list:
		#add suffix to each word and add it to word list
		out_list.append(x + suffix)
	
	#return inflected list
	return(out_list)

past = inflector(verbs,"ed")
prog = inflector(verbs,"ing")

print(past)

def past(verb_list):
	out_list = []
	
	for x in verb_list:
		#if the last letter is "e":
		if x[-1] == "e":
			#add "d"
			out_list.append(x + "d")
		#else add "ed"
		else:
			out_list.append(x + "ed")
	
	return(out_list)

past2 = past(verbs)
print(past2)