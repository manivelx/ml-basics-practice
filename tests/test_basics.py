"""Small unit tests for python-basics/basics.py."""
from python_basics.basics import grade_student, is_palindrome, word_frequency

def test_is_palindrome_ignores_case_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!")

def test_word_frequency_counts():
    assert word_frequency("Red red blue") == {"red": 2, "blue": 1}

def test_grade_student_returns_average_and_grade():
    result = grade_student([82, 91, 79])
    assert result["grade"] == "A"
    assert result["avg"] == 84.0
