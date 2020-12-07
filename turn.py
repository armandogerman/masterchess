from random import randint

def position(i):                #esta funcion calcula la posicion enviada de la cadena y devuelve fila y columna
    for j in range(0, 16):
        colum = i - j * 16
        if colum < 16 and colum >= 0:
            return j,colum

def pieza_aliada(pa,co):
    if co=="white":
        if pa=="p" or pa=="r" or pa=="h" or pa=="b" or pa=="q" or pa=="k":
            return False
        return True
    if co=="black":
        if pa=="p" or pa=="r" or pa=="h" or pa=="b" or pa=="q" or pa=="k":
            return True
        return False

def pawneatw(mboard,actual_turn):
    i=0
    while i <= 255:
        if mboard[i] == 'P':
            if mboard[i-15] != ' ' and not(pieza_aliada(mboard[i-15],actual_turn)):  
                if position(i-15)[0] == position(i-16)[0]:
                    print("pawn: x+1,y+1",i)
                    return position(i), position(i-15)
            elif mboard[i-17] != ' ' and not(pieza_aliada(mboard[i-17],actual_turn)):
                if position(i-17)[0] == position(i-16)[0]:
                    print("pawn: x+1,y-1",i) 
                    return position(i), position(i-17)
        i += 1
    return None
def pawneatb(mboard,actual_turn):
    n=0
    while n <= 256:
        i = 255 - n
        if mboard[i] == 'p':
            if mboard[i+15] != ' ' and not(pieza_aliada(mboard[i+15],actual_turn)):
                if position(i+15)[0] == position(i+16)[0]:
                    print("pawn: x+1,y+1",i)
                    return position(i), position(i+15)
            elif mboard[i+17] != ' ' and not(pieza_aliada(mboard[i+17],actual_turn)):
                if position(i+17)[0] == position(i+16)[0]:
                    print("pawn: x+1,y-1",i) 
                    return position(i), position(i+17)
        n += 1
    return None
def pawneat(mboard,actual_turn):
    if actual_turn == "white":
        return pawneatw(mboard,actual_turn)
    elif actual_turn == "black":
        return pawneatb(mboard,actual_turn)
    return None
def pawnmove(mboard,actual_turn):
    if actual_turn == "white":
        i=0
        while i <= 256:
            if mboard[i] == 'P':
                if i > 191:
                    if mboard[i-32] == ' ':
                        if mboard[i-16] == ' ':
                            print("pawn: x+2,y",i)
                            return position(i), position(i-32)
                elif i <= 191:
                    print("pawn: x+1,y")
                    if mboard[i-16] == ' ':
                        return position(i),position(i-16)
            i += 1
    elif actual_turn == "black":
        n=0
        while n <= 255:
            i=255-n
            if mboard[i] == 'p':
                if i < 64:
                    if mboard[i+32] == ' ':
                        if mboard[i+16] == ' ':
                            print("pawn: x+2,y")                         
                            return position(i),position(i+32)
                elif i >= 64:
                    if mboard[i+16] == ' ':
                        print("pawn: x+1,y")
                        return position(i),position(i+16)
            n += 1
  
def select_pawn(actual_turn,mboard):
    if pawneat(actual_turn,mboard) != None:
        return pawneat(actual_turn, mboard)
    if pawnmove(actual_turn,mboard) != None and pawneat(actual_turn,mboard) == None:
       return pawnmove(actual_turn, mboard)
                   
def calc(actual_turn, mboard):
    if actual_turn == "black":
        print("hello black")
        fromto = select_pawn(actual_turn, mboard)
        return fromto
    else:
        print("hello white")
        fromto = select_pawn(actual_turn, mboard)
        return fromto


