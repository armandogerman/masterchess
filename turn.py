

value = 0
chessCardinals = [(1,0),(0,1),(-1,0),(0,-1)]
chessDiagonals = [(1,1),(-1,1),(1,-1),(-1,-1)]

class Board:
    def __init__(self,data):
        pass

class Square:
    pass

class PieceSet:
    pass
'''
class Piece:
    def getPieceValue(self, piece):
        if(piece == None):
            return 0
        if piece == "P" or piece == "p":
            value = 10
        if piece == "H" or piece == "h":
            value = 30
        if piece == "B" or piece == "b":
            value = 40
        if piece == "R" or piece == "r":
            value = 60
        if piece == "Q" or piece == "q":
            value = 5
        if piece == 'K' or piece == 'k':
            value = 100
    return value
'''       
class Pawn:
    pass

class Knight:
    pass

class Bishop:
    pass

class Queen:
    pass

class Rock:
    pass
