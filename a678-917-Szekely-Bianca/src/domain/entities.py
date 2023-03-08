class Student:
    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # student_1 == student_2
    def __eq__(self, x):
        if int(self.__student_id) == int(x.get_id):
            return True
        return False

    def __str__(self):
        return f"Student Id:  {str(self.__student_id)}, Name:  {self.__name}"

    def __repr__(self):
        return str(self)


class Discipline:
    def __init__(self, discipline_id, name):
        self.__discipline_id = discipline_id
        self.__name = name

    def get_id(self):
        return self.__discipline_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"Discipline Id: {str(self.__discipline_id)}, Name: {self.__name}"

    def __repr__(self):
        return str(self)


class Grade:
    def __init__(self, student_id, discipline_id, grade_value):
        self.__student_id = student_id
        self.__discipline_id = discipline_id
        self.__grade_value = grade_value

    def get_student_id(self):
        return self.__student_id

    def get_discipline_id(self):
        return self.__discipline_id

    def grade_value(self):
        return self.__grade_value

    def __str__(self):
        return f"Student Id: {str(self.__student_id)}, Discipline Id: {str(self.__discipline_id)}, " \
               f"Grade Value: {str(self.__grade_value)}"

    def __repr__(self):
        return str(self)