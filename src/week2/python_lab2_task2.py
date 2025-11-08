"""
Lab 3.2 – Comprehensions and Transformations

Goals:
- Practice list, set, and dictionary comprehensions.
- Transform and filter data concisely.

Instructions:
Given the list:
    numbers = [3, 8, -2, 7, 0, -5, 10]

1. Create a list `squares` with the square of each number.
2. Create a list `positives` containing only positive numbers.
3. Create a set `even_squares` of the squares of even numbers.
4. Create a dictionary `cubes` mapping each number to its cube.
5. Print all results.
"""

# Source numbers
numbers = [3, 8, -2, 7, 0, -5, 10]

# Comprehension-based transformations
squares = [number**2 for number in numbers]
positives = [number for number in numbers if number > 0]
even_squares = {number**2 for number in numbers if number % 2 == 0}
cubes = {number: number**3 for number in numbers}

# Output results
print("Squares:", squares)
print("Positives:", positives)
print("Even squares:", even_squares)
print("Cubes:", cubes)
