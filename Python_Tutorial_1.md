
# Introduction to Python

### Accessing Python; Values, Variables and Functions

---
#### Prelude: Hello World
In the programming tradition, we must begin with the following program:
```python
print("Hello, World!")
```


```python
>>> print("Hello, World!")
```

    Hello, World!


---
#### We can run this code at least three ways
* Directly in the Python terminal
* By saving a script <script_name.py> that includes the command and running it
* In a Python interpreter (such as spyder)

---

#### Part I: Value types

Python has three basic types of **_values_**:
* strings
* integers
* floats

---

#### Strings
Strings are sequences of characters that are interpreted as text

Strings are defined using quotation marks (" or ')  
```python
"A string can include letters, numbers, or other characters"

'But be careful. Numbers that are represented as strings (like 9)'
'can not be added, subtracted, etc.'
```

---
#### Integers
Integers are whole numbers (i.e., have no decimal places)

Integers can be added, subtracted, multiplied, and divided.

```python
#these are integers:
1
2
3
4
```
---

#### Floats
Floats are numbers that have decimal places

When integers are divided, they are converted to floats
```python
#these are floats:
1.234
2.0
6.789
```
---

#### Part 2: Defining Variables
Defining variables is quite easy in python.

They can be strings, integers, floats (and a variety of other structures)

```python
a = "this is a string"
b = 9
c = 3.2
```

##### what will happen when we run the following line of code?
```python
b + c
```


```python
b+c
```




    12.2



#### Important functions

Functions are called (used) via the following syntax:  
function(arguments)

Commonly used functions include:  
* print() - Prints variable to output
* len() - Provides length of string (# characters) or list (# items)
* str() - Converts integers and floats (and other data) to a string
* int() - Converts strings (if possible) and floats (rounds down) to integers
* float() - Converts strings (if possible) and integers to floats


```python
test_var = "This is a string"
print(test_var)
```

    This is a string



```python
n_char = len(test_var)
n_char
```




    16




```python
n_char_string = str(n_char)
n_char_string
```




    '16'




```python
int(n_char_string)
```




    16




```python
float(n_char_string)
```




    16.0



#### Important Methods

Functions use objects to complete tasks.

Methods are similar to functions, but complete operations on objects, which often changes them.

Methods tend to be specific to particular object types.

Some important **_string_** methods include:
* .lower() Converts all letters in a string to lower case
* .split() This turns strings into lists.


```python
sample_string = "This is a STRING"
l_sample_string = sample_string.lower()
```




    'this is a string'




```python
l_sample_string.split(" ")
```




    ['this', 'is', 'a', 'string']




```python
#but, we can split on any character (note, this deletes that character)
l_sample_string.split("i")
```




    ['th', 's ', 's a str', 'ng']



---
### Next up...
* lists
* tuples
* dictionaries
* functions

---
