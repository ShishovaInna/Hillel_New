from student import Student

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()


    def add_student(self, student):
        if len(self.group) >= 10:
            raise MyException('The group is already full')
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + '\n'
        return f'Number:{self.number}\n{all_students} '


class MyException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'{self.value}'
