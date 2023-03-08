from src.domain.entities import  Student, Discipline, Grade
from src.validation.validators import StudentValidator, DisciplineValidator, GradeValidator


class StudentService:
    def __init__(self, repo_student,repo_grade):
        self.__repo_student = repo_student
        self.__repo_grade = repo_grade

    def init_students(self):
        name = ["Andrei Balcescu", "Andreea Pop", "Adela Petrescu", "Viorel Drimus", "Remus Rus", "Florin Moldovan",
                "Sebastian Joicaliuc",
                "Raul Treista", "Mariana Stan", "Ionela Teleptean", "Rares Simedrea", "Cosmin Ardelean", "Vasile Osan",
                "Alex Velea",
                "Catalin Bolo", "Petrisor Vlad", "Florin Boc", "Emilia Mutu", "Ioana Ieudean", "Mark Zoltan"]
        for i in range(20):
            self.__repo_student.add_student(Student(i + 1, name[i]))

    def add_student(self, id_student, name):
        student = Student(id_student, name)
        StudentValidator.validate_student(student)
        self.__repo_student.add_student(student)

    def remove_student(self, id_student):
        self.__repo_student.remove_student(id_student)
        grades_list = self.__repo_grade.get_grades_list()
        for grade in grades_list:
            if int(grade.get_student_id()) == int(id_student):
                self.__repo_grade.remove_grade(grade)

    def update_student(self, id_student, name):
        student = Student(id_student, name)
        StudentValidator.validate_student(student)
        self.__repo_student.update_student(id_student, name)

    def get_all_students(self):
        return self.__repo_student.get_students_list()

    def search_stud_id(self, id):
        self._stud_list_id = []
        for stud in self.__repo_student.get_students_list():
            if stud.get_id() == id:
                self._stud_list_id.append(stud)
        return self._stud_list_id

    def search_stud_name(self, word):
        self._stud_list_name = []
        for stud in self.__repo_student.get_students_list():
            if word.lower() in stud.get_name().lower():
                self._stud_list_name.append(stud)
        return self._stud_list_name




class DisciplineService:

    def __init__(self, repo_discipline, repo_grade):
        self.__repo_discipline = repo_discipline
        self.__repo_grade = repo_grade

    def init_disciplines(self):
        name = ["Math", "Computer System Architecture", "Algebra", "Calculus", "Computational Logic",
                "Fundamentals of Programming", "Sport", "Physics", "Chemistry", "English", "Romanian", "Biology"]
        for i in range(12):
            self.__repo_discipline.add_discipline(Discipline(i + 1, name[i]))

    def add_discipline(self, id_discipline, name):
        discipline = Discipline(id_discipline, name)
        DisciplineValidator.validate_discipline(discipline)
        self.__repo_discipline.add_discipline(discipline)

    def remove_discipline(self, id_discipline):
        self.__repo_discipline.remove_discipline(id_discipline)
        grades_list = self.__repo_grade.get_grades_list()
        for grade in grades_list:
            if int(grade.get_discipline_id()) == int(id_discipline):
                self.__repo_grade.remove_grade(grade)

    def update_discipline(self, id_discipline,name):
        discipline = Discipline(id_discipline, name)
        DisciplineValidator.validate_discipline(discipline)
        self.__repo_discipline.update_discipline(id_discipline,name)

    def get_all_disciplines(self):
        return self.__repo_discipline.get_disciplines_list()

    def search_disc_id(self, id):
        self._disc_list_id = []
        for disc in self.__repo_discipline.get_disciplines_list():
            if disc.get_id() == id:
                self._disc_list_id.append(disc)
        return self._disc_list_id

    def search_disc_name(self, word):
        self._disc_list_name = []
        for disc in self.__repo_discipline.get_disciplines_list():
            if word.lower() in disc.get_name().lower():
                self._disc_list_name.append(disc)
        return self._disc_list_name


class GradeService:
    def __init__(self,repo_grade):
        self.__repo_grade = repo_grade

    def init_grades(self):
        id_stud = [11, 2, 3, 4, 11, 9, 2, 6, 1, 8]
        id_disc = [9, 10, 4, 2, 3, 1, 10, 7, 2, 11]
        grade_value = [10, 5, 7, 3, 6, 10, 4, 3, 9, 4]
        for i in range(10):
            grade = Grade(id_stud[i], id_disc[i], grade_value[i])
            self.__repo_grade.add_grade_repo(grade)

    def add_grade(self, student_id, discipline_id, grade_value):
        grade = Grade(student_id, discipline_id, grade_value)
        GradeValidator.validate_grade(grade)
        self.__repo_grade.add_grade_repo(grade)

    def remove_grade(self,student_id, discipline_id, grade_value):
        grade = Grade(student_id, discipline_id, grade_value)
        self.__repo_grade.remove_grade(grade)

    def get_all_grades(self):
        return self.__repo_grade.get_grades_list()

    def failing_stud(self):
        self._stud_list = []
        grades = self.__repo_grade.get_grades_list()
        for i in range(0, len(grades)):
            x=1
            average = int(grades[i].grade_value())
            for j in range(i+1, len(grades)):
                if grades[i].get_discipline_id() == grades[j].get_discipline_id() and grades[i].get_student_id() == grades[j].get_student_id():
                    average += int(grades[j].grade_value())
                    x += 1
            if x != 0:
                if average/x < 5:
                    if grades[i].get_student_id() not in self._stud_list:
                        self._stud_list.append(grades[i].get_student_id())
        return self._stud_list

    def best_stud(self):
        aggregate_average = []
        id_aggregate_average =[]
        grades = self.__repo_grade.get_grades_list()
        for i in range(0, len(grades)):
            aggregate = int(grades[i].grade_value())
            x=1
            for j in range(i + 1, len(grades)):
                if grades[i].get_student_id() == grades[j].get_student_id():
                    aggregate += int(grades[j].grade_value())
                    x+=1
            if grades[i].get_student_id() not in id_aggregate_average:
                aggregate_average.append(aggregate / x)
                id_aggregate_average.append(grades[i].get_student_id())
        aggregate_average, id_aggregate_average = self.sorted_list(aggregate_average, id_aggregate_average)
        return id_aggregate_average

    def sorted_list(self, list1,list2):
        for i in range(len(list1)):
            for j in range(i + 1, len(list1)):
                if list1[i] < list1[j]:
                    list2 = self.swap(list2,i,j)
                    list1 = self.swap(list1, i, j)
        return list1,list2

    def swap(self,list,x1,x2):
        aux = list[x1]
        list[x1] = list[x2]
        list[x2] = aux
        return list

    def discipline_grade(self):
        discipline_list = []
        average_grade =[]
        grades = self.__repo_grade.get_grades_list()
        for i in range(0, len(grades)):
            x = 1
            average = int(grades[i].grade_value())
            for j in range(i + 1, len(grades)):
                if grades[i].get_discipline_id() == grades[j].get_discipline_id():
                    average += int(grades[j].grade_value())
                    x += 1
            if grades[i].get_discipline_id() not in discipline_list:
                average_grade.append(average / x)
                discipline_list.append(grades[i].get_discipline_id())
        average_grade, discipline_list = self.sorted_list(average_grade, discipline_list)
        return discipline_list
