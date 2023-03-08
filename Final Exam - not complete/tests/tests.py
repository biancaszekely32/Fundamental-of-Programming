from board.board import *
from service.service import *
from presentation.ui import *
import unittest


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.__board = Board()
        self.__board.set_board(1, 1, 'X')
        self.__board.set_board(0, 1, 'O')
        self.__board.set_board(1, 2, 'O')
        self.__board.set_board(2, 1, 'X')
        self.__board.set_board(2, 2, 'X')
        self.__board.set_board(2, 0, 'O')
        self.__board.set_board(3, 0, 'O')
        self.__board.set_board(3, 3, 'O')
        self.__board.set_board(2, 3, 'X')
        self.__board.set_board(3, 1, 'X')
        self.__board.set_board(3, 2, 'X')
        self.__board.set_board(4, 1, 'X')
        self.__board.set_board(4, 2, 'O')
        self.__board.set_board(4, 4, 'X')
        self.__board.set_board(5, 1, 'X')
        print(self.__board.get_board_str())
        """
| |O| | | | |
| |X|O| | | |
|O|X|X|X| | |
|O|X|X|O| | |
| |X|O| |X| |
| |X| | | | | 
        """

    def test_end_game(self):
        self.assertEqual(self.__board.end_game(3, 1),True)
        #self.assertEqual(self.__board.end_game(1,1), True)
        self.assertEqual(self.__board.end_game(0,0), False)
        self.assertEqual(self.__board.end_game(3,2 ), False)


