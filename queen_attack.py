class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        if (row < 0):
            raise ValueError ("row not positive")
        if (row > 7):
            raise ValueError ("row not on board")
        if (column < 0):
            raise ValueError ("column not positive")
        if (column > 7):
            raise ValueError ("column not on board")
        return

    def can_attack(self, another_queen):
        if ((self.row == another_queen.row) and (self.column == another_queen.column)):
            raise ValueError ("Invalid queen position: both queens in the same square")
        elif ((self.row - another_queen.row) == 0):
            return True
        elif ((self.column - another_queen.column) == 0):
            return True
        elif ((self.row - another_queen.row) == (self.column - another_queen.column)) or ((self.row - another_queen.row) == (another_queen.column - self.column)):
            return True
        else:
            return False
