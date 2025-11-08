
"""
Lab 3.3 – Operator Frequency Counter

Goals:
- Practice using strings and dictionaries.
- Count character frequencies in user-provided text.

Instructions:
1. Ask the user for an arithmetic expression, e.g. "3 + 5 * (2 - 1) + 7 / 2".
2. Count how many times each operator occurs:
   +  -  *  /  (  )
3. Store counts in a dictionary.
4. Print the result.
"""

# TODO: Get input from the user
expression = input("Enter an arithmetic expression: ")

# Define possible operator symbols
operators = ['+', '-', '*', '/', '(', ')']

# Initialize frequency dictionary with zero counts
operator_counts = {operator: 0 for operator in operators}

# Count operator occurrences
for char in expression:
    if char in operator_counts:
        operator_counts[char] += 1

# Display results
print("Operator counts:")
for operator, count in operator_counts.items():
    print(f"  {operator}: {count}")
