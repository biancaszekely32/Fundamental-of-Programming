from board.board import *
class ServiceError(Exception):
    pass

class Service:
    def __init__(self,board):
        self.__board = board

    def get_board(self):
        return self.__board.get_board_str()

    def make_move(self,x,y,symbol):
        if self.__board.valid_move(x,y) == True and self.__board.valid_symbol(symbol) == True:
            self.__board.set_board(x, y, symbol)
        else:
            raise ServiceError("Invalid input!")

    def place_computer(self):
        good_x = 0
        good_y = 0
        max_neighbour = -1
        for x in range(0,6):
            for y in range(0,6):
                if self.__board.valid_move(x, y) == True:
                    neighbour = self.__board.find_neighbours(x, y)
                    if neighbour > max_neighbour:
                        max_neighbour = neighbour
                        good_x = x
                        good_y = y
        return [good_x, good_y]


    def check_end_game(self):
        for x in range(0,6):
            for y in range(0,6):
                return self.__board.end_game(x, y)

    def choose_symbol(self):
        return self.__board.choose()

    def full_board_serv(self):
        return self.__board.full_board()
