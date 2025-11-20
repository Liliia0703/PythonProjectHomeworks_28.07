class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_grade):
        self.average_grade = new_grade

student1 = Student("Діана", "Москвіта", 21, 85)

print("Ім'я:", student1.name)
print("Прізвище:", student1.surname)
print("Вік:", student1.age)
print("Середній бал:", student1.average_grade)

student1.change_average_grade(99)

print("\nПісля зміни середнього балу:")
print("Середній бал:", student1.average_grade)