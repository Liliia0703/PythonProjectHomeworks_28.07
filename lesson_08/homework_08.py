def sum_numbers_in_string(s: str):
    try:
        numbers = s.split(",")
        total = sum(int(n) for n in numbers)
        return total
    except ValueError:
        return "Не можу це зробити!"

data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for item in data:
    print(sum_numbers_in_string(item))