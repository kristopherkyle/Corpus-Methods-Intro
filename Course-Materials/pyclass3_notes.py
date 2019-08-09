# -*- coding: utf-8 -*-
"""
Spyder Editor

This is all of the code run during the third Python class.

"""
import corpus_toolkit as ct #this is corpus_toolkit.py

small_corpus = ct.load_corpus("small_sample")

tokenized = ct.tokenize(small_corpus) #tokenize corpus

lemmatized = ct.lemmatize(tokenized) #lemmatize corpus

#examples with the Brown corpus
brown = ct.load_corpus("Brown_tokenized") #load raw corpus files
brown_token = ct.tokenize(brown) #tokenize Brown corpus
print(brown_token[0][:100]) #print first 100 words in first document

brown_lemma = ct.lemmatize(brown_token) #create lemmatized version
print(brown_lemma[0][:100])#print first 100 lemmas in first document

brown_bigram = ct.ngrammer(brown_token,2) #create bigram version
brown_trigram = ct.ngrammer(brown_token,3) #create trigram version

#Get Frequency Lists
brown_freq = ct.corpus_frequency(brown_lemma) #raw lemma frequency
ct.high_val(brown_freq)

brown_freq_norm = ct.corpus_frequency(brown_lemma,normed = True)
ct.high_val(brown_freq_norm)

brown_range = ct.corpus_frequency(brown_lemma,calc = 'range') #raw range list for Brown corpus
ct.high_val(brown_range) #print top 20 hits

brown_range_norm = ct.corpus_frequency(brown_lemma,calc = 'range',normed = True)
ct.high_val(brown_range_norm)

#write frequency list to a file, only include most frequent 1000 words
ct.high_val(brown_freq_norm,filename = "brown_normed.txt",hits = 1000)

#make bigram list from begining:
#examples with the Brown corpus
brown = ct.load_corpus("Brown_tokenized") #load raw corpus files
brown_token = ct.tokenize(brown) #tokenize Brown corpus
brown_bigram = ct.ngrammer(brown_token,2) #create bigram version
brown_bigram_freq = ct.corpus_frequency(brown_bigram)
ct.high_val(brown_bigram_freq)

import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("The man in the red hat kicked the ball.")
for token in doc:
	print(token.text,token.lemma_,token.tag_,token.pos_,token.dep_)

tagged_list = [] #empty list

for token in doc:
	word = token.lemma_ #lemma form
	tag = token.pos_ #universal part of speech
	combo = word + "_" + tag #combine lemma, "_", and tag
	tagged_list.append(combo) #add to list

print(tagged_list)

### After break, restarted kernal
import corpus_nlp as tg #this is corpus_nlp.py
import corpus_toolkit as ct #this is corpus_toolkit.py

#load, tokenize,lemmatize, tag, and parse entire corpus
sample_tagged = tg.tag_corpus("small_sample") #default lemma and upos

#create frequency list
small_freq = ct.corpus_frequency(sample_tagged)

#print top 20 items in list
ct.high_val(small_freq)

#example with raw words
sample_tagged_raw = tg.tag_corpus("small_sample",lemma = False) #use raw words
small_freq_raw = ct.corpus_frequency(sample_tagged_raw)
ct.high_val(small_freq_raw)

#example with raw words and penn tags
sample_tagged_raw_penn = tg.tag_corpus("small_sample",lemma = False,tp = "penn") #use raw words
small_freq_raw_penn = ct.corpus_frequency(sample_tagged_raw_penn)
ct.high_val(small_freq_raw_penn)

#example with raw words and dependencies
sample_tagged_raw_dep = tg.tag_corpus("small_sample",lemma = False,tp = "dep") #use raw words
small_freq_raw_dep = ct.corpus_frequency(sample_tagged_raw_dep)
ct.high_val(small_freq_raw_dep)

ct.write_corpus("small_sample","small_sample_tagged",sample_tagged_raw) #old directory, new directory, corpus
