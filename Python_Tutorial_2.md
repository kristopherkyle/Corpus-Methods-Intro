[Back to Tutorial Index](py_index.md)

# Python Tutorial 2

### More fun with Python:  
### Conditionals, Loops, Strings, and Lists

# Part I: Conditionals

### Conditional statements are very powerful

#### The most commonly used conditional statement is the 'if' statement and its children, the 'elif' and 'else' statements 


```python
os1 = "Windows"
os2 = "Mac"
os3 = "Linux"
os4 = "some gibberish"

#computer = "Linux"
computer = "Windows"
if computer == os1:
    print("not awesome")
elif computer == os2:
    print("awesome")
elif computer == os3:
    print("super awesome, we are not worthy!")
else:
    print("What the devilry is this?")
```

# Possible operators in Python

| Operator | Description |
|:----|---|
| **x == y** | _x is equal to y_|
| **x != y** | _x is not equal to y_
| **x > y** | _x is greater than y_
| **x < y** |  _x is less than y_
| **x >= y** | _x is greater than or equal to y_
| **x <= y** | _x is less than or equal to y_


# More fun with strings

#### Strings can be:
* **Indexed (using [ ]) :** _retrieve one character from a particular location in a string_
* **Sliced (using [ : ]) :** _retrieve multiple contiguous characters from a particular location in a string_
* **Concatenated (using "+") :** _strings can be added together to make longer strings_
* **Searched (using _in_) :** _we can check if certain characters (or character combinations) are in a string_




```python
#indexing
sample_string = "sample"

i1 = sample_string[0] #note, index counts start at 0 NOT 1
i2 = sample_string[1] #second letter
i3 = sample_string[-1] #last letter

print(i1)
```

    s



```python
#slices
s1 = sample_string[0:1] #start at position 0, grab characters until you get to position 1
s2 = sample_string[0:2] #start at position 0, grab characters until you get to position 2
s3 = sample_string[1:-1] #start at position 1, grab characters until you get to last position
s4 = sample_string[1:] #start at position 1, grab all following characters
s5 = sample_string[:2] #start at beginning, grab characters until you get to position 2

print(s3)
```

    ampl



```python
#concatenation
sample1 = "awesome"
sample2 = "super"

sample3 = sample2 + sample1
print(sample3)
```

    superawesome



```python
sample4 = sample2 + " " + sample1
print(sample4)
```

    super awesome



```python
#searching in strings
if "a" in sample1:
    print("yay!")
else:
    print("nope")

```

    yay!



```python
#searching in strings
if "a" in sample2:
    print("yay!")
else:
    print("nope")
```

    nope


# Lists
#### Lists are awesome
#### In Python, lists are indicated by square brackets [ ]
#### List items are separated by commas
#### Almost any Python object can be a list item
#### Lists can be:
* **Indexed (using [ ]) :** _retrieve one list item from a particular location in a list_
* **Sliced (using [ : ]) :** _retrieve multiple contiguous list items from a particular location in a list
* **Concatenated (using ".append()") :**_almost any Python object can be appended to a list to make a longer list_
* **Searched (using _in_) :** _we can check if certain objects are in a list_
* **Changed (using list_name[position] = y ) :** _We can replace items in certain positions in lists_



```python
#indexing
l1 = ["Windows","Mac","Linux"]

l1[1] #just like strings, we can get particular list items
```




    'Mac'




```python
#slicing
l1[1:] #just like strings, we can get multiple list items
```




    ['Mac', 'Linux']




```python
#concatenate
l1.append("new string")
l1
```




    ['Windows', 'Mac', 'Linux', 'new string']




```python
#Change items
l1[0] = "rubbish"
l1
```




    ['rubbish', 'Mac', 'Linux', 'new string']



# Loops
#### Loops are awesome. With conditional statements, they are the backbone of programming
#### Things to remember when working with loops:
* You can loop over any iterable item (e.g., strings, lists, tuples, and dictionaries)
* Loops use local and global variables. Don't confuse the two!
* You can have if statements inside of loops
* You can have loops inside of loops
* You must be careful with loops levels


```python
#Creating a loop:
sl = ["a", "wonderful", "list", "this", "is"]

for x in sl: #note that 'x' is  local variable and is completely arbitrary 
    print(x) #we can call the local variable
```

    a
    wonderful
    list
    this
    is



```python
#if statements in loops
for x in sl:
    if "t" in x:
        print(x)
    else:
        continue #continue tells the loop to go to the next item
```

    list
    this


# Exercise
#### 1. Assign the string "This is an awesome sample sentence" to the variable _a_
#### 2. Split the string into a list and assign it to variable _b_
#### 3. Write a loop that prints each item in _b_ if the last letter in the item is "e"
#### 4. Define a new empty list and assign it to variable _c_
#### 5. Write a loop that adds each item in _b_ to _c_ if the last letter in the item is "e"


```python
a = "This is an awesome sample sentence"
b = a.split(" ")

for blah in b:
    if blah[-1] == "e":
        print(blah)
    else: 
        continue
```

    awesome
    sample
    sentence



```python
a = "This is an awesome sample sentence"
b = a.split(" ")
c = []
for blah in b:
    if blah[-1] == "e":
        c.append(blah)
    else: 
        continue
print(c)
```

    ['awesome', 'sample', 'sentence']



```python

```
