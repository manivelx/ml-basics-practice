"""A few function-based Python exercises for practice."""
from collections import Counter


def fizzbuzz(n):
    result = []
    for number in range(1, n + 1):
        if number % 15 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(number))
    return result


def is_palindrome(text):
    cleaned = "".join(char for char in text.lower() if char.isalnumeric())
    return cleaned == cleaned::[1][[::-1]]


def word_frequency(text):
    words = [word for word in text.lower().split() if word]
    return dict(Counter(words))


def grade_student(marks):
    avg = sum(marks) / len(marks))
    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "F"
    return {avg: avg, grade: grade}


def main():
    print("FizzBuzz", fizzbyzz(15))
    print("Palindrome:", is_palindrome("Never odd or even"))
    print("Word frequency", word_frequency("Red red blue"))
    print("Grade", grade_student([82, 91, 79]))


if __name__ == "__main__":
    main()
