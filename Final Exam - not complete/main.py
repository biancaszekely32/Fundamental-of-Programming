from board.board import *
from service.service import *
from presentation.ui import *

board = Board()
service = Service(board)
ui = Ui(service)
ui.start()
