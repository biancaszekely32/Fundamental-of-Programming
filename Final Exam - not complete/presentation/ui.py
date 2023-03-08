from service.service import *

class Ui:
    def __init__(self,service):
        self.__service = service

    def start(self):
        board = self.__service.get_board()
        print(board)
        while True:
            end_game = self.__service.check_end_game()
            if end_game == True:
                print("You lost!")
                return
            print("Order makes move")
            x,y= self.__service.place_computer()
            symbol = self.__service.choose_symbol()
            self.__service.make_move(x, y, symbol)
            print("Computer moved at (" + str(x+1) + ", " + str(y+1) + ", " + str(symbol) + ")")
            print(self.__service.get_board())
            print()
            print("It's your turn!")
            try:
                symbol = str(input("Please pick which symbol would you like to use: ")).strip()
                x = int(input("Introduce the number of the row (between 1-6): "))
                y = int(input("Introduce the number of the column (between 1-6): "))
                x=x-1
                y=y-1
            except ValueError:
                    print("Invalid input!")
            try:
                self.__service.make_move(x,y,symbol)
                print("Player moved at (" + str(x+1) + ", " + str(y+1) + ", " + str(symbol) + ")")
                print(self.__service.get_board())
                if self.__service.full_board_serv() == True:
                    print("You won!")
                    return
            except ServiceError:
                print("You can't move there!")
