from src.persistence.repositories import *
from src.business.services import *
from src.business.UndoRedo import *
from src.presentation.ui import *
from src.validation.validators import *
from src.domain.entities import *

repo_students = StudentRepo()
repo_disciplines = DisciplineRepo()
repo_grades = GradeRepo(repo_students, repo_disciplines)

service_students = StudentService(repo_students,repo_grades)
service_disciplines = DisciplineService(repo_disciplines,repo_grades)
service_grades = GradeService(repo_grades)
undo_redo = UndoRedo(service_students,service_disciplines,service_grades)

ui = Ui(service_students, service_disciplines, service_grades, undo_redo)
ui.run()
