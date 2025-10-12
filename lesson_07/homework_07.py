#Task_1
print("Task_1")

def multiplication_table(number):

    multiplier = 1

    while True:
        result = number * multiplier

        if result > 25:
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1

multiplication_table(3)
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
# 3x6=18
# 3x7=21
# 3x8=24
print()

#Task_2
print("Task_2")

def add_two_numbers(num1, num2):

    result = 0

    result = num1 + num2

    return result
print(add_two_numbers(5, 7))
print()

#Task_3
print("Task_3")

def average(numbers):

    if len(numbers) == 0:
        return 0

    total = sum(numbers)

    count = len(numbers)

    avg = total//count

    return avg
print(average([1, 2, 3, 4, 5]))
print(average([]))
print()

#Task_4
print("Task_4")

def reverse_string(text: str) -> str:
    return text[::-1]
print(reverse_string("Liliia"))
print()

#Task_5
print("Task_5")

def find_longest_word(words: list[str]) -> str:
    return max(words, key=len)

print(find_longest_word(["flower", "animals", "tree"]))
print()


#Task_6
print("Task_6")

def find_substring(str1: str, str2: str) -> int:
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))
print()

#Task_7
print("Task_7")

def has_more_than_10_unique_chars() -> bool:
    """
    Просить у користувача ввести рядок.
    Повертає True, якщо унікальних символів більше 10, інакше False.
    """
    text = input("Hello: ")
    return len(set(text)) > 10
print(has_more_than_10_unique_chars())
print()

#Task_8
print("Task_8")

def input_word_with_h() -> str:
    """
    Просить користувача вводити слово, поки воно не буде містити букву 'h'/'H'.
    Повертає правильне слово.
    """
    while True:
        word = input("Word with 'h': ")
        if 'h' in word.lower():
            return word
print(input_word_with_h())
print()

#Task_9
print("Task_9")

def filter_strings_from_list(data: list) -> list[str]:
    """
    Приймає список і повертає новий список, що містить лише рядки.
    """
    return [x for x in data if isinstance(x, str)]

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(filter_strings_from_list(lst1))
print()

#Task_10
print("Task_10")

def sum_even_numbers(numbers: list[int]) -> int:
    """
    Приймає список чисел і повертає суму всіх парних чисел.
    """
    return sum(x for x in numbers if isinstance(x, int) and x % 2 == 0)
print(sum_even_numbers([1, 2, 3, 4, 5, 6, 10, 11]))
print()





