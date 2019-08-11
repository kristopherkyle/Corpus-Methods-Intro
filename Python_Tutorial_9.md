# Python Tutorial 9: Extracting Dependency Relations, Calculating Strength of Association
[Back to Tutorial Index](py_index.md)

In this tutorial, we will work more with texts that are tokenized, tagged, and dependency parsed by spaCy.

This tutorial presumes:
1. That you have [installed spaCy](https://spacy.io/usage)
2. That you have installed the ["en_core_web_sm" language model](https://spacy.io/usage/models) for spaCy
3. That you have downloaded [this version of the Brown corpus (which includes 500 files)]((https://github.com/kristopherkyle/Corpus-Methods-Intro/blob/master/Course-Materials/brown_single.zip?raw=true), extracted it, and placed it in your working directory (making sure that you see the text files when you open the folder, not a "\_MacOSX" folder and a "brown_single" folder)

### Extracting dependency relations (dependency bigrams) with spacy

While collocation analyses are very useful in corpus linguistics, it is often helpful to see the grammatical relations between particular words (and determine the strenght of association between particular relations).

For example, it may be useful to see all of the collocates of the word "red". However, it may be more useful in many situations to see all of the nouns that tend to be modified by the adjective "red" more specifically. Of course, this all depends on one's research questions.

SpaCy makes it very easy to tag a text for dependency relationships and identify the dependency head (also called a "governor") in each relationship.

```python
import spacy
nlp = spacy.load("en_core_web_sm") #load the English model. This can be changed - just make sure that you download the appropriate model first

sample = "The famous player scored a goal." #sample text

doc = nlp(sample) #tokenize, tag, and parse the sample text

for token in doc: #iterate through processed text
	print(token.lemma_, #print lemma form of word
	token.dep_, #print dependency relationship
	token.head.lemma_) #print the lemma form of the words head (via the dependency relationship)

```

```
>
the det player
famous amod player
player nsubj score
score ROOT score
a det goal
goal dobj score
. punct score
```
If we want to analyze the frequency (or strength of association) of particular pairs of words within a particular dependency relationship (e.g., adjetives and the nouns that they modify), we can do this relatively easily.

The function **_dep_bg_simple()_** below is a simple example of how to create a list of dependency bigrams from a text. The function takes two arguments, namely a text (in the form of a string), and a dependency relationship (in the form of a string).

The function simply determines whether the dependency relationship for each word matches the **_dep_** argument. If so, the dependent and the head are joined with an underscore ("\_") and added to a list. The program returns a list of all matches.

```python
def dep_bg_simple(text,dep): #for teaching purposes
	dep_list = [] #list for dependency bigrams
	doc = nlp(text) #tokenize, tag, and parse text

	for token in doc: #iterate through tokens

		if token.dep_ == dep: #if the dependency relationship matches
			dep = token.lemma_ #extract the lemma of the dependent
			head = token.head.lemma_ #extract the lemma of the head

			dep_bigram = dep + "_" + head #create a dep_head string

			dep_list.append(dep_bigram) #add dep_head string to list

	return(dep_list)
```
**Example usage**
Below, the **__dep_bg_simple()_** function is used to identify all adjective modifier ("amod") relationships in a string.

```python
def dep_bg_simple(text,dep): #for teaching purposes
	dep_list = [] #list for dependency bigrams
	doc = nlp(text) #tokenize, tag, and parse text

	for token in doc: #iterate through tokens

		if token.dep_ == dep: #if the dependency relationship matches
			dependent = token.lemma_ #extract the lemma of the dependent
			head = token.head.lemma_ #extract the lemma of the head

			dep_bigram = dependent + "_" + head #create a dep_head string

			dep_list.append(dep_bigram) #add dep_head string to list

	return(dep_list)
```
```
> ['expensive_car', 'red_car', 'orange_cone']
```

### Calculating Association Strengths (Step 1)

In [Tutorial 6](Python_Tutorial_6), we briefly discussed association strength in terms of pointwise mutual information (MI) and t-score (T). While these are commonly used association strength metrics for collocations, other (perhaps superior, see Gries & Ellis, 2015) metrics are also available such as **_faith_** and **_delta p_**. While MI and T are not directional, **_faith_** and **_delta p_** are (see Gries & Ellis, 2015).

**_Faith_** is simply the probability of an outcome occurring given a particular cue (e.g., the probability of having "car" as an outcome given the word "red"). Faith is directional, meaning that a different value is obtained if we calculate the probability of getting the word "red" given the word "car".

**_delta p_** (or, change in probability) is a variant of Faith that adjusts probability of getting the outcome given a cue by subtracting for the probability of getting the outcome (e.g., car) with any other cue.

In order to calculate association strengths, we need to know the size of the corpus (or in this case, the number of particular dependency relationships we have, e.g., the number of "amod" relationships in a corpus), the frequency of the dependent in the dependency relationship (e.g., the frequency of "red" as an adjective modifier), and the frequency of the head in the dependency relationship (e.g., "car" modified by an adjective).

The function **_dep_bigram_corpus()_** takes a corpus directory/folder as input and returns a dictionary of frequency dictionaries needed to calculate association strengths between dependents and heads of particular dependency relationships. These frequency dictionaries, (which can be accessed with the keys "bi_freq", "dep_freq", and "head_freq") can then be used to calculate association strength using the **_bigram_soa()_** function (which is described in the next section).

The **_dep_bigram_corpus()_** function also outputs a list of all sentences in which matching depedency relationships occur (using the key "samples"). Sentences that include more than one matching dependency relationship are included multiple times (one for each matching relationship). Dependents and heads are marked with the relationship (e.g., "dobj") and whether they are dependents ("dep") or heads ("head"). For example, the sentence _The player kicked the ball_ would be represented as _The player **kicked_dobj_head** the **ball_dobj_dep**._

The **_dep_bigram_corpus()_** function takes nine arguments (but only the first two need to be specified for the program to run with the default settings).
1. **_dirname_** is a string. This should be the name of the folder that your corpus files are in.
2. **_dep_** is a string. This will indicate the dependency relationship to be examined. Common examples include adjective modifier "amod", direct object "dobj" and noun modifier ("nmod"). A complete list of dependency relationships tagged by spaCy can be found [in the spaCy dependency annotation documentation](https://spacy.io/api/annotation#dependency-parsing).
3. **_ending_** is a string that indicates the file ending for your corpus files. By default, this is ".txt".
4. **_lemma_** is a Boolean value. If True, the word form will be a lemma. Otherwise, the word form will be a word. The default value is True.
5. **_lower_** is a Boolean value. Lemmas are lower case by default in spaCY. If lemma = False and lower = True, the word form will be a word in lower case. The default value is lower = True
6. **_dep_upos_** is a string. If specified, the function will only return hits if the universal part of speech tag for the dependent matches what is provided. Common examples include nouns "NOUN", and adverbs "ADV". A complete list of universal part of speech tags used by spaCy can be found in the [spacy part of speech annotation documentation](https://spacy.io/api/annotation#pos-tagging). By default, this is ignored.
7. **_head_upos_** is a string. If specified, the function will only return hits if the universal part of speech tag for the dependent matches what is provided. Common examples include verbs "VERB", and nouns "NOUN". A complete list of universal part of speech tags used by spaCy can be found in the [spacy part of speech annotation documentation](https://spacy.io/api/annotation#pos-tagging). By default, this is ignored.
8. **_dep_text_** is a string. If specified, the function will only return hits if the dependent token matches what is provided. By default, this is ignored.
9. **_head_text_** is a string. If specified, the function will only return hits if the head token matches what is provided. By default, this is ignored.

```python
def dep_bigram_corpus(dirname,dep,ending = ".txt", lemma = True, lower = True, dep_upos = None, head_upos = None, dep_text = None, head_text = None):
	filenames = glob.glob(dirname + "/*" + ending) #gather all text names

	bi_freq = {} #holder for dependency bigram frequency
	dep_freq = {} #holder for depenent frequency
	head_freq = {} #holder for head frequency
	match_sentences = [] #holder for sentences that include matches

	def dicter(item,d): #d is a dictinoary
		if item not in d:
			d[item] = 1
		else:
			d[item] +=1

	file_count  = 1 #this is to give the user updates about the pogram's progress
	total = len(filenames) #this is the total number of files to process

	for filename in filenames: #iterate through corpus filenames
		#user message
		print("Tagging " + str(file_count) + " of " + str(total) + " files.")
		file_count += 1 #add one to the file_count

		text = open(filename, errors = "ignore").read() #open each file
		doc = nlp(text) #tokenize, tag, and parse text using spaCy
		#sent_text = "first"
		for sentence in doc.sents: #iterate through sentences
			#print(sent_text)
			index_start = 0 #for identifying sentence-level indexes later
			sent_text = [] #holder for sentence
			dep_headi = [] #list for storing [dep,head] indexes
			first_token = True #for identifying index of first token

			for token in sentence: #iterate through parsed spaCy document
				if first_token == True:
					index_start = token.i #if this is the first token, set the index start number
					first_token = False #then set first token to False

				sent_text.append(token.text) #for adding word to sentence

				if token.dep_ == dep: #if the token's dependency tag matches the one designated
					dep_tg = token.pos_ #get upos tag for the dependent (only used if dep_upos is specified)
					head_tg = token.head.pos_ #get upos tag for the head (only used if dep_upos is specified)

					if lemma == True: #if lemma is true, use lemma form of dependent and head
						dependent = token.lemma_
						headt = token.head.lemma_

					elif lemma == False: #if lemma is false, use the token form
						if lower == True: #if lower is true, lower it
							dependent = token.text.lower()
							headt = token.head.text.lower()
						else: #if lower is false, don't lower
							dependent = token.text
							headt = token.head.text

					if dep_upos != None and dep_upos != dep_tg: #if dependent tag is specified and upos doesn't match, skip item
						continue

					if head_upos != None and head_upos!= head_tg: #if head tag is specified and upos doesn't match, skip item
						continue

					if dep_text != None and dep_text != dependent: #if dependent text is specified and text doesn't match, skip item
						continue

					if head_text != None and head_text != head: #if head text is specified and text doesn't match, skip item
						continue

					dep_headi.append([token.i-index_start,token.head.i-index_start]) #add sentence-level index numbers for dependent and head

					dep_bigram = dependent + "_" + headt #create dependency bigram

					dicter(dep_bigram,bi_freq) #add values to frequency dictionary
					dicter(dependent,dep_freq) #add values to frequency dictionary
					dicter(headt,head_freq) #add values to frequency dictionary

		### this section is for creating a list of sentences that include our hits ###
		for x in dep_headi: #iterate through hits

			temp_sent = sent_text.copy() #because there may be multiple hits in each sentence (but we only want to display one hit at at time), we make a temporary copy of the sentence that we will modify

			depi = sent_text[x[0]] + "_" + dep+ "_dep" #e.g., word_dobj_dep
			headi = sent_text[x[1]] + "_" + dep+ "_head" #e.g., word_dobj_head

			temp_sent[x[0]] = depi #change dependent word to depi in temporary sentence
			temp_sent[x[1]] = headi ##change head word to headi in temporary sentence

			temp_sent.append(filename) ## add filename to sent to indicate where example originated
			match_sentences.append(temp_sent) #add temporary sentence to match_sentences for output


	bigram_dict = {"bi_freq":bi_freq,"dep_freq":dep_freq,"head_freq": head_freq,"samples":match_sentences} #create a dictioary of dictionaries
	return(bigram_dict) # return dictionary of dictionaries


```
**Usage examples:**
Note that the dependent of the relationship comes first in the bigram, followed by the head (regardless of their position in a sentence).
```python
#extract all "amod" relationships from the documents in the "brown_single" folder
dobj_brown = dep_bigram_corpus("brown_single","amod")

#import high_val function from corpus_tools (see Tutorial 8)
import from corpus_toolkit import high_val
#get the top 20 bigram frequency hits
high_val(dobj_brown["bi_freq"])
```
Most frequent dependent_head pairs with a "dobj" relationshp (i.e., direct objects and their verbs). As we see below, many of these are pronouns (spaCy lemmatizes all pronouns as "-PRON-")
```
-PRON-_tell     365
what_do 247
-PRON-_see      183
-PRON-_take     159
-PRON-_ask      115
-PRON-_do       106
-PRON-_get      93
-PRON-_put      92
-PRON-_keep     84
place_take      84
```
Frequency of dependents (in this case, lemmas that occur in the direct object position):
```python
high_val(dobj_brown["dep_freq"])
```
```
-PRON-  6060
what    835
that    402
which   335
one     274
man     211
time    206
way     192
hand    190
this    189
```
Frequency of heads (in this case, verb lemmas that take direct objects in the corpus):
```python
high_val(dobj_brown["head_freq"])
```
```
have    2806
take    1298
make    1064
give    997
do      932
see     790
get     661
tell    638
use     496
find    488
```
The first five direct object samples in the Brown corpus:

```python
for sample in dobj_brown["samples"][:5]:
	print(" ".join(sample).replace("\n",""))
```
```
These 1750 cases were carted off in a one - night operation by the O'Banion men , who left_dobj_head in their stead the same number_dobj_dep of barrels filled with water .  brown_single/cf_cf20.txt
And another one comes to me and he says , ' Look here , there 's a mill in my state employs five thousand people making_dobj_head uniforms_dobj_dep for the Navy .  brown_single/ck_ck03.txt
This is the first time in 100 years that a candidate for the presidency announced_dobj_head the result_dobj_dep of an election in which he was defeated " , he said .  brown_single/ca_ca37.txt
" Call_dobj_head this_dobj_dep a cry for help " , Faith Constable said .  brown_single/cl_cl14.txt
Barbara Borland of Tigard took_dobj_head top senior individual home economics honors_dobj_dep with a demonstration called filbert hats .  brown_single/ca_ca23.txt
```

### Calculating Association Strengths (Step 2)

Now that we have calculated the required frequencies, we can calculate various strength of association metrics using the **dep_soa()** function.

The **_bigram_soa()_** function takes a dictionary of frequency dictionaries (such as the one created by the **_dep_bigram_corpus()_**) that includes "bi_freq", "dep_freq", and "head_freq" keys and returns a dictionary of {bigram : soa_value} key : value pairs. The **_bigram_soa()_** takes one required argument and two optional arguments.
1. **_freq_dict_** is a dictionary of frequency dictionaries. The dictionaries must be called using the keys "bi_freq", "dep_freq", and "head_freq". _Note that the association between words in non-dependency bigrams can also be calculated as long as the bigrams in the frequency list are separated with an underscore ("\_"). In this case, "dep_freq" and "head_freq" will point to the same word frequency dictionary._
2. **_stat_** is a string that indicates the association strength calculation method. Choices include "MI", "T", "faith_dep", "faith_head", "dp_dep", and "dp_head". By default, this value is set to "MI"
3. **_cutoff_** is an integer that indicates the minimum frequency threshold for the collocation analysis. If the dependency bigram occurs with a frequency below the cutoff, it will be ignored. The default cutoff value is 5.


```python
def bigram_soa(freq_dict,stat = "MI", cutoff=5):
	stat_dict = {}
	n_bigrams = sum(freq_dict["bi_freq"].values()) #get number of head_dependent in corpus for statistical calculations

	for x in freq_dict["bi_freq"]:
		observed = freq_dict["bi_freq"][x] #frequency of dependency bigram
		if observed < cutoff:
			continue

		dep = x.split("_")[0] #split bigram into dependent and head, get dependent
		dep_freq = freq_dict["dep_freq"][dep] #get dependent frequency from dictionary

		head = x.split("_")[1] #split bigram into dependent and head, get head
		head_freq = freq_dict["head_freq"][head] #get head frequency from dictionary

		expected = ((dep_freq * head_freq)/n_bigrams) #expected = (frequency of dependent (as dependent of relationship in entire corpus) * frequency of head (of head of relationship in entire corpus)) / number of relationships in corpus

		#for calculating directional strength of association measures see Gries & Ellis (2015)
		a = observed
		b = head_freq - observed
		c = dep_freq - observed
		d = n_bigrams - (a+b+c)

		if stat == "MI": #pointwise mutual information
			mi_score = math.log2(observed/expected) #log base 2 of observed co-occurence/expected co-occurence
			stat_dict[x] = mi_score #add value to dictionary

		elif stat == "T": #t-score
			t_score = math.log2((observed - expected)/math.sqrt(expected))
			stat_dict[x] = t_score

		elif stat == "faith_dep": #probability of getting the head given the governor (e.g., getting "apple" given "red")
			faith_dep_cue = (a/(a+c))
			stat_dict[x] = faith_dep_cue

		elif stat == "faith_head": #probability of getting the head given the governor (e.g., getting "red" given "apple")
			faith_gov_cue = (a/(a+b))
			stat_dict[x] = faith_gov_cue

		elif stat == "dp_dep": #adjusted probability of getting the head given the governor (e.g., getting "apple" given "red")
			delta_p_dep_cue = (a/(a+c)) - (b/(b+d))
			stat_dict[x] = delta_p_dep_cue

		elif stat == "dp_head": #adjusted probability of getting the head given the governor (e.g., getting "red" given "apple")
			delta_p_gov_cue = (a/(a+b)) - (c/(c+d))
			stat_dict[x] = delta_p_gov_cue

	return(stat_dict)
```
**Usage examples:**

Top 10 most strongly associated direct object - verb combinations (using MI):
```python
#get MI values for all dobj relations in the brown corpus
dobj_brown_mi = bigram_soa(dobj_brown)
high_val(dobj_brown_mi,hits = 10)
```

```
radiation_ionize        12.037952463862721
B_paragraph     12.037952463862721
cigarette_smoke 10.523379291032963
suicide_commit  10.479462174502755
nose_scratch    10.282371191529167
calendar_adjust 9.912421581778862
imagination_capture     9.774918058028927
nose_blow       9.512490974890227
English_speak   9.461760172769297
throat_clear    9.368101065555052
```
Top 10 most strongly associated direct object - verb combinations (using Faith - dependent as cue):
```python
#get MI values for all dobj relations in the brown corpus
dobj_brown_fdep = bigram_soa(dobj_brown,stat = "faith_dep")
high_val(dobj_brown_fdep,hits = 10)
```

```
damn_give       1.0
hereunto_have   1.0
antibody_contain        1.0
incentive_provide       1.0
buffer_start    0.875
chapter_see     0.8461538461538461
suicide_commit  0.8333333333333334
Income_determine        0.8333333333333334
fool_make       0.8333333333333334
mistake_make    0.8
```
The results above indicate, for example, that there is a probability of 1.0 (i.e., a 100% chance) that given "damn" as a direct object, the verb will be "give" (in the Brown corpus).

Top 10 most strongly associated direct object - verb combinations (using Faith - head as cue):

```python
#get MI values for all dobj relations in the brown corpus
dobj_brown_mi = bigram_soa(dobj_brown)
high_val(dobj_brown_mi,hits = 10)
```
```
radiation_ionize        1.0
B_paragraph     1.0
-PRON-_distract 0.8333333333333334
-PRON-_damn     0.7777777777777778
-PRON-_interest 0.7777777777777778
-PRON-_steer    0.7777777777777778
-PRON-_exhaust  0.75
-PRON-_thank    0.717391304347826
-PRON-_frighten 0.7142857142857143
-PRON-_deprive  0.7142857142857143
```
The results above indicate, for example, that there is a probability of 1.0 (i.e., a 100% chance) that given "ionize" as a verb, the direct object will be "radiation" (in the Brown corpus).
