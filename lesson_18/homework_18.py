def even_numbers_generator(N):
    for num in range(0, N + 1):
        if num % 2 == 0:
            yield num

def fibonacci_generator(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b


class ReverseListIterator:
    def __init__(self, input_list):
        self.input_list = input_list
        self.index = len(input_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.input_list[self.index]
        self.index -= 1
        return value


class EvenNumbersIterator:
    def __init__(self, N):
        self.N = N
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.N:
            if self.current % 2 == 0:
                result = self.current
                self.current += 1
                return result
            self.current += 1
        raise StopIteration


def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції {func.__name__} з аргументами: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат функції {func.__name__}: {result}")
        return result
    return wrapper


def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(f"Виняток у функції {func.__name__}: {error}")
    return wrapper


@log_arguments
@catch_exceptions
def divide(a, b):
    return a / b

if __name__ == "__main__":
    print("Генератор парних чисел:", list(even_numbers_generator(10)))
    print("Генератор Фібоначчі:", list(fibonacci_generator(30)))

    print("Зворотний ітератор:", list(ReverseListIterator([1, 2, 3, 4, 5])))
    print("Ітератор парних:", list(EvenNumbersIterator(10)))

    print("\nТест декораторів:")
    divide(10, 2)
    divide(5, 0)
