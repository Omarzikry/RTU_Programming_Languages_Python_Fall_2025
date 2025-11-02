"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

import re

def count_characters(text):
    """Count non-space characters in a string."""
    return sum(1 for char in text if not char.isspace())

def count_words(text):
    """Count number of words in a string."""
    return len(text.split())

def extract_numbers(text):
    """Return list of integers found in text."""
    matches = re.findall(r"-?\d+", text)
    return [int(match) for match in matches]

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    char_count = count_characters(text)
    word_count = count_words(text)
    numbers = extract_numbers(text)
    total = sum(numbers)
    average = total / len(numbers) if numbers else None

    return {
        "char_count": char_count,
        "word_count": word_count,
        "numbers": numbers,
        "sum": total,
        "average": average,
    }

if __name__ == "__main__":
    user_text = input("Enter text to analyze: ")
    results = analyze_text(user_text)

    print(f"Non-space characters: {results['char_count']}")
    print(f"Word count: {results['word_count']}")
    print(f"Numbers found: {results['numbers']}")
    print(f"Sum of numbers: {results['sum']}")
    if results["average"] is not None:
        print(f"Average of numbers: {results['average']:.2f}")
    else:
        print("Average of numbers: N/A")
