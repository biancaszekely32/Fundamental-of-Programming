from src.errors.errors import RepoError, ValidError, UndoError

class Ui:
    def __init__(self, service_students, service_disciplines, service_grades,undo_redo):
        self.__service_students = service_students
        self.__service_disciplines = service_disciplines
        self.__service_grades = service_grades
        self.__undo_redo = undo_redo

    def print_menu(self):
        print("Available menu: ")
        print("1 - add")
        print("2 - remove")
        print("3 - update")
        print("4 - grade one student")
        print("5 - list")
        print("6 - search ")
        print("7 - statistics")
        print("8 - undo/redo")
        print("0 - exit")


    def run(self):
        self.__service_disciplines.init_disciplines()
        self.__service_students.init_students()
        self.__service_grades.init_grades()
        while True:
            self.print_menu()
            cmd = input("Enter a command: ").strip()
            if cmd == "0":
                return
            if cmd == "":
                continue
            if cmd == "1":
                cmd1 = input("What would you like to add:\n 1.Student \n 2.Discipline  :  ")
                if cmd1 == "1":
                    try:
                        self.__ui_add_student()
                    except ValidError as ve:
                        print(ve)
                    except RepoError as re:
                        print(re)
                elif cmd1 == "2":
                    try:
                        self.__ui_add_discipline()
                    except ValidError as ve:
                        print(ve)
                    except RepoError as re:
                        print(re)
                else:
                    print("  Option not available")
            elif cmd == "2":
                cmd1 = input("What would you like to remove:\n 1.Student \n 2.Discipline  :  ")
                if cmd1 == "1":
                    try:
                        self.__ui_remove_student()
                    except ValidError as ve:
                        print(ve)
                    except RepoError as re:
                        print(re)
                elif cmd1 == "2":
                    try:
                        self.__ui_remove_discipline()
                    except ValidError as ve:
                        print(ve)
                    except RepoError as re:
                        print(re)
                else:
                    print("  Option not available")
            elif cmd == "3":
                cmd1 = input("What would you like to update:\n 1.Student \n 2.Discipline  :  ")
                if cmd1 == "1":
                    try:
                        self.__ui_update_student()
                    except ValidError as ve:
                        print(ve)
                    except RepoError as re:
                        print(re)
                elif cmd1 == "2":
                    try:
                        self.__ui_update_discipline()
                    except ValidError as ve:
                        print(ve)
                    except RepoError as re:
                        print(re)
                else:
                    print("  Option not available")
            elif cmd == "4":
                try:
                    self.__ui_add_grade()
                except ValidError as ve:
                    print(ve)
                except RepoError as re:
                    print(re)
            elif cmd == "5":
                cmd1 = input("What would you like to print:\n 1.Students \n 2.Disciplines \n 3.Grades :  ")
                if cmd1 == "1":
                    self.__ui_print_students()
                elif cmd1 == "2":
                    self.__ui_print_disciplines()
                elif cmd1 == "3":
                    self.__ui_print_grades()
                else:
                    print("  Option not available")
            elif cmd == "6":
                cmd1 = input("What would you like to base your search on:\n 1.Id \n 2.Name  :  ")
                if cmd1 == "1":
                    cmd2 = input("What would you like to search for based on Id:\n 1.Students \n 2.Disciplines  :  ")
                    if cmd2 == "1":
                        try:
                            self.__ui_search_stud_id()
                        except ValidError as ve:
                            print(ve)
                        except RepoError as re:
                            print(re)
                    elif cmd2 == "2":
                        try:
                            self.__ui_search_disc_id()
                        except ValidError as ve:
                            print(ve)
                        except RepoError as re:
                            print(re)
                    else:
                        print("  Option not available")
                elif cmd1 == "2":
                    cmd3 = input("What would you like to search for based on Name:\n 1.Students \n 2.Disciplines  :  ")
                    if cmd3 == "1":
                        try:
                            self.__ui_search_stud_name()
                        except ValidError as ve:
                            print(ve)
                        except RepoError as re:
                            print(re)
                    elif cmd3 == "2":
                        try:
                            self.__ui_search_disc_name()
                        except ValidError as ve:
                            print(ve)
                        except RepoError as re:
                            print(re)
                    else:
                        print("  Option not available")
                else:
                    print("  Option not available")
            elif cmd == "7":
                cmd1= input("What statistics would you like to see: \n 1.Failing Students \n 2.Students with the best "
                            "school situation \n 3.Disciplines at which there is at least one grade  :  ")
                if cmd1 == "1":
                    self.__ui_failing_students()
                elif cmd1 == "2":
                    self.__ui_best_students()
                elif cmd1 == "3":
                    self.__ui_disciplines_grades()
                else:
                    print("  Option not available")
            elif cmd == "8":
                cmd1= input("What would you like to do: \n 1.Undo \n 2.Redo  :")
                if cmd1 == "1":
                    try:
                        self.__undo_redo.undo()
                        print("  Undo done successfully!")
                    except ValidError as ve:
                        print(ve)
                    except RepoError as re:
                        print(re)
                    except UndoError as ue:
                        print(ue)
                elif cmd1 == "2":
                    try:
                        self.__undo_redo.redo()
                        print("  Redo done successfully!")
                    except ValidError as ve:
                        print(ve)
                    except RepoError as re:
                        print(re)
                    except UndoError as ue:
                        print(ue)
                else:
                    print("  Option not available")
            else:
                print("Invalid command!")

    def __ui_add_student(self):
        try:
            id_student = int(input("Student ID: "))
        except ValueError:
            print("Invalid student id!")
            return
        try:
            name = input("Student Name: ")
        except ValueError:
            print("Invalid student name!")
            return
        self.__service_students.add_student(id_student, name)
        self.__undo_redo.remove_student(id_student,name)
        print("Student added successfully!")

    def __ui_remove_student(self):
        try:
            id_student = int(input("Student ID: "))
        except ValueError:
            print("Invalid student id!")
            return
        """
        grades_list = self.__service_grades.get_all_grades        for grade in grades_list:
            if int(grade.get_student_id()) == int(id_student):
                discipline_id = grade.get_discipline_id()
                grade_value = grade.grade_value()
                self.__undo_redo.add_grade(id_student, discipline_id, grade_value)"""
        stud = self.__service_students.search_stud_id(id_student)
        name = stud[0].get_name()
        self.__undo_redo.add_student(id_student, name)
        self.__service_students.remove_student(id_student)
        print("Student removed successfully!")

    def __ui_update_student(self):
        try:
            id_student = int(input("Student ID: "))
        except ValueError:
            print("Invalid student id!")
            return
        try:
            name = input("Student Name: ")
        except ValueError:
            print("Invalid student name!")
            return
        stud = self.__service_students.search_stud_id(id_student)
        self.__undo_redo.update_student(id_student, stud[0].get_name())
        self.__service_students.update_student(id_student, name)
        print("Student updated successfully!")

    def __ui_print_students(self):
        students = self.__service_students.get_all_students()
        if len(students) == 0:
            print("Empty students list!")
            return
        for student in students:
            print(student)

    def __ui_add_discipline(self):
        try:
            id_discipline = int(input("Discipline ID: "))
        except ValueError:
            print("Invalid Discipline id!")
            return
        try:
            name = input("Discipline Name: ")
        except ValueError:
            print("Invalid discipline name!")
            return
        self.__service_disciplines.add_discipline(id_discipline, name)
        self.__undo_redo.remove_discipline(id_discipline, name)
        print("Discipline added successfully!")

    def __ui_remove_discipline(self):
        try:
            id_discipline = int(input("Discipline ID: "))
        except ValueError:
            print("Invalid Discipline id!")
            return
        """
        grades_list = self.__service_grades.get_all_grades()
        for grade in grades_list:
            if int(grade.get_discipline_id()) == int(id_discipline):
                id_student = grade.get_student_id()
                grade_value = grade.grade_value()
                self.__undo_redo.add_grade(id_student, id_discipline, grade_value)"""
        name = self.__service_disciplines.search_disc_id(id_discipline)[0].get_name()
        self.__service_disciplines.remove_discipline(id_discipline)
        self.__undo_redo.add_discipline(id_discipline, name)
        print("Discipline removed successfully!")

    def __ui_update_discipline(self):
        try:
            id_discipline = int(input("Discipline ID: "))
        except ValueError:
            print("Invalid Discipline id!")
            return
        try:
            name = input("Discipline Name: ")
        except ValueError:
            print("Invalid discipline name!")
            return
        disc = self.__service_disciplines.search_disc_id(id_discipline)
        self.__undo_redo.update_discipline(id_discipline, disc[0].get_name())
        self.__service_disciplines.update_discipline(id_discipline, name)
        print("Discipline updated successfully!")

    def __ui_print_disciplines(self):
        disciplines = self.__service_disciplines.get_all_disciplines()
        if len(disciplines) == 0:
            print("Empty disciplines list!")
            return
        for discipline in disciplines:
            print(discipline)

    def __ui_add_grade(self):
        try:
            id_student = int(input("Student ID: "))
        except ValueError:
            print("Invalid Student id!")
            return
        try:
            id_discipline = int(input("Discipline ID: "))
        except ValueError:
            print("Invalid discipline id!")
            return
        try:
            grade_value = int(input("Grade Value: "))
        except ValueError:
            print("Invalid grade value!")
            return
        self.__undo_redo.remove_grade(id_student, id_discipline,grade_value)
        self.__service_grades.add_grade(id_student, id_discipline,grade_value)
        print("Grade added successfully!")

    def __ui_print_grades(self):
        grades = self.__service_grades.get_all_grades()
        if len(grades) == 0:
            print("Empty grades list!")
            return
        for grade in grades:
            print(grade)

    def __ui_search_stud_id(self):
        try:
            id_student = int(input("Student ID: "))
        except ValueError:
            print("Invalid Student id!")
            return
        students = self.__service_students.search_stud_id(id_student)
        for stud in students:
            print(stud)

    def __ui_search_stud_name(self):
        try:
            word = input("Student Name: ")
        except ValueError:
            print("Invalid student name!")
            return
        students = self.__service_students.search_stud_name(word)
        for stud in students:
            print(stud)

    def __ui_search_disc_id(self):
        try:
            id_discipline = int(input("Discipline ID: "))
        except ValueError:
            print("Invalid Discipline id!")
            return
        disciplines = self.__service_disciplines.search_disc_id(id_discipline)
        for disc in disciplines:
            print(disc)

    def __ui_search_disc_name(self):
        try:
            word = input("Discipline Name: ")
        except ValueError:
            print("Invalid Discipline name!")
            return
        disciplines = self.__service_disciplines.search_disc_name(word)
        for disc in disciplines:
            print(disc)

    def __ui_failing_students(self):
        fails = self.__service_grades.failing_stud()
        students_failing =[]
        if len(fails) == 0:
            print("There is no failing student!")
            return
        for fail in fails:
            students_failing += self.__service_students.search_stud_id(fail)
        print("The failing students are: ")
        for stud in students_failing:
            print(stud)

    def __ui_best_students(self):
        bestt = self.__service_grades.best_stud()
        best_students = []
        for best in bestt:
            best_students += self.__service_students.search_stud_id(best)
        print("The best students are:")
        for stud in best_students:
            print(stud)

    def __ui_disciplines_grades(self):
        discipline = self.__service_grades.discipline_grade()
        all_disc = []
        for disc in discipline:
            all_disc += self.__service_disciplines.search_disc_id(disc)
        print("The disciplines with at least one grade are: ")
        for one_disc in all_disc:
            print(one_disc)


