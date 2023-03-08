from src.errors.errors import RepoError


class StudentRepo:
    def __init__(self):
        self.__students_list = []

    def search_student(self, student_id):
        idx = 0
        for other in self.__students_list:
            if other.get_id() == student_id:
                return idx
            idx = idx + 1
        return - 1

    def add_student(self, student):
        if self.search_student(student.get_id) != -1:
            raise RepoError("Existing student!")
        self.__students_list.append(student)

    def remove_student(self, student_id):
        if self.search_student(student_id) == -1:
            raise RepoError("Non-existing student!")
        del self.__students_list[self.search_student(student_id)]

    def update_student(self,student_id,new_name):
        if self.search_student(student_id) == -1:
            raise RepoError("Non-existing student!")
        student = self.__students_list[self.search_student(student_id)]
        student.set_name(new_name)

    def get_students_list(self):
        return self.__students_list


class DisciplineRepo:
    def __init__(self):
        self.__disciplines_list = []

    def search_discipline(self, discipline_id):
        idx = 0
        for other in self.__disciplines_list:
            if other.get_id() == discipline_id:
                return idx
            idx = idx + 1
        return -1

    def add_discipline(self, discipline):
        if self.search_discipline(discipline.get_id()) != -1:
            raise RepoError("Existing discipline!")
        self.__disciplines_list.append(discipline)

    def remove_discipline(self, discipline_id):
        if self.search_discipline(discipline_id) == -1:
            raise RepoError("Non-existing discipline!")
        del self.__disciplines_list[self.search_discipline(discipline_id)]

    def update_discipline(self, discipline_id, new_name):
        if self.search_discipline(discipline_id) == -1:
            raise RepoError("Non-existing discipline!")
        discipline = self.__disciplines_list[self.search_discipline(discipline_id)]
        discipline.set_name(new_name)

    def get_disciplines_list(self):
        return self.__disciplines_list


class GradeRepo:
    def __init__(self,student_repo,discipline_repo):
        self.__grades_list = []
        self.__discipline_repository = discipline_repo
        self.__student_repository = student_repo

    def search_grade(self,grade):
        idx = 0
        for other in self.__grades_list:
            if grade.grade_value() == other.grade_value() and grade.get_discipline_id() == other.get_discipline_id() \
                    and grade.get_student_id() == other.get_student_id():
                return idx
            idx = idx + 1
        return -1

    def add_grade_repo(self, grade):
        self.__grades_list.append(grade)

    def remove_grade(self,grade):
        if self.search_grade(grade) == -1 :
            raise RepoError("Non-existing grade!")
        del self.__grades_list[self.search_grade(grade)]

    def get_grades_list(self):
        return self.__grades_list




