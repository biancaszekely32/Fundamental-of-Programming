class Board:
    def __init__(self):
        self._board = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],]

    def set_board(self,x,y,value):
        if x>=0 and x<=5 and y>=0 and y<=5:
            self._board[x][y] = value

    def get_board_str(self):
        board_str = ""
        for row in self._board:
            row_str = "|"
            for el in row:
                row_str =  row_str +str(el) +"|"
            board_str = board_str +row_str +"\n"
        return board_str

    def valid_move(self,x,y):
        if x<= 5  and y<= 5 and x>=0 and y>= 0 and self._board[x][y] == " ":
            return True
        else:
            return False

    def valid_symbol(self,symbol):
        if symbol == "X" or symbol == "O":
            return True
        else:
            return False

    def find_neighbours(self,x,y):
        neighbour = 0
        if x - 1 >= 0 and y - 1 >= 0 and x - 1 <= 5 and y - 1 <= 5 and self._board[x - 1][y - 1] == 'X':
            neighbour = neighbour + 1
        if x - 1 >= 0 and y >= 0 and x - 1 <= 5 and y <= 5 and self._board[x - 1][y] == 'X':
            neighbour = neighbour + 1
        if x - 1 >= 0 and y + 1 >= 0 and x - 1 <= 5 and y + 1 <= 5 and self._board[x - 1][y + 1] == 'X':
            neighbour = neighbour + 1
        if x + 1 >= 0 and y - 1 >= 0 and x + 1 <= 5 and y - 1 <= 5 and self._board[x + 1][y - 1] == 'X':
            neighbour = neighbour + 1
        if x + 1 >= 0 and y >= 0 and x + 1 <= 5 and y <= 5 and self._board[x + 1][y] == 'X':
            neighbour = neighbour + 1
        if x + 1 >= 0 and y + 1 >= 0 and x + 1 <= 5 and y + 1 <= 5 and self._board[x + 1][y + 1] == 'X':
            neighbour = neighbour + 1
        if x >= 0 and y + 1 >= 0 and x <= 5 and y + 1 <= 5 and self._board[x][y + 1] == 'X':
            neighbour = neighbour + 1
        if x >= 0 and y - 1 >= 0 and x <= 5 and y - 1 <= 5 and self._board[x][y - 1] == 'X':
            neighbour = neighbour + 1
        return neighbour

    def end_game(self,x,y):
        """
        we verify if each element from the table taken in a row,column or diagonal order is in a
         formation of 5 consecutive symbols of the same type
        :param x: row
        :param y: column
        :return: True if there are 5 consecutive symbols of the type in a row, column or diagonal order
        :return: False,otherwise
        """
        """
         if self._board[x][y] == "X" and self._board[x+1][y] == "X" and self._board[x+2][y] == "X" \
                and self._board[x+3][y] == "X" and self._board[x+4][y] == "X":
            return True
        if self._board[x-1][y] == "X" and self._board[x][y] == "X" and self._board[x+1][y] == "X" \
                and self._board[x+2][y] == "X" and self._board[x+3][y] == "X":
            return True
        if self._board[x-4][y] == "X" and self._board[x-3][y] == "X" and self._board[x-2][y] == "X" \
                and self._board[x-1][y] == "X" and self._board[x][y] == "X":
            return True
        if self._board[x+1][y] == "X" and self._board[x-3][y] == "X" and self._board[x-2][y] == "X" \
                and self._board[x-1][y] == "X" and self._board[x][y] == "X":
            return True
        if self._board[x][y] == "X" and self._board[x][y-1] == "X" and self._board[x][y-2] == "X" \
                and self._board[x][y] == "X" and self._board[x][y] == "X":
            return True
        if self._board[x][y] == "X" and self._board[x-1][y] == "X" and self._board[x-2][y] == "X" \
                and self._board[x+1][y] == "X" and self._board[x+2][y] == "X":
            return True
        """

        if self._board[x][y] == "X" and self._board[x-1][y] == "X" and self._board[x-2][y] == "X" \
                and self._board[x+1][y] == "X" and self._board[x+2][y] == "X":
            return True
        if self._board[x][y] == "O" and self._board[x][y-1] == "O" and self._board[x][y-2] == "O" \
                and self._board[x][y+1] == "O" and self._board[x][y+2] == "X":
            return True
        if self._board[x][y] == "O" and self._board[x-1][y-1] == "O" and self._board[x-2][y-2] == "O" \
                and self._board[x+1][y+1] == "O" and self._board[x+2][y+2] == "X":
            return True
        if self._board[x][y] == "O" and self._board[x-1][y] == "O" and self._board[x-2][y] == "O" \
                and self._board[x+1][y] == "O" and self._board[x+2][y] == "X":
            return True
        return False

    def choose(self):
        X=0
        O=0
        for i in range(0, 6):
            for j in range(0, 6):
                if self._board[i][j] == "X":
                    X+=1
                elif self._board[i][j] == "O":
                    O+=1
        if X >= O:
            return "X"
        else: return "O"

    def full_board(self):
        for i in range(0, 6):
            for j in range(0, 6):
                if self._board[i][j] == " ":
                    return False
        return True