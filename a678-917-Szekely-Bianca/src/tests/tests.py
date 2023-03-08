import unittest

from src.persistence.repositories import *
from src.business.services import *
from src.business.UndoRedo import *
from src.presentation.ui import *
from src.validation.validators import *
from src.domain.entities import *


test_repo_students = StudentRepo()
test_repo_disciplines = DisciplineRepo()
test_repo_grades = GradeRepo(test_repo_students, test_repo_disciplines)

test_service_students = StudentService(test_repo_students,test_repo_grades)
test_service_disciplines = DisciplineService(test_repo_disciplines,test_repo_grades)
test_service_grades = GradeService(test_repo_grades)


class TestStudentService(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_repo_grades = GradeRepo(test_repo_students, test_repo_disciplines)
        self.__test_repo_students = StudentRepo()
        self.__test_service_students = StudentService(test_repo_students,test_repo_grades)

    def test_add_student(self):
        self.__test_service_students.add_student(45, "Florea")
        self.assertEqual(len(self.__test_service_students.get_all_students()), 1)
        self.__test_service_students.add_student(99, "Dan")
        self.assertEqual(len(self.__test_service_students.get_all_students()), 2)
        students_list = self.__test_service_students.get_all_students()
        stud1 = students_list[0]
        stud2 = students_list[1]
        self.assertEqual(stud1.get_id(), 45)
        self.assertEqual(stud1.get_name(), "Florea")
        self.assertEqual(stud2.get_id(), 99)
        self.assertEqual(stud2.get_name(), "Dan")

    def test_update_student(self):
        self.__test_service_students.add_student(45, "Florea")
        self.assertEqual(len(self.__test_service_students.get_all_students()), 4)
        self.__test_service_students.update_student(45,"Mariana")
        students_list = self.__test_service_students.get_all_students()
        stud1 = students_list[0]
        self.assertEqual(stud1.get_id(), 45)
        self.assertEqual(stud1.get_name(), "Mariana")

    def test_remove_student(self):
        self.assertEqual(len(self.__test_service_students.get_all_students()), 2)
        self.__test_service_students.remove_student(99)
        self.assertEqual(len(self.__test_service_students.get_all_students()), 1)
        students_list = self.__test_service_students.get_all_students()
        stud1 = students_list[0]
        self.assertEqual(stud1.get_id(), 45)
        self.assertEqual(stud1.get_name(), "Florea")

    def test_search_stud_id(self):
        self.__test_service_students.add_student(2,"Roman")
        self.__test_service_students.add_student(9,"Mircea")
        students_list = self.__test_service_students.search_stud_id(45)
        self.assertEqual(students_list[0].get_id(), 45)
        self.assertEqual(students_list[0].get_name(), "Florea")
        students_list = self.__test_service_students.search_stud_id(9)
        self.assertEqual(students_list[0].get_id(), 9)
        self.assertEqual(students_list[0].get_name(), "Mircea")

    def test_search_stud_name(self):
        students_list = self.__test_service_students.search_stud_name("Ea")
        self.assertEqual(len(students_list),2)

    def tearDown(self) -> None:
        """
        Runs after all tests are completed
        """
        pass


class TestDisciplineService(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_repo_grades = GradeRepo(test_repo_students, test_repo_disciplines)
        self.__test_repo_disciplines = DisciplineRepo()
        self.__test_service_disciplines = DisciplineService(test_repo_disciplines,test_repo_grades)

    def test_add_discipline(self):
        self.__test_service_disciplines.add_discipline(5, "Math")
        self.assertEqual(len(self.__test_service_disciplines.get_all_disciplines()), 1)
        self.__test_service_disciplines.add_discipline(100, "Sport")
        self.assertEqual(len(self.__test_service_disciplines.get_all_disciplines()), 2)
        disciplines_list = self.__test_service_disciplines.get_all_disciplines()
        disc1 = disciplines_list[0]
        disc2 = disciplines_list[1]
        self.assertEqual(disc1.get_id(), 5)
        self.assertEqual(disc1.get_name(), "Math")
        self.assertEqual(disc2.get_id(), 100)
        self.assertEqual(disc2.get_name(), "Sport")

    def test_update_discipline(self):
        self.__test_service_disciplines.add_discipline(7, "English")
        self.assertEqual(len(self.__test_service_disciplines.get_all_disciplines()), 4)
        self.__test_service_disciplines.update_discipline(7,"Biology")
        disciplines_list = self.__test_service_disciplines.get_all_disciplines()
        disc1 = disciplines_list[0]
        self.assertEqual(disc1.get_id(), 5)
        self.assertEqual(disc1.get_name(), "Math")
        disc2 = disciplines_list[3]
        self.assertEqual(disc2.get_id(), 7)
        self.assertEqual(disc2.get_name(), "Biology")

    def test_remove_discipline(self):
        self.assertEqual(len(self.__test_service_disciplines.get_all_disciplines()), 2)
        self.__test_service_disciplines.remove_discipline(100)
        self.assertEqual(len(self.__test_service_disciplines.get_all_disciplines()), 1)
        disciplines_list = self.__test_service_disciplines.get_all_disciplines()
        disc1 = disciplines_list[0]
        self.assertEqual(disc1.get_id(), 5)
        self.assertEqual(disc1.get_name(), "Math")

    def test_search_disc_id(self):
        self.__test_service_disciplines.add_discipline(58, "Spanish")
        self.__test_service_disciplines.add_discipline(10, "English")
        disciplines_list = self.__test_service_disciplines.search_disc_id(10)
        self.assertEqual(disciplines_list[0].get_id(), 10)
        self.assertEqual(disciplines_list[0].get_name(), "English")

    def test_search_disc_name(self):
        disciplines_list = self.__test_service_disciplines.search_disc_name("iSh")
        self.assertEqual(len(disciplines_list), 2)

    def tearDown(self) -> None:
        """
        Runs after all tests are completed
        """
        pass


class TestGradeService(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_repo_students = StudentRepo()
        self.__test_repo_disciplines = DisciplineRepo()
        self.__test_repo_grades = GradeRepo(test_repo_students, test_repo_disciplines)
        self.__test_service_grades = GradeService(test_repo_grades)

    def test_add_grade(self):
        self.__test_service_grades.add_grade(10,5,9)
        self.assertEqual(len(self.__test_service_grades.get_all_grades()), 1)
        self.__test_service_grades.add_grade(1,4,7)
        self.assertEqual(len(self.__test_service_grades.get_all_grades()), 2)
        grades_list = self.__test_service_grades.get_all_grades()
        grade1 = grades_list[0]
        grade2 = grades_list[1]
        self.assertEqual(grade1.get_student_id(), 10)
        self.assertEqual(grade1.get_discipline_id(), 5)
        self.assertEqual(grade1.grade_value(), 9)
        self.assertEqual(grade2.get_student_id(), 1)
        self.assertEqual(grade2.get_discipline_id(), 4)
        self.assertEqual(grade2.grade_value(), 7)

    def test_failing_stud(self):
        self.__test_service_grades.add_grade(100, 7, 2)
        self.__test_service_grades.add_grade(3, 8, 5)
        self.__test_service_grades.add_grade(6, 1, 4)
        grades_list = self.__test_service_grades.failing_stud()
        self.assertEqual(len(grades_list),2)

    def test_best_stud(self):
        self.__test_service_grades.add_grade(100, 7, 2)
        self.__test_service_grades.add_grade(3, 8, 6)
        self.__test_service_grades.add_grade(6, 1, 4)
        stud_list = self.__test_service_grades.best_stud()
        self.assertEqual(stud_list[0], 10)
        self.assertEqual(stud_list[1], 1)
        self.assertEqual(stud_list[len(stud_list)-1], 100)

    def test_discipline_grade(self):
        discipline_list = self.__test_service_grades.discipline_grade()
        self.assertEqual(discipline_list[0], 5)
        self.assertEqual(discipline_list[1], 4)
        self.assertEqual(discipline_list[len(discipline_list) - 1], 7)


    def tearDown(self) -> None:
        """
        Runs after all tests are completed
        """
        pass

class TestUndoRedo(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_service_students = test_service_students
        self.__test_service_disciplines = test_service_disciplines
        self.__test_service_grades = test_service_grades
        self.__test_undo = []
        self.__test_redo = []
        self.__test_undo_redo = UndoRedo(test_service_students,test_service_disciplines,test_service_grades)

    def test_undo_redo(self):
        self.__test_service_students.get_all_students().clear()
        self.__test_service_students.add_student(12,"Marcela")
        self.__test_undo_redo.remove_student(12,"Marcela")
        self.__test_service_students.add_student(50, "Popescu")
        self.__test_undo_redo.remove_student(50, "Popescu")
        self.assertEqual(len(test_service_students.get_all_students()),2)
        self.__test_undo_redo.undo()
        self.assertEqual(len(test_service_students.get_all_students()),1)
        self.__test_undo_redo.redo()
        self.assertEqual(len(test_service_students.get_all_students()), 2)

        stud = self.__test_service_students.search_stud_id(12)
        name = stud[0].get_name()
        self.__test_service_students.remove_student(12)
        self.__test_undo_redo.add_student(12, name)
        self.assertEqual(len(test_service_students.get_all_students()), 1)
        self.__test_undo_redo.undo()
        self.assertEqual(len(test_service_students.get_all_students()), 2)
        self.__test_undo_redo.redo()
        self.assertEqual(len(test_service_students.get_all_students()), 1)

        self.__test_undo_redo.undo()
        self.__test_service_students.add_student(12, "Marcela")
        self.__test_undo_redo.update_student(12, "Marius")
        self.__test_service_students.update_student(12,"Marius")
        self.assertEqual(len(test_service_students.get_all_students()), 3)
        self.__test_undo_redo.undo()
        stud = self.__test_service_students.search_stud_id(12)
        self.assertEqual(stud[0].get_name(), "Marius")
        self.__test_undo_redo.redo()
        self.assertEqual(stud[0].get_name(), "Marius")







    def tearDown(self) -> None:
        """
        Runs after all tests are completed
        """
        pass