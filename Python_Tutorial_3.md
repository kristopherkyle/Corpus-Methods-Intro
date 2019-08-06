
# Welcome to 680R, Day 5

### More fun with Python:  
### Dictionaries, Tuples, Functions, and Files

# Part I: Dictionaries

### Dictionaries are storage and retrievel objects (like lists)
### Lists are organized via sequential order:


```python
sample = ["this", "is", "a", "sample", "list"]
sample[2]
```




    'a'



### Dictionaries are unordered, and are organized via "key" and "value" pairs
### Dictionary traversal (i.e., "for" loops on dictionaries) is faster than list traversal


```python
sample_d = {"Windows": "Not Awesome","Mac" : "Awesome","Linux": "We are not worthy"}
sample_d["Windows"]
```




    'Not Awesome'




```python
for x in sample_d:
    print(x) #prints keys
```

    Windows
    Mac
    Linux



```python
for x in sample_d:
    print(sample_d[x])
```

    Not Awesome
    Awesome
    We are not worthy


### Adding items to dictionaries:


```python
sample_d["Nintendo"] = "Super Cool"
print(sample_d)
```

    {'Windows': 'Not Awesome', 'Mac': 'Awesome', 'Linux': 'We are not worthy', 'Nintendo': 'Super Cool'}


# Uses for dictionaries

### I most often use dictionaries for storing word/value (e.g., frequency values, lemma form, POS, etc.) pairs.
### Note that dictionary values can be strings, integers, floats, lists, tuples, or other dictionaries!



# Part II: Tuples
### Tuples are storage and retrieval objects (like lists)
### The main difference between tuples and lists is that tuples are immutable
### This means that while you can ADD items (but only using "+", and only tuples) to tuples, you can't CHANGE a tuple item


```python
sample_t = (1,2)
sample_t = sample_t + (3,4)
sample_t
```




    (1, 2, 3, 4)




```python
sample_l = [1,2,3,4]
sample_l[1] = "two"
print(sample_l)
```

    [1, 'two', 3, 4]



```python
print(sample_t[1])
```

    2



```python
sample_t[1] = "two"
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-40-ec2ffd9bc0a6> in <module>()
    ----> 1 sample_t[1] = "two"


    TypeError: 'tuple' object does not support item assignment


# Part III: Functions
### An important mantra in programming is "Don't Repeat Yourself", or DRY

### The opposite of this is often called "WET" ("write everything twice", "we enjoy typing" or "waste everyone's time")

### Functions allow us to follow the DRY principle

### Functions also helps with debugging because errors will occur in the function instead of in multiple places in your code

### I did NOT learn functions early in my programming career... which led to really long scripts and time-consuming debugging

# Writing functions:
### We will start with a real example from one of my programs
### I often calculate the average frequency score for words in a text.
### But, I only count words that are represented in my frequency database
### So, average frequency = sum of frequency scores/number of words in text that are in frequency database
### Some times, in short texts, NONE of the words in the text are in my frequency database


```python
#normal situation:
freq_counter = 235648
n_words = 52

av_freq = freq_counter/n_words
print(av_freq)
```

    4531.692307692308



```python
#rare situation:
freq_counter2 = 0 #no words in database, so no summed frequency
n_words2 = 0 #no words in database

av_freq2 = freq_counter2/n_words2
print(av_freq)
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-29-a5d0f2e0e9fe> in <module>()
          3 n_words2 = 0 #no words in database
          4
    ----> 5 av_freq2 = freq_counter2/n_words2
          6 print(av_freq)


    ZeroDivisionError: division by zero


# To get around this issue, I write a function called "safe_divide"
### The syntax is as follows:
#### def function_name(arguments):
#### followed by the script of your function
#### Note that the command "return" is used at the end of the function to output products (any python object) of the function


```python
def safe_divide(numerator,denominator):
    if denominator == 0:
        output = 0
    else:
        output = numerator/denominator

    return output
```


```python
test = safe_divide(1,2)
print(test)
```

    0.5



```python
test2 = safe_divide(0,0)
print(test2)
```

    0



```python
av_freq = safe_divide(freq_counter,n_words)
print(av_freq)
```

    4531.692307692308



```python
av_freq2 = safe_divide(freq_counter2,n_words2)
print(av_freq2)
```

    0


# Part IV: Files
### Reading and writing files is an important aspect NLP
### Both are straightforward in Python
### But, YOU MUST SET/CHECK YOUR WORKING DIRECTORY!!!

# Writing a file


```python
x = open("test_file.txt", "w") #this opens a new file (called "test_file.txt") in the "w" (write) mode. #It will be written to your working directory
```


```python
sample_string = "This is an awesome example sentence.\n\nNote that I can use a newline character to insert hard returns."
x.write(sample_string) #this writes a string to our newly created file
x.flush() #strings are first written to a buffer. The buffer writes to the file when it is full, so we have to make sure that we manually push everything out of the buffer when we are done writing
x.close() #this closes the file
```

# Opening a file
### To read files, we use the .read() method of the open() function
### Files that are read are interpreted as strings


```python
new_file = open("test_file.txt").read()
```


```python
new_file
```




    'This is an awesome example sentence.\n\nNote that I can use a newline character to insert hard returns.'




```python
print(new_file)
```

    This is an awesome example sentence.

    Note that I can use a newline character to insert hard returns.


# Writing a spreadsheet file
### We can easily write a .csv (comma separated values) or .tsv (tab separated values) spreadsheet


```python
sample_spread = open("test_spreadsheet.csv", "w") #create .csv file
sample_spread.write("Operating System,Kris' Opinion\n") #note that the values are separated by "," and that I added a newline character ("\n")

sample_spread.flush() #flush buffer so we can check file
```


```python
for stuff in sample_d:
    outstring = stuff + "," + sample_d[stuff] + "\n" #key + separator + value + newline character
    sample_spread.write(outstring)

sample_spread.flush()
sample_spread.close()
```


```python

```
