# 0x01. Python - if/else, loops, functions

## Resources
Read or watch:

More Control Flow Tools (Read until “4.6. Defining Functions” included)
IndentationError
How To Use String Formatters in Python 3
Learn to Program
Learn to Program 2 : Looping
Pycodestyle – Style Guide for Python Code
man or help:

## python3

### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
Why Python programming is awesome
Why indentation is so important in Python
How to use the if, if ... else statements
How to use comments
How to affect values to variables
How to use the while and for loops
How is Python’s for different from C‘s?
How to use the break and continues statements
How to use else clauses on loops
What does the pass statement do, and when to use it
How to use range
What is a function and how do you use functions
What does return a function that does not use any return statement
Scope of variables
What’s a traceback
What are the arithmetic operators and how to use them
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.


## Requirements

### Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc

### C Scripts
Allowed editors: vi, vim, emacs
All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
All your files should end with a new line
Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
You are not allowed to use global variables
No more than 5 functions per file
In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
The prototypes of all your functions should be included in your header file called lists.h
Don’t forget to push your header file
All your header files should be include guarded

0-positive_or_negative.py - This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

1-last_digit.py - This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.The output of the program should be:
The string Last digit of, followed by
the number, followed by
the string is, followed by the last digit of number, followed by
if the last digit is greater than 5: the string and is greater than 5
if the last digit is 0: the string and is 0
if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
followed by a new line

2-print_alphabet.py - program that prints the ASCII alphabet, in lowercase, not followed by a new line.

You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store characters in a variable
You are not allowed to import any module

3-print_alphabt.py -  a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

Print all the letters except q and e
You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store characters in a variable
You are not allowed to import any module

4-print_hexa.py -  a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)

You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module

5-print_comb2.py - a program that prints numbers from 0 to 99.

Numbers must be separated by ,, followed by a space
Numbers should be printed in ascending order, with two digits
The last number should be followed by a new line
You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module


6-print_comb3.py - a program that prints all possible different combinations of two digits.

Numbers must be separated by ,, followed by a space
The two digits must be different
01 and 10 are considered the same combination of the two digits 0 and 1
Print only the smallest combination of two digits
Numbers should be printed in ascending order, with two digits
The last number should be followed by a new line
You can only use no more than 3 print functions with string format
You can only use no more than 2 loops in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module

7-islower.py -  function that checks for lowercase character.

Prototype: def islower(c):
Returns True if c is lowercase
Returns False otherwise
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
Tips: ord()
You don’t need to understand __import__
