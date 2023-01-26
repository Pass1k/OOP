class Student:
    def __init__(self, full_name, number_g, performance):
        self.full_name = full_name
        self.number_g = number_g
        self.performance = performance

    def average_score(self):
        return sum(self.performance) / len(self.performance)

    def __str__(self):
        result = f'{self.full_name} {self.number_g} {self.average_score()}'
        return result


students = []

for i in range(2):
    print(f'Студент {i + 1}: ')
    full_name = input('ФИО: ')
    group_n = int(input('Номер группы: '))
    academic_p = list(map(int, input("Оценки: ").split()))
    students.append(Student(full_name, group_n, academic_p))

sort = sorted(students, key=lambda student: student.average_score())
print(*sort, sep='\n')