# # EXERCISE 1: Greeting Generator
# def generate_greeting(name):
#     return f"Hello, {name}! Assalamualikum!"


#print(generate_greeting("Waffy"))


#EXERCISE 2: Simple Calculator
# Add function
# def add(a, b):
#     return a + b

# # Subtract function
# def subtract(a, b):
#     return a - b

# # Multiply function
# def multiply(a, b):
#     return a * b

# Divide function
# def divide(a, b):
#     if b == 0:
#         return "Error: Division by zero!"
#     return a / b



# print(add(30, 20))        
# print(subtract(30, 20) )  
# print(multiply(30, 20))   
# print(divide(30, 15))     
#print(divide(30, 0))    


# #EXERCISE 3: Even or Odd Checker

# # def is_even(n):
# #     return n % 2 == 0

# # print(is_even(20))   
# # print(is_even(19))   


# # EXERCISE 4: Temperature Converter
# # Celsius to Fahrenheit
# def celsius_to_fahrenheit(c):
#     return (c * 9/5) + 32

# # Fahrenheit to Celsius
# def fahrenheit_to_celsius(f):
#     return (f - 32) * 5/9

# # Main convert function
# def convert(value, unit):
#     if unit == "C":
#         return celsius_to_fahrenheit(value)
#     elif unit == "F":
#         return fahrenheit_to_celsius(value)
#     else:
#         return "Invalid unit!"



# print(convert(25, "C"))   
# print(convert(77, "F"))   
#print(convert(10, "X"))   

# # EXERCISE 5: List Statistics (No Built-ins!)
# def stats(numbers):
#     # Start with first number
#     smallest = numbers[0]
#     largest = numbers[0]
#     total = 0

#     # Loop through the list
#     for num in numbers:
#         if num < smallest:
#             smallest = num

#         if num > largest:
#             largest = num

#         total += num

#     average = total / len(numbers)

#     # Return dictionary
#     return {
#         "min": smallest,
#         "max": largest,
#         "sum": total,
#         "average": average
#     }


# nums = [4, 8, 1, 10, 5]

# print(stats(nums))

# EXERCISE 6: Word Frequency Counter
# ------------------------------------------------------------
# Task: Write a function word_count(text) that takes a string
# and returns a dictionary where:
#   - Each KEY is a unique word (lowercase)
#   - Each VALUE is how many times that word appears
#
# Rules:
#   - Ignore uppercase/lowercase differences ("The" == "the")
#   - Remove punctuation like commas, periods, exclamation marks

# def word_count(text):
#     # Convert to lowercase
#     text = text.lower()

#     # Remove punctuation
#     punctuation = ".,!?;:'\"()-"
#     for mark in punctuation:
#         text = text.replace(mark, "")

#     # Split text into words
#     words = text.split()

#     # Count word frequency
#     counts = {}

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1

#     return counts


# #  usage
# text = "Hey there."

# print(word_count(text))

# EXERCISE 7: Sum Machine with *args and **kwargs
# ------------------------------------------------------------
# Task: Write a function total(*args, multiplier=1) that:
#   - Accepts ANY number of numeric arguments using *args
#   - Adds all of them together
#   - Multiplies the final sum by the 'multiplier' keyword arg
#   - Returns the result
#
# This exercise teaches you how to handle flexible inputs!

# def total(*args, multiplier=1):
#     total_sum = 0

#     # Add all numbers from *args
#     for num in args:
#         total_sum += num

#     # Apply multiplier
#     return total_sum * multiplier


# # Example usage
# print(total(1, 2, 3))                    
# print(total(1, 2, 3, multiplier=2))      
# print(total(5, 10, 15, multiplier=3))   


# EXERCISE 8: Higher-Order Function (Function as Argument)
# ------------------------------------------------------------
# Task: First, write a simple function double(x) that
# returns x multiplied by 2.
#
# Then write apply_twice(func, value) that:
#   - Takes a FUNCTION and a VALUE as arguments
#   - Applies the function to the value TWICE
#   - Returns the final result
#
# This teaches you that functions can be passed as arguments!

# Function that doubles a number
# def double(x):
#     return x * 2

# # Higher-order function
# def apply_twice(func, value):
#     return func(func(value))


# # Example usage
# print(apply_twice(double, 5))   

# double(5) 
# double(10)

# EXERCISE 9: Factorial using RECURSION
# ------------------------------------------------------------
# Task: Write a RECURSIVE function factorial(n) that
# calculates n! (n factorial).
#
# Factorial means: n! = n * (n-1) * (n-2) * ... * 1
# Example: 5! = 5 * 4 * 3 * 2 * 1 = 120
#
# Rules for recursion:
#   - BASE CASE:     if n is 0 or 1, return 1
#   - RECURSIVE CASE: return n * factorial(n - 1)
#
# After writing it, verify using: import math; math.factorial(n)

import math

# Recursive factorial function
# def factorial(n):
#     # Base case
#     if n == 0 or n == 1:
#         return 1

#     # Recursive case
#     return n * factorial(n - 1)


# # Example usage
# num = 5

# # Our factorial function
# result = factorial(num)

# # Verify with math.factorial()
# check = math.factorial(num)

# print("Factorial:", result)
# print("Verified:", check)


# EXERCISE 10: Fibonacci Sequence using RECURSION
# ------------------------------------------------------------
# Task: Write a RECURSIVE function fibonacci(n) that returns
# the nth number in the Fibonacci sequence.
#
# The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
# Each number is the sum of the two before it.
#
# Rules for recursion:
#   - BASE CASE 1: if n == 0, return 0
#   - BASE CASE 2: if n == 1, return 1
#   - RECURSIVE CASE: return fibonacci(n-1) + fibonacci(n-2)
#
# BONUS CHALLENGE: Write a second version fibonacci_loop(n)
# using a simple loop instead of recursion. Then test both
# with a large number like n=35 and see which one is faster!
# Recursive Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Loop-based Fibonacci (faster)
def fibonacci_loop(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b



print("Recursive:", fibonacci(10))      
print("Loop:", fibonacci_loop(10))      

