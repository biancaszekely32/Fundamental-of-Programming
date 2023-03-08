from src.domain.entities import  Student, Discipline, Grade
from src.errors.errors import UndoError


class UndoRedo:
    def __init__(self, service_students, service_disciplines, service_grades):
        self.__service_students = service_students
        self.__service_disciplines = service_disciplines
        self.__service_grades = service_grades
        self.__undo = []
        self.__redo = []

    def add_student(self, student_id, name):
        student = Student(student_id, name)
        self.__undo.append(['student', 'add', student])

    def remove_student(self, student_id, name):
        student = Student(student_id, name)
        self.__undo.append(['student', 'remove', student])

    def update_student(self, student_id, name):
        student = Student(student_id, name)
        self.__undo.append(['student', 'update', student])

    def add_discipline(self, discipline_id, name):
        discipline = Discipline(discipline_id, name)
        self.__undo.append(['discipline', 'add', discipline])

    def remove_discipline(self, discipline_id, name):
        discipline = Discipline(discipline_id, name)
        self.__undo.append(['discipline', 'remove', discipline])

    def update_discipline(self, discipline_id, name):
        discipline = Discipline(discipline_id, name)
        self.__undo.append(['discipline', 'update', discipline])

    def add_grade(self,student_id, discipline_id, grade_value):
        grade = Grade(student_id, discipline_id, grade_value)
        self.__undo.append(['grade', 'add', grade])

    def remove_grade(self,student_id, discipline_id, grade_value):
        grade = Grade(student_id, discipline_id, grade_value)
        self.__undo.append(['grade', 'remove', grade])

    def undo(self):
        if len(self.__undo) == 0:
            raise UndoError("There is nothing to undo!")
        command = self.__undo[len(self.__undo) - 1]
        option = command[0]
        undo_command = command[1]
        entity = command[2]
        if option == 'student':
            if undo_command == 'remove':
                student_id = entity.get_id()
                self.__service_students.remove_student(student_id)
                self.__redo.append(['student', 'add', entity])
            elif undo_command == 'add':
                self.__service_students.add_student(entity.get_id(), str(entity.get_name()))
                self.__redo.append(['student', 'remove', entity])
            elif undo_command == "update":
                stud= self.__service_students.search_stud_id(entity.get_id())
                self.__redo.append(['student', 'update', stud[0]])
                self.__service_students.update_student(entity.get_id(), entity.get_name())
        elif option == 'discipline':
            if undo_command == 'remove':
                discipline_id = entity.get_id()
                self.__service_disciplines.remove_discipline(discipline_id)
                self.__redo.append(['discipline', 'add', entity])
            elif undo_command == 'add':
                self.__service_disciplines.add_discipline(entity.get_id(), entity.get_name())
                self.__redo.append(['discipline', 'remove', entity])
            elif undo_command == "update":
                disc = self.__service_disciplines.search_disc_id(entity.get_id())
                self.__redo.append(['discipline', 'update', disc[0]])
                self.__service_disciplines.update_discipline(entity.get_id(), entity.get_name())
        elif option == 'grade':
            if undo_command == 'add':
                self.__service_grades.add_grade(entity.get_student_id(), entity.get_discipline_id(),
                                                entity.grade_value())
                self.__redo.append(['grade', 'remove', entity])
            if undo_command == 'remove':
                self.__service_grades.remove_grade(entity.get_student_id(),entity.get_discipline_id(),entity.grade_value())
                self.__redo.append(['grade', 'add', entity])
        self.__undo.pop()

    def redo(self):
        if len(self.__redo) == 0:
            raise UndoError("There is nothing to redo!")
        command = self.__redo[len(self.__redo) - 1]
        option = command[0]
        redo_command = command[1]
        entity = command[2]
        if option == 'student':
            if redo_command == 'remove':
                student_id = entity.get_id()
                self.__service_students.remove_student(student_id)
                self.__undo.append(['student', 'add', entity])
            elif redo_command == 'add':
                self.__service_students.add_student(entity.get_id(), entity.get_name())
                self.__undo.append(['student', 'remove', entity])
            elif redo_command == "update":
                stud = self.__service_students.search_stud_id(entity.get_id())
                self.__undo.append(['student', 'update', stud[0]])
                self.__service_students.update_student(entity.get_id(), entity.get_name())
        elif option == 'discipline':
            if redo_command == 'remove':
                discipline_id = entity.get_id()
                self.__service_disciplines.remove_discipline(discipline_id)
                self.__undo.append(['discipline', 'add', entity])
            elif redo_command == 'add':
                self.__service_disciplines.add_discipline(entity.get_id(), entity.get_name())
                self.__undo.append(['discipline', 'remove', entity])
            elif redo_command == "update":
                disc = self.__service_disciplines.search_disc_id(entity.get_id())
                self.__undo.append(['discipline', 'update', disc[0]])
                self.__service_disciplines.update_discipline(entity.get_id(), entity.get_name())
        else:
            if redo_command == 'remove':
                self.__service_grades.remove_grade(entity.get_student_id(), entity.get_discipline_id(),
                                                entity.grade_value())
                self.__undo.append(['grade', 'add', entity])
            elif redo_command == 'add':
                self.__service_grades.add_grade(entity.get_student_id(), entity.get_discipline_id(),
                                                entity.grade_value())
                self.__undo.append(['grade', "remove", entity])
        self.__redo.pop()
