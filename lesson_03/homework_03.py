#Task1
alice_in_wonderland = (
'"Would you tell me, please, which way I ought to go from here?"\n'
'"That depends a good deal on where you want to get to," said the Cat.\n'
'"I don\'t much care where —" said Alice.\n.'
)

#Task2
print("Task_2")
indices = [i for i, ch in enumerate(alice_in_wonderland) if ch == "'"]
print(f"{len(indices)}")
print()

#Task3
print("Task_3")
print(alice_in_wonderland)
print()

#Task4
print("Task_4")
black_sea_area = 436_402
azov_sea_area = 37_800
total_area = black_sea_area + azov_sea_area
print(f"Площа чорного моря становить {black_sea_area} км².")
print(f"Площа Азовського моря становить {azov_sea_area} км²")
print(f"Яку площу займають Чорне і Азовське море разом? Відповідь:{total_area}")
print()

#Task5
print("Task_5")
total_goods = 375_291
first_second_goods = 250_449
second_third_goods = 222_950
third = total_goods - first_second_goods
second = second_third_goods - third
first = first_second_goods - second
print(f"Мережа супермаркетів має три склади, де всього розміщено {total_goods} товарів")
print(f"На першому та другому складах перебуває {first_second_goods} товарів")
print(f"На другому та третьому {second_third_goods} товарів")
print("Яка кількість товарів на складах?")
print(f"На першому складі {first} товарів.")
print(f"На другому складі {second} товарів")
print(f"На третьому складі {third} товарів")
print()

#Task6
print("Task_6")
months = 18
monthly_payment = 1179
total_price = months * monthly_payment
print("Михайло разом з батьками вирішили купити комп’ютер, скориставшись послугою Оплата частинами.")
print(f"Відомо, що сплачувати необхідно буде {months} місяців, по {monthly_payment} грн/місяць")
print(f"Обчисліть вартість комп’ютера. Відповідь: {total_price}")
print()

#Task7
print("Task_7")
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(f"a) 8019 % 8 = {a}")
print(f"b) 9907 % 9 = {b}")
print(f"c) 2789 % 5 = {c}")
print(f"d) 7248 % 6 = {d}")
print(f"e) 7128 % 5 = {e}")
print(f"f) 19224 % 9 = {f}")
print()

#Task8
print("Task_8")
order = """\
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
"""
print(order)
food_products = [
    ("pizza_large", 4, 274),
    ("pizza_medium", 2, 218),
    ("juice", 4, 35),
    ("cake", 1, 350),
    ("water", 3, 21)
]
total_cost = 0
print("Замовлення Іринки:")
for name, pieces, price in food_products:
    item_total = pieces * price
    total_cost += item_total
    print(f"{name}: {pieces} шт × {price} грн = {item_total} грн")
print(f"\nЗагальна вартість замовлення: {total_cost} грн")
print()

#Task9
print("Task_9")
photos = 232
per_page = 8
pages_needed = photos // per_page
print(f"Ігор вирішив зібрати всі свої {photos} фотографії та вклеїти в альбом.")
print(f"На одній сторінці може бути розміщено {per_page} фото")
print(f"Скільки сторінок знадобиться Ігорю, щоб вклеїти всі фото? Відповідь: {pages_needed}")
print()

#Task10
print("Task_10")
distance_km = 1600
consumption_per_100 = 9
per_100_km = 100
tank_l = 48
liters_needed = distance_km // per_100_km * consumption_per_100
stops = liters_needed // tank_l
print("Родина зібралася в автомобільну подорож із Харкова в Будапешт.")
print(f"Відстань між цими містами становить {distance_km} км.")
print(f"Відомо, що на кожні {per_100_km} км необхідно {consumption_per_100} літрів бензину.")
print(f"Місткість бака становить {tank_l} літрів.")
print(f"Скільки літрів бензину знадобиться для такої подорожі? Відповідь: {liters_needed}")
print("Скільки щонайменше разів родині необхідно заїхати на заправку під час цієї подорожі, кожного разу заправляючи повний бак?")
print(f"Відповідь: {stops}")