'''
def select_pawn(actual_turn,mboard):
    if actual_turn == "white":                                            #valido que sea blanco por la posicion de las piezas
        for i in range(256):                                              #recorro el tablero
            if mboard[i] == 'P':                                          #find white pawn
                if mboard[i-15] != ' ':
                    print("pawn: x+1,y+1")                                #reviso la posición (x+1,y+1) para ver si puedo comer algo
                    if position(i-15) == position(i-16):                  #valido si existe esa posicion o la pieza esta en una esquina y no puede comer en diagonal
                        return position(i), position(i-15)                #devuelvo posición  (x+1,y+1)
                elif mboard[i-17] != ' ':
                    print("pawn: x+1,y-1")                                #reviso la posición (x+1,y-1) para ver si puedo comer algo
                    if position(i-15) == position(i-16):                  #valido si existe esa posicion o la pieza esta en una esquina y no puede comer en diagonal
                        return position(i), position(i-17)                #devuelvo posición  (x+1,y-1)
                elif i > 191:
                    print("pawn: x+2,y")                                  #reviso que este en primera o segunda linea de peon para avanzar dos pasos
                    if mboard[i-32] == ' ':
                        if mboard[i-16] == ' ':                           #reviso que las casillas (x+1,y) y (x+2,y) estas libres
                            return position(i),position(i-32)
                elif i <= 191:
                    print("pawn: x+1,y")
                    return position(i),position(i-16)                     #devuelvo posición (x+1,y)
    if actual_turn == "black":                                            #valido que sea Negro por la posicion de las piezas
        for n in range(256):                                              #recorro el tablero
            i = 255 - n
            if mboard[i] == 'p':                                          #find black pawn
                if mboard[i+15] != ' ':
                    print("pawn: x+1,y-1")                                #reviso la posición (x+1,y-1) para ver si puedo comer algo
                    if position(i+15) == position(i+16):                  #valido si existe esa posicion o la pieza esta en una esquina y no puede comer en diagonal
                        return position(i), position(i+15)                #devuelvo posición  (x+1,y-1)
                elif mboard[i+17] != ' ':
                    print("pawn: x+1,y+1")                                #reviso la posición (x+1,y+1) para ver si puedo comer algo
                    if position(i+17) == position(i+16):                  #valido si existe esa posicion o la pieza esta en una esquina y no puede comer en diagonal
                        return position(i), position(i+17)                #devuelvo posición  (x+1,y+1)
                elif i < 64:
                    print("pawn: x+2,y")                                  #reviso que este en primera o segunda linea de peon para avanzar dos pasos
                    if mboard[i+32] == ' ':
                        if mboard[i+16] == ' ':                           #reviso que las casillas (x+1,y) y (x+2,y) estas libres
                            return position(i),position(i+32)
                elif i >= 64:
                    print("pawn: x+1,y")
                    return position(i),position(i+16)                     #devuelvo posición (x+1,y)
''' 

'''
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
       

def select_pawn(actual_turn,mboard):
    if actual_turn == "white":                                       #valido que sea blanco por la posicion de las piezas
        i = 0
        for i in mboard:                                             #recorro el tablero
            if mboard[i] == 'P':                                     #find white pawn
                if mboard[i-15] != ' ':                              #reviso la posición (x+1,y+1) para ver si puedo comer algo
                    return position(i), position(i-15)                            #devuelvo posición  (x+1,y+1)
                elif mboard[i-17] == ' ':                            #reviso la posición (x+1,y-1) para ver si puedo comer algo
                    return position(i), position(i-17)                            #devuelvo posición  (x+1,y-1)
                elif i > 191:                                        #reviso que este en primera o segunda linea de peon para avanzar dos pasos
                    if mboard[i-32] == ' ' and mboard[i-16] == ' ':  #reviso que las casillas (x+1,y) y (x+2,y) estas libres
                        return position(i), position(i-32)                        #devuelvo posición (x+2,y)
                elif i: return position(i), position(i-16)                        #devuelvo posición (x+1,y)
                                     

        if actual_turn == "black":
            pass

    pass

class Knight:
    pass

class Bishop:
    pass

class Queen:
    pass

class Rock:
    pass


def calc(actual_turn, mboard):
    #fromr, fromc, tor, toc = ''
    if actual_turn == "black":
        print("hello black")
        #fromr = int(3)
        fromc = int(randint(0, 15))
        #tor = int(5)
        #toc = int(fromc)
        #fromto = fromr, fromc, tor, toc
        fromto = int(3), fromc, int(5), fromc
        return fromto
    else:
        print("hello white")
        fromto = select_pawn(actual_turn, mboard)
        return fromto

'''