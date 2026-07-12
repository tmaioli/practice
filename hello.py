"""
================================================================================
PYTHON FUNDAMENTALS PRACTICE SCRIPT
================================================================================

Purpose:
    This script serves as a comprehensive learning tool for Python beginners,
    demonstrating core programming concepts through practical examples.

Functional Breakdown:
    1. Variable Declaration & Data Types - Integers, floats, and strings
    2. Arithmetic Operations - Adding different numeric types
    3. Type Inspection - Using type() to identify variable types
    4. String Indexing & Slicing - Accessing specific characters and substrings
    5. String Methods - strip(), upper(), replace(), split()
    6. Built-in Functions - len() for string length
    7. User Input - Interactive console input with input()
    8. String Concatenation - Combining strings for output

Learning Objectives:
    - Understand Python's dynamic typing system
    - Master basic string manipulation techniques
    - Learn method syntax (object.method())
    - Practice interactive program creation

Author: Learning Repository
Version: 1.0
Date: 2024
================================================================================
"""

# =============================================================================
# SECTION 1: VARIABLE DECLARATION AND BASIC DATA TYPES
# =============================================================================
# This section demonstrates how to create variables with different data types:
# - Integers (whole numbers)
# - Strings (text data)
# - Floats (decimal numbers)
# =============================================================================

# Initialize an integer variable
number = 5

# Initialize a string variable
msg = "high"

# Display the string variable content
print(msg)

# Display a classic greeting message
print("Hello world")

# Display the integer variable content
print(number)

# =============================================================================
# SECTION 2: ARITHMETIC OPERATIONS AND TYPE COERCION
# =============================================================================
# This section demonstrates:
# - Creating float and integer variables
# - Adding different numeric types (float + int = float)
# - Python's automatic type coercion in arithmetic operations
# =============================================================================

# Initialize a float variable (note: variable names are case-sensitive)
Number1 = 2.01

# Initialize an integer variable
number2 = 4

# Perform addition - result will be a float due to mixed types
total = Number1 + number2

# Display the arithmetic result
print(total)

# Display the data type of the result (demonstrates type inspection)
# Expected output: <class 'float'> because float + int = float
print(type(total))

# =============================================================================
# SECTION 3: STRING INDEXING AND SLICING
# =============================================================================
# This section demonstrates:
# - String indexing (accessing individual characters by position)
# - String slicing (extracting substrings using [start:end] notation)
# - The len() function to count characters including whitespace
# =============================================================================

# Create a string with leading and trailing whitespace for method demonstrations
stringvar = "    hello    "

# Display the first character (index 0) - will show a space
print(stringvar[0])

# Display characters from index 0 to 2 (end index 3 is exclusive)
# This extracts the first 3 characters including spaces
print(stringvar[0:3])

# Display the total length of the string including all whitespace
# len() counts every character including spaces
print(len(stringvar))

# =============================================================================
# SECTION 4: STRING METHODS - CLEANING AND TRANSFORMATION
# =============================================================================
# This section demonstrates common string methods:
# - strip(): Remove leading and trailing whitespace
# - upper(): Convert all characters to uppercase
# - replace(): Substitute characters or substrings
# - split(): Divide string into a list based on a delimiter
# 
# Syntax Note: Methods are called using dot notation: object.method()
# =============================================================================

# Remove leading and trailing whitespace from the string
print(stringvar.strip())

# Convert the entire string to uppercase letters
print(stringvar.upper())

# Replace all occurrences of 'h' with 'x' (case-sensitive)
# Note: Only lowercase 'h' will be replaced, not 'H'
print(stringvar.replace("h", "x"))

# =============================================================================
# SECTION 5: STRING SPLITTING INTO LISTS
# =============================================================================
# This section demonstrates:
# - Creating a sentence string
# - Using split() to convert a string into a list of words
# - Splitting on space character as the delimiter
# =============================================================================

# Create a sentence with multiple words
Sentence = "This is a sentence and it has spaces between the words"

# Split the sentence into a list of words using space as delimiter
# Result: ['This', 'is', 'a', 'sentence', 'and', 'it', 'has', 'spaces', 
#          'between', 'the', 'words']
print(Sentence.split(" "))

# =============================================================================
# SECTION 6: USER INPUT AND STRING CONCATENATION
# =============================================================================
# This section demonstrates:
# - Displaying a prompt message to the user
# - Capturing user input from the console using input()
# - Concatenating strings using the + operator
# - Creating personalized interactive output
# =============================================================================

# Display a prompt message asking for user input
msg = "Your name:   "
print(msg)

# Capture user input from the console
# input() pauses program execution and waits for user to type and press Enter
username = input()

# Create a personalized greeting by concatenating strings
# The + operator joins two strings together
print("Hello " + username)
