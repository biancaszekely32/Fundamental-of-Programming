"""main"""
from repository.repo import Repository
from services.service import Service
from ui.ui import UI

file_name = "sentences.txt"

"""create repository"""
repo = Repository(file_name)

"""create service"""
service = Service(repo)

"""create ui"""
ui = UI(service, repo)

ui.boot_up()







