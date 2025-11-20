class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Довжина сторони a повинна бути більшою за 0.")
            object.__setattr__(self, name, value)

        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут a повинен бути в діапазоні (0; 180).")
            object.__setattr__(self, "angle_a", value)
            angle_b = 180 - value
            object.__setattr__(self, "angle_b", angle_b)

        elif name == "angle_b":
            if not (0 < value < 180):
                raise ValueError("Кут b повинен бути в діапазоні (0; 180).")
            angle_a = 180 - value
            object.__setattr__(self, "angle_a", angle_a)
            object.__setattr__(self, "angle_b", value)

        else:
            object.__setattr__(self, name, value)

    def show_info(self):
        print(f"Сторона a: {self.side_a}")
        print(f"Кут a: {self.angle_a}")
        print(f"Кут b: {self.angle_b}")
        print(f"Сума кутів a + b: {self.angle_a + self.angle_b}")

rhombus1 = Rhombus(5, 60)

print("Початкові значення:")
rhombus1.show_info()

print("\nЗмінюємо кут a на 30 градусів...")
rhombus1.angle_a = 30

print("\nПісля зміни:")
rhombus1.show_info()
