"""Small Python fundamentals exercises: loops, strings, dicts and functions.

Run `python basics.py` for a demo, or `pytest` from the repo root to run the tests.
"""
from collections import Counter


def fizzbuzz(n):
    """Return the FizzBuzz sequence from 1 to n as a list of strings."""
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def is_palindrome(text):
    """Check a palindrome, ignoring case, spaces and punctuation."""
    cleaned = [ch.lower() for ch in text if ch.isalnum()]
    return cleaned == cleaned[::-1]


def word_frequency(text, top=3):
    """Return the `top` most common words as (word, count) pairs."""
    words = [w.strip(".,!?;:\"'").lower() for w in text.split()]
    return Counter(w for w in words if w).most_common(top)


def grade(marks):
    """Map a mark out of 100 to a letter grade."""
    if not 0 <= marks <= 100:
        raise ValueError("marks must be between 0 and 100")
    for cutoff, letter in ((90, "A"), (80, "B"), (70, "C"), (50, "D")):
        if marks >= cutoff:
            return letter
    return "F"


def class_report(students):
    """Given {name: marks}, return {name: letter} plus the class average."""
    grades = {name: grade(marks) for name, marks in students.items()}
    average = sum(students.values()) / len(students)
    return grades, average


if __name__ == "__main__":
    print(fizzbuzz(15))
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(word_frequency("the cat and the hat and the bat"))
    print(class_report({"Asha": 91, "Ravi": 64, "Meena": 48}))
