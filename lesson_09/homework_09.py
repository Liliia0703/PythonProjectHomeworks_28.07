import pytest
from lesson_09.test_homework_09 import (
    multiplication_table,
    is_palindrome,
    find_max_number,
    average,
    count_vowels
)

def test_multiplication_table_basic():
    assert multiplication_table(3) == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

def test_multiplication_table_zero():
    assert multiplication_table(0) == [0] * 10

def test_palindrome_true():
    assert is_palindrome("Anna") is True

def test_palindrome_false():
    assert is_palindrome("Python") is False

def test_find_max_number_normal():
    assert find_max_number([1, 5, 9, 2]) == 9

def test_find_max_number_negative():
    assert find_max_number([-10, -5, -20]) == -5

def test_find_max_number_empty():
    with pytest.raises(ValueError):
        find_max_number([])

def test_average_basic():
    assert average([2, 4, 6]) == pytest.approx(4.0)

def test_average_empty():
    with pytest.raises(ValueError):
        average([])

def test_count_vowels_english():
    assert count_vowels("Beautiful") == 5

def test_count_vowels_ukrainian():
    assert count_vowels("Лілія") == 3