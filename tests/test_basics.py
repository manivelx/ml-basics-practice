import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "python-basics"))

from basics import class_report, fizzbuzz, grade, is_palindrome, word_frequency  # noqa: E402


def test_fizzbuzz():
    assert fizzbuzz(15)[2] == "Fizz"
    assert fizzbuzz(15)[4] == "Buzz"
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    assert fizzbuzz(0) == []


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("machine learning")


def test_word_frequency():
    assert word_frequency("the cat and the hat and the bat", top=2) == [("the", 3), ("and", 2)]


def test_grade_boundaries():
    assert grade(90) == "A"
    assert grade(50) == "D"
    assert grade(49) == "F"
    with pytest.raises(ValueError):
        grade(101)


def test_class_report():
    grades, average = class_report({"A": 90, "B": 50})
    assert grades == {"A": "A", "B": "D"}
    assert average == 70
