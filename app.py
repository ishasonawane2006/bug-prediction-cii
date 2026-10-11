"""Sample application: a tiny calculator and string utility module."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print("add(2, 3) =", add(2, 3))
    print("divide(10, 2) =", divide(10, 2))
    print("is_palindrome('Madam') =", is_palindrome("Madam"))
