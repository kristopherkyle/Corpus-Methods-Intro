# Python Tutorial 5: Frequency, Range, and File Writing
[Back to Tutorial Index](py_index.md)

In this tutorial, we will build on previous tutorials to create range and frequency lists (and write them to a file).

### Frequency and Range

A basic corpus analysis includes obtaining the frequency for each item in the corpus. In this section, we will look at a function that will calculate raw and normalized frequencies. This function will also be able to calculate range, which is the number of corpus documents a word occurs in.

The **_corpus_frequency()_** function takes four arguments and outputs a dictionary consisting of {word : frequency} pairs.
1. **_corpus_list_** is a tokenized (or lemmatized, or n-grammed) list of list (corpus documents) of lists (word units)
2. **_ignore_** is a list of items to ignore. This will be used to get rid of any last pesky items. By default, this is the **ignore_list**.
3. **_calc_** is a string. For now, the options are 'freq' or 'range'. The default setting is 'freq'.
4. **_normed_** is a Boolean value (True or False). If True, the frequencies will be normed per million words (for frequency) or per 100 documents (for range). The default value is **False**

```python
def corpus_frequency(corpus_list, ignore = ignore_list, calc = 'freq', normed = False): #options for calc are 'freq' or 'range'
	freq_dict = {} #empty dictionary

	for tokenized in corpus_list: #iterate through the tokenized texts
		if calc == 'range': #if range was selected:
			tokenized = list(set(tokenized)) #this creates a list of types (unique words)

		for token in tokenized: #iterate through each word in the texts
			if token in ignore_list: #if token is in ignore list
				continue #move on to next word
			if token not in freq_dict: #if the token isn't already in the dictionary:
				freq_dict[token] = 1 #set the token as the key and the value as 1
			else: #if it is in the dictionary
				freq_dict[token] += 1 #add one to the count

	### Normalization:
	if normed == True and calc == 'freq':
		corp_size = sum(freq_dict.values()) #this sums all of the values in the dictionary
		for x in freq_dict:
			freq_dict[x] = freq_dict[x]/corp_size * 1000000 #norm per million words
	elif normed == True and calc == "range":
		corp_size = len(corpus_list) #number of documents in corpus
		for x in freq_dict:
			freq_dict[x] = freq_dict[x]/corp_size * 100 #create percentage (norm by 100)

	return(freq_dict)
```

Below is an example with the default values (raw frequency):

```python
corp_freq = corpus_frequency(tokenized_corpus)
print(corp_freq["this"])
```
Normed frequency values:

```python
corp_freq_normalized = corpus_frequency(tokenized_corpus,normed = True)
print(corp_freq_normalized["this"])
```

Range values:
```python
corp_range = corpus_frequency(tokenized_corpus,calc = 'range')
print(corp_range["this"])
```
Normed range values:
```python
corp_range_normalized = corpus_frequency(tokenized_corpus,calc = 'range',normed = True)
print(corp_range["this"])
```

### Writing Frequency Values to a File
If we want to output our frequency list to a file for later use, we can do so using the **_list_writer()_** function, which takes five arguments.
1. **_outf_name_** is a string. This will be the name of your output file (e.g., "corpus_results.csv")
2. **_dict_list_** is a list of dictionaries. If you only have one dictionary, just put it inside a list: [freq_dict]
3. **_header_list_** is a list of header names. By default this is ["word","frequency"], but you can adjust it based on the dictionaries you include.
4. **_cutoff_** is an integer or a float. If an item's value is lower than the cutoff value, it will not be included in the output. The default cutoff value is 5.
5. **_sep_** is a string. By default, this is a comma ",". However, if you retain commas in your tokenized lists, you will need to change sep to something else (e.g., "\t").

```python
def list_writer(outf_name,dict_list,header_list = ["word","frequency"],cutoff = 5, sep = ","):
	outf = open(outf_name, "w") #create output file

	outf.write(",".join(header_list) + "\n") #turn header_list into a string, then write the header

	#use the first dictionary in the dict_list for the basis of sorting
	#this will output a list of (word,frequency) tuples
	sorted_list = sorted(dict_list[0].items(),key=operator.itemgetter(1),reverse = True)

	for x in sorted_list: #iterate through (word, frequency) list items
		word = x[0]
		freq = x[1]
		if freq < cutoff: #if the frequency doesn't meet the frequency cutoff
			continue #skip that item
		out_list = [word] #create list for output that includes the word
		for entry in dict_list: #iterate through all dictionaries in the dict_list (there may only be one)
			if word in entry: #make sure entry is in dictionary
				out_list.append(str(entry[word])) #add the value to the list. Note, we convert the value to a string using str()
			else:
				out_list.append("0") #if it isn't in the dictioanary, set it to "0"

		outf.write(sep.join(out_list) + "\n") #write the line to the file
```
Simple usage example (one frequency dictionary)
```python
list_writer("simple_frequency.csv",[corp_freq_normalized])


```

More complicated example (two frequency dictionaries and a range dictionary). This presumes that you have already created the for dictionaries indicated.

```python
list_writer("complicated_frequency.csv",[corp_freq,corp_freq_normalized,rcorp_range,corp_range_normalized],["word","frequency","normed_frequency","range","normed_range"])


```
