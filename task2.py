#Класс студентов
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def rate_lecturer(self, lecturer, course, grade): #Выставление оценок за лекции
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self): #Средняя оценка за дз
        if self.grades:
            total = 0
            count = 0
            for course, grades in self.grades.items():
                total += sum(grades)
                count += len(grades)
            return total/count
        return 'Нет оценок'

    def __str__(self):
        courses_in_progress_str = ' , '.join(self.courses_in_progress)
        finished_courses_str = ' , '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nКурсы в процессе изучения: {courses_in_progress_str}" \
               f"\nЗавершенные курсы: {finished_courses_str}\nСредняя оценка за дз: {self.average_grade()}"




# student1 = Student('Ruoy', 'Eman', 'your_gender')
# student1.courses_in_progress += ['Python']
# student1.finished_courses += ['Git']
# student1.grades['Python'] = [9, 10, 9]
# student1.grades['Git'] = [8, 8, 7]
#
# student2 = Student('Puuk', 'Kryak', 'your_gender')
# student2.courses_in_progress += ['Python', 'Git']
# student2.finished_courses += ['SQL']
# student2.grades['Python'] = [6, 10, 8]
# student2.grades['Git'] = [6, 7, 10]

# if student1 > student2:
#     print(f"{student1.name} {student1.surname} имеет выше среднюю оценку за дз")
# elif student1 < student2:
#     print(f'{student2.name} {student2.surname} имеет выше среднюю оценку за дз')
# elif student1 == student2:
#     print(f'{student1.name} {student1.surname} и {student2.name} {student2.surname} имеют одинаковые средние оценки за дз')

# print(student1)

#Класс менторов
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_attached = []
        self.grades = {}

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def average_grade(self): #Средняя оценка за лекцию
        if self.grades:
            total = 0
            count = 0
            for course, grades in self.grades.items():
                if course in self.lecturer_attached:
                    total += sum(grades)
                    count += len(grades)
            return total / count if count > 0 else 'Нет оценок'


    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.average_grade()}"



# lecturer1 = Lecturer('John', 'Doe')
# lecturer1.lecturer_attached += ['Python']
# lecturer1.grades['Python'] = [10, 8, 9]
#
# lecturer2 = Lecturer('Patrick', 'Poor')
# lecturer2.lecturer_attached += ['Python', 'Git']
# lecturer2.grades['Python'] = [10, 8, 9]
#
# if lecturer1 > lecturer2:
#     print(f"{lecturer1.name} {lecturer1.surname} имеет выше среднюю оценку за лекции")
# elif lecturer1 < lecturer2:
#     print(f"{lecturer2.name} {lecturer2.surname} имеет выше среднюю оценку за лекции")
# elif lecturer1 == lecturer2:
#     print(f"{lecturer1.name} {lecturer1.surname} и {lecturer2.name} {lecturer2.surname} имеют одинаковые средние оценки за лекции")

# print(lecturer1)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.reviewer_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.reviewer_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

# reviewer1 = Reviewer('Mark', 'Kim')
# reviewer2 = Reviewer('Peter', 'Parker')
# print(reviewer1)

def average_grade_hw_course(students, course): #Средняя оценка за домашние задания по всем студентам в рамках конкретного курса
    total_grades_hw = 0
    count_grades_hw = 0
    for student in students:
        if course in student.grades:
            total_grades_hw += sum(student.grades[course])
            count_grades_hw += len(student.grades[course])
    return total_grades_hw / count_grades_hw if count_grades_hw > 0 else 'Нет оценок'

# students = [
#     Student('Masha', 'Petrova', 'female'),
#     Student('Katya', 'Pupkina', 'female')
# ]
#
# students[0].grades['Python'] = [8, 9, 10]
# students[1].grades['Python'] = [9, 7]
#
# average_grade = average_grade_hw_course(students, 'Python')
# print(average_grade)

def average_grade_lecture_course(lecturer, course): #Средняя оценка за лекции всех лекторов в рамках курса
    total_grades_lecture = 0
    count_grades_lecture = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades_lecture += sum(lecturer.grades[course])
            count_grades_lecture += len(lecturer.grades[course])
    return total_grades_lecture / count_grades_lecture if count_grades_lecture > 0 else 'Нет оценок'

# lecturers = [
#     Lecturer('Ted', 'Mosby'),
#     Lecturer('Kara', 'Pit')
# ]
#
# lecturers[0].grades['Python'] = [9, 9, 7]
# lecturers[1].grades['Python'] = [9, 9, 6]
#
# average_grade = average_grade_lecture_course(lecturers, 'Python')
# print(average_grade)

