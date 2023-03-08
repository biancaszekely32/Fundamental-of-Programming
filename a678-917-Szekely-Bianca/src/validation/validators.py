from src.errors.errors import ValidError


class StudentValidator:
    @staticmethod
    def validate_student(student):
        errors = ""
        if student.get_id() < 0:
            errors += "Student Id must be a positive integer!\n"
        if isinstance(student.get_name(), str) is False:
            errors += "Student Name must be a string!\n"
        if student.get_name() == "":
            errors += "Invalid name!\n"
        if len(errors):
            raise ValidError(errors)


class GradeValidator:
    @staticmethod
    def validate_grade(grade):
        errors = ""
        if grade.get_discipline_id() < 0:
            errors += "Discipline Id must be a positive integer!\n"
        if grade.get_student_id() < 0:
            errors += "Student Id must be a positive integer!\n"
        if grade.grade_value() < 0:
            errors += "Grade Value must be a positive integer!\n"
        if len(errors):
            raise ValidError(errors)


class DisciplineValidator:
    @staticmethod
    def validate_discipline(discipline):
        errors = ""
        if discipline.get_id() < 0:
            errors += "Discipline Id must be a positive integer!\n"
        if isinstance(discipline.get_name(), str) is False:
            errors += "Discipline Name must be a string!\n"
        if discipline.get_name() == "":
            errors += "Invalid name!\n"
        if len(errors):
            raise ValidError(errors)
