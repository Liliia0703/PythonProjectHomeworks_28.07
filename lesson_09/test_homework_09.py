def multiplication_table(number: int) -> list:
    return [number * i for i in range(1, 11)]


def is_palindrome(word: str) -> bool:
    return word.lower() == word[::-1].lower()


def find_max_number(numbers: list) -> int:
    if not numbers:
        raise ValueError("List is empty")
    return max(numbers)


def average(numbers: list) -> float:
    if not numbers:
        raise ValueError("List is empty")
    return sum(numbers) / len(numbers)


def count_vowels(word: str) -> int:
    vowels = "aeiouаеєиіїоуюя"
    return sum(1 for char in word.lower() if char in vowels)