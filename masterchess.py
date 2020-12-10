import asyncio
import json
from random import randint
import sys
import websockets

def position(i):                #esta funcion calcula la posicion enviada de la cadena y devuelve fila y columna
    for j in range(0, 16):
        colum = i-(j*16)
        if colum<16 and colum>=0:
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
def pawnmove(mboard,actual_turn):
    if actual_turn == "white":
        i=143
        while i<=255:
            if mboard[i] == 'P':
                if i>191:
                    if mboard[i-32] == ' ':
                        if mboard[i-16] == ' ':
                            return position(i), position(i-32)
                elif i<=191:
                    if mboard[i-16] == ' ':
                        return position(i),position(i-16)
            i+=1
    elif actual_turn == "black":
        n=143
        while n<=255:
            i=255-n
            if mboard[i] == 'p':
                if i < 64:
                    if mboard[i+32] == ' ':
                        if mboard[i+16] == ' ':
                            return position(i),position(i+32)
                elif i >= 64:
                    if mboard[i+16] == ' ':
                        return position(i),position(i+16)
            n+=1
def pawneat(mboard,actual_turn):
    if actual_turn == "white":
        i=0
        while i<=255:
            if mboard[i] == 'P':
                if mboard[i-15] != ' ':
                    if (pieza_aliada(mboard[i-15],actual_turn)):
                        i=257
                    elif not(pieza_aliada(mboard[i-15],actual_turn)):  
                        if position(i-15)[0] == position(i-16)[0]:
                            print("pawn: x+1,y+1",i)
                            return position(i), position(i-15)
                elif mboard[i-17] != ' ':
                    if (pieza_aliada(mboard[i-17],actual_turn)):
                        i=257
                    elif not(pieza_aliada(mboard[i-17],actual_turn)):
                        if position(i-17)[0] == position(i-16)[0]:
                            print("pawn: x+1,y-1",i) 
                            return position(i), position(i-17)
            elif i>=247:
                return None            
            i+=1
        return None
    elif actual_turn == "black":
        n=100
        while n<=256:
            i=256-n
            if mboard[i] == 'p':
                if mboard[i+17] != ' ':
                    if (pieza_aliada(mboard[i+17],actual_turn)):
                        n=257
                    elif not(pieza_aliada(mboard[i+17],actual_turn)):
                        if position(i+17)[0] == position(i+16)[0]:
                            return position(i), position(i+17)
                elif mboard[i+15] != ' ':
                    if(pieza_aliada(mboard[i+15],actual_turn)):
                        n=257    
                    elif not(pieza_aliada(mboard[i+15],actual_turn)):
                        if position(i+15)[0] == position(i+16)[0]:
                            return position(i), position(i+15)
                elif i+17>=256:
                    return None
            n+=1
 
def select_pawn(mboard,actual_turn):
    if pawneat(mboard,actual_turn) != None:
        return pawneat(mboard,actual_turn)
    elif pawnmove(mboard,actual_turn) != None and pawneat(mboard,actual_turn) == None:
        return pawnmove(mboard,actual_turn)
# rooks and queens: horizontal and vertical moves
def rookmovehwleft(mboard,actual_turn):
    if actual_turn == "white":
        #rook move horizontal line
        i=0
        while i<=255:
            if mboard[i] == 'R' or mboard[i] =='Q':
                n=0
                while n<=16:
                    if (i-n)<=255 and (i-n)>=0:
                        if mboard[i] != ' ':
                            if pieza_aliada(mboard[i-n],actual_turn):
                                i=257
                                n=17
                            elif not pieza_aliada(mboard[i-n],actual_turn):
                                if position(i-n)[0] == position(i-n)[0]:
                                    return position(i), position(i-n)
                        i=255
                        return None       
                    n+=1
            i+=1
def rookmovehwright(mboard,actual_turn):
    if actual_turn == "white":
        #rook move horizontal line
        i=0
        while i<=255:
            if mboard[i] == 'R' or mboard[i] =='Q':
                n=0
                while n<=16:
                    if (i+n)<=255 and (i+n)>=0:
                        if mboard[i+n] != ' ':
                            if pieza_aliada(mboard[i+n],actual_turn):
                                i=257
                                n=17    
                            elif not(pieza_aliada(mboard[i+n],actual_turn)):
                                if position(i)[0] == position(i+n)[0]:
                                    return position(i), position(i+n)
                        i=255
                        return None       
                    n+=1
            i+=1
def rookmovehw(mboard,actual_turn):
    if rookmovehwleft(mboard,actual_turn) !=None:
        return rookmovehwleft(mboard,actual_turn)
    elif rookmovehwright(mboard,actual_turn) != None:
        return rookmovehwright(mboard,actual_turn)

def rookmovehbleft(mboard,actual_turn):
    if actual_turn == "black":
        #rook move horizontal line
        j=0
        while j<=255:
            i=255-j
            if mboard[i] =='r' or mboard[i] =='q':
                n=0
                while n<=16:
                    if (i-n)<=256 and (i-n)>=0:
                        if mboard[i-n] != ' ':
                            if pieza_aliada(mboard[i-n],actual_turn):
                                i=257
                                n=17
                            elif not(pieza_aliada(mboard[i-n],actual_turn)): #verifico a la izq
                                if position(i-n)[0] == position(i-n)[0]:
                                    return position(i), position(i-n)
                        j=255
                        return None       
                    n+=1
            j+=1
def rookmovehbright(mboard,actual_turn):
    if actual_turn == "black":
        #rook move horizontal line
        j=0
        while j<=255:
            i=255-j
            if mboard[i] =='r' or mboard[i] =='q':
                n=0
                while n<=16:
                    if (i+n)<=256 and (i+n)>=0:
                        if mboard[i+n] != ' ':
                            if pieza_aliada(mboard[i+n],actual_turn):
                                i=257
                                n=17       
                            elif not(pieza_aliada(mboard[i+n],actual_turn)):
                                if position(i)[0] == position(i+n)[0]:
                                    if mboard[i] == 'R' or mboard[i] == 'r':
                                        print("rookmovehbright rook: x+",i,"y+",n)
                                    if mboard[i] == 'Q' or mboard[i] == 'q':
                                        print("rookmovehbright queen: x+",i,"y+",n)
                                    return position(i), position(i+n)
                        j = 255
                        return None       
                    n += 1
            j += 1
def rookmovehb(mboard,actual_turn):
    if rookmovehbleft(mboard,actual_turn) !=None:
        return rookmovehbleft(mboard,actual_turn)
    elif rookmovehbright(mboard,actual_turn) != None:
        return rookmovehbright(mboard,actual_turn)

def rookmovevwdown(mboard,actual_turn):
    if actual_turn == "white":
        i=0
        while i<=256:
            if mboard[i] == 'R' or mboard[i] =='Q':
                n=1
                while n<=16:
                    if (i+n*16)<=255 and (i+n*16)>=0:
                        if mboard[i+n*16] != ' ':
                            if pieza_aliada(mboard[i+n*16],actual_turn):
                                i=257
                                n=17
                                return None
                            elif not (pieza_aliada(mboard[i+n*16],actual_turn)):
                                if position(i)[1] == position(i+n*16)[1]:
                                    rta = position(i), position(i+n*16)
                                    i=257
                                    n=17
                                    return rta
                        elif i+n*16>=239:
                            i=257
                            return
                    n+=1
            i+=1
def rookmovevwup(mboard,actual_turn):
    if actual_turn == "white":    
        #rook move vertical line REVISAR
        i=0
        while i <= 256:
            if mboard[i] == 'R' or mboard[i] =='Q':
                n = 1
                while n <= 16:
                    if (i - n*16) <= 255 and (i - n*16) >= 0:
                        if mboard[i-n*16] != ' ':
                            if pieza_aliada(mboard[i-n*16],actual_turn): #verifico abajo
                                i=257
                                n=17
                                return None
                            elif not (pieza_aliada(mboard[i-n*16],actual_turn)):
                                if position(i)[1] == position(i-n*16)[1]:
                                    rta = position(i), position(i-n*16)
                                    i=257
                                    n=17
                                    return rta
                    n += 1
            i += 1                               
def rookmovevw(mboard,actual_turn):
    if rookmovevwup(mboard,actual_turn) !=None:
        return rookmovevwup(mboard,actual_turn)
    elif rookmovevwdown(mboard,actual_turn) != None:
        return rookmovevwdown(mboard,actual_turn)

def rookmovevbdown(mboard,actual_turn):
    if actual_turn == "black":
        j=0
        while j <= 256:
            i=255-j
            if mboard[i] == 'r' or mboard[i] =='q':
                n=1
                while n<= 16:
                    if (i+n*16)<=255 and (i+n*16)>=0:
                        if mboard[i+n*16] != ' ':
                            if pieza_aliada(mboard[i+n*16],actual_turn): #verifico abajo
                                j=257
                                n=17
                            elif not (pieza_aliada(mboard[i+n*16],actual_turn)):
                                if position(i)[1] == position(i+n*16)[1]:
                                    rta = position(i), position(i+n*16)
                                    j=257
                                    n=17
                                    return rta    
                    n+=1
                j=257
                return None
            j+=1       
def rookmovevbup(mboard,actual_turn):
    if actual_turn == "black":
        j=0
        while j<=256:
            i=255-j
            if mboard[i] == 'r' or mboard[i] =='q':
                n=1
                while n<=16:
                    if (i-n*16)<=255 and (i-n*16)>=0:
                        if mboard[i-n*16] != ' ' and not(pieza_aliada(mboard[i-n*16],actual_turn)): #verifico arriba
                            if pieza_aliada(mboard[i-n*16],actual_turn): #verifico abajo
                                j=257
                                n=17
                            elif not(pieza_aliada(mboard[i-n*16],actual_turn)): #verifico abajo    
                                if position(i)[1] == position(i-n*16)[1]:
                                    rta = position(i), position(i-n*16)
                                    j=257
                                    n=17
                                    return rta                             
                    n+=1
                j=257
                return None
            j+=1    
def rookmovevb(mboard,actual_turn):
    if rookmovevbdown(mboard,actual_turn) !=None:
        return rookmovevbdown(mboard,actual_turn)
    elif rookmovevbup(mboard,actual_turn) != None:
        return rookmovevbup(mboard,actual_turn)

def rookmove(mboard,actual_turn):
    if actual_turn=="white":
        if rookmovehw(mboard,actual_turn) !=None:
            return rookmovehw(mboard,actual_turn)
        elif rookmovevw(mboard,actual_turn) !=None:
            return rookmovevw(mboard,actual_turn)
    if actual_turn=="black":
        if rookmovehb(mboard,actual_turn) !=None:
            return rookmovehb(mboard,actual_turn)
        elif rookmovevb(mboard,actual_turn) !=None:
            return rookmovevb(mboard,actual_turn)
# Bishops and queens: diagonal / and \ moves UP UP UP
def bishopmovebright(mboard,actual_turn):
    if actual_turn == "black":
        j=0
        while j<=255:
            i=255-j
            if mboard[i] =='b' or mboard[i] =='q':
                n=0
                while n<=16:
                    if (i-(n*15)-15)<=255 and (i-(n*15)-15)>=0:
                        if mboard[i-(n*15)-15] != ' ':
                            if pieza_aliada(mboard[i-(n*15)-15],actual_turn):
                                i=257
                                n=17    
                            elif not(pieza_aliada(mboard[i-(n*15)-15],actual_turn)): #verifico a la derecha
                                print(position(i),"to",position(i-(n*15)-15))
                                if (abs(position(i)[0] - position(i-(n*15)-15)[0]) == abs(position(i)[1] - position(i-(n*15)-15)[1])):
                                    return position(i), position(i-(n*15)-15)
                        j=255
                        return None       
                    n+=1
            j+=1 
def bishopmovebleft(mboard,actual_turn):
    if actual_turn == "black":
        #rook move horizontal line
        j=0
        while j<=255:
            i=255-j
            if mboard[i] =='b' or mboard[i] =='q':
                n=0
                while n <= 16:
                    if (i-(n*17)-17)<=256 and (i-(n*17)-17)>=0:
                        if mboard[i-(n*17)-17] != ' ':
                            if pieza_aliada(mboard[i-(n*17)-17],actual_turn):
                                i=257
                                n=17    
                            elif not(pieza_aliada(mboard[i-(n*17)-17],actual_turn)): #verifico a la derecha
                                print(position(i),"to",position(i-(n*17)-17))
                                if (abs(position(i)[0] - position(i-(n*17)-17)[0]) == abs(position(i)[1] - position(i-(n*17)-17)[1])):
                                    return position(i), position(i-(n*17)-17)
                        j=255
                        return None       
                    n+=1
            j+=1 
def bishopmovewright(mboard,actual_turn):
    if actual_turn == "white":
        #rook move horizontal line
        i=0
        while i<=255:
            if mboard[i] == 'B' or mboard[i] =='Q':
                n=0
                while n<=16:
                    if (i-(n*15)-15)<=255 and (i-(n*15)-15)>=0:
                        if mboard[(i-(n*15)-15)] != ' ':
                            if pieza_aliada(mboard[(i-(n*15)-15)],actual_turn):
                                i=257
                                n=17
                                return None
                            elif not(pieza_aliada(mboard[(i-(n*15)-15)],actual_turn)):
                                if (abs(position(i)[0] - position(i-(n*15)-15)[0]) == abs(position(i)[1] - position(i-(n*15)-15)[1])):
                                    return position(i), position(i-(n*15)-15)
                    n+=1
            i+=1
def bishopmovewleft(mboard,actual_turn):
    if actual_turn == "white":
        #rook move horizontal line
        i=0
        while i<=255:
            if mboard[i] =='B' or mboard[i] =='Q':
                n=0
                while n<=16:
                    if (i-(n*17)-17)<=255 and (i-(n*17)-17)>=0:
                        if mboard[(i-(n*17)-17)] != ' ':
                            if pieza_aliada(mboard[i+n+1],actual_turn):
                                i=257
                                n=17    
                            elif not(pieza_aliada(mboard[i+n+1],actual_turn)): #verifico a la derecha
                                if (abs(position(i)[0] - position(i-(n*17)-17)[0]) == abs(position(i)[1] - position(i-(n*17)-17)[1])):
                                    return position(i), position(i-(n*17)-17)
                        i=255
                        return None       
                    n+=1
            i+=1   
# Bishops and queens: diagonal / and \ moves DOWN
def bishopmovebleftdown(mboard,actual_turn):
    if actual_turn == "black":
        #rook move horizontal line
        j=0
        while j<=255:
            i=255-j
            if mboard[i] =='b' or mboard[i] =='q':
                n=0
                while n<=16:
                    if (i+(n*15)+15)<=255 and (i+(n*15)+15)>=0:
                        if mboard[i+(n*15)+15] != ' ':
                            if pieza_aliada(mboard[i+(n*15)+15],actual_turn):
                                i=257
                                n=17
                                return None     
                            elif not(pieza_aliada(mboard[i+(n*15)+15],actual_turn)): #verifico a la derecha
                                print(position(i),"to",position(i+(n*15)+15))
                                if (abs(position(i)[0] - position(i+(n*15)+15)[0]) == abs(position(i)[1] - position(i+(n*15)+15)[1])):
                                    return position(i), position(i+(n*15)+15)
                    n+=1
            j+=1 
def bishopmovebrightdown(mboard,actual_turn):
    if actual_turn == "black":
        #rook move horizontal line
        j=0
        while j <= 255:
            i=255-j
            if mboard[i] =='b' or mboard[i] =='q':
                n=0
                while n<=16:
                    if (i+(n*17)+17)<=255 and (i+(n*17)+17)>=0:
                        if mboard[i+(n*17)+17] != ' ':
                            if pieza_aliada(mboard[i+(n*17)+17],actual_turn):
                                i=257
                                n=17
                                return None     
                            elif not(pieza_aliada(mboard[i+(n*17)+17],actual_turn)): #verifico a la derecha
                                if (abs(position(i)[0] - position(i+(n*17)+17)[0]) == abs(position(i)[1] - position(i+(n*17)+17)[1])):
                                    return position(i), position(i+(n*17)+17)
                    n+=1
            j+=1 
def bishopmovewrightdown(mboard,actual_turn):
    if actual_turn == "white":
        #rook move horizontal line
        i=0
        while i<=255:
            if mboard[i] == 'B' or mboard[i] =='Q':
                n=0
                while n<=16:
                    if (i+(n*17)+17) <= 255 and (i+(n*17)+17) >= 0:
                        if mboard[(i+(n*17)+17)] != ' ':
                            if pieza_aliada(mboard[(i+(n*17)+17)],actual_turn):
                                i=257
                                n=17
                                return None
                            elif not(pieza_aliada(mboard[(i+(n*17)+17)],actual_turn)): #verifico a la derecha
                                if (abs(position(i)[0] - position(i+(n*17)+17)[0]) == abs(position(i)[1] - position(i+(n*17)+17)[1])):
                                    return position(i), position(i+(n*17)+17)
                        elif (i+(n*17)+17+17)<=255:
                            return None
                    n+=1
            i+=1
def bishopmovewleftdown(mboard,actual_turn):
    if actual_turn == "white":
        #rook move horizontal line
        i=0
        while i<=255:
            if mboard[i] =='B' or mboard[i] =='Q':
                n=0
                while n<=16:
                    if (i+(n*17)+17)<=255 and (i+(n*17)+17)>=0:
                        if mboard[(i-(n*15)-15)] != ' ':
                            if pieza_aliada(mboard[(i-(n*15)-15)],actual_turn):
                                i=257
                                n=17
                                return None    
                            elif not(pieza_aliada(mboard[(i-(n*15)-15)],actual_turn)):
                                if (abs(position(i)[0] - position(i-(n*15)-15)[0]) == abs(position(i)[1] - position(i-(n*15)-15)[1])):
                                    return position(i), position(i-(n*15)-15)
                    n+=1
            i+=1   

def bishopmove(mboard,actual_turn):
    if actual_turn=="white":
        if bishopmovewright(mboard,actual_turn) !=None:
            return bishopmovewright(mboard,actual_turn)
        elif bishopmovewleft(mboard,actual_turn) !=None:
            return bishopmovewleft(mboard,actual_turn)
        elif bishopmovewrightdown(mboard,actual_turn) !=None:
            return bishopmovewrightdown(mboard,actual_turn)
        elif bishopmovewleftdown(mboard,actual_turn) !=None:
            return bishopmovewleftdown(mboard,actual_turn)
    elif actual_turn=="black":
        if bishopmovebright(mboard,actual_turn) !=None:
            return bishopmovebright(mboard,actual_turn)
        elif bishopmovebleft(mboard,actual_turn) !=None:
            return bishopmovebleft(mboard,actual_turn)
        elif bishopmovebrightdown(mboard,actual_turn) !=None:
            return bishopmovebrightdown(mboard,actual_turn)
        elif bishopmovebleftdown(mboard,actual_turn) !=None:
            return bishopmovebleftdown(mboard,actual_turn)

def kingmove(mboard,actual_turn):
    if actual_turn == "white":
        i=0
        while i<=255:
            if mboard[i] =='K':
                    if (i-1)<=255 and (i-1)>=0:
                        if mboard[(i-1)] != ' ':
                            if not(pieza_aliada(mboard[(i-1)],actual_turn)):
                                    return position(i), position(i-1)
                    elif (i+1)<=255 and (i+1)>=0:
                        if mboard[(i+1)] != ' ':
                            if not(pieza_aliada(mboard[(i+1)],actual_turn)):
                                    return position(i), position(i+1)
                    elif (i+16)<=255 and (i+16)>=0:
                        if mboard[(i+16)] != ' ':
                            if not(pieza_aliada(mboard[(i+16)],actual_turn)):
                                    return position(i), position(i+16)
                    elif (i-16)<=255 and (i-16)>=0:
                        if mboard[(i-16)] != ' ':
                            if not(pieza_aliada(mboard[(i-16)],actual_turn)):
                                    return position(i), position(i-16)
                    elif (i+17)<=255 and (i+17)>=0:
                        if mboard[(i+17)] != ' ':
                            if not(pieza_aliada(mboard[(i+17)],actual_turn)):
                                    return position(i), position(i+17)
                    elif (i-17)<=255 and (i-17)>=0:
                        if mboard[(i-17)] != ' ':
                            if not(pieza_aliada(mboard[(i-17)],actual_turn)):
                                    return position(i), position(i-17)
                    elif (i-15)<=255 and (i-15)>=0:
                        if mboard[(i-15)] != ' ':
                            if not(pieza_aliada(mboard[(i-15)],actual_turn)):
                                    return position(i), position(i-15)
                    elif (i+15)<=255 and (i+15)>=0:
                        if mboard[(i+15)] != ' ':
                            if not(pieza_aliada(mboard[(i+15)],actual_turn)):
                                    return position(i), position(i+15)
            elif i>=247:
                return None
            i+=1
    elif actual_turn == "black":
        i=0
        while i<=255:
            if mboard[i] =='k':
                    if (i-1)<=255 and (i-1)>=0:
                        if mboard[(i-1)] != ' ':
                            if not(pieza_aliada(mboard[(i-1)],actual_turn)):
                                    return position(i), position(i-1)
                    elif(i+1)<=255 and (i+1)>=0:
                        if mboard[(i+1)] != ' ':
                            if not(pieza_aliada(mboard[(i+1)],actual_turn)):
                                    return position(i), position(i+1)
                    elif (i+16)<=255 and (i+16)>=0:
                        if mboard[(i+16)] != ' ':
                            if not(pieza_aliada(mboard[(i+16)],actual_turn)):
                                    return position(i), position(i+16)
                    elif (i-16)<=255 and (i-16)>=0:
                        if mboard[(i-16)] != ' ':
                            if not(pieza_aliada(mboard[(i-16)],actual_turn)):
                                    return position(i), position(i-16)
                    elif (i+17)<=255 and (i+17)>=0:
                        if mboard[(i+17)] != ' ':
                            if not(pieza_aliada(mboard[(i+17)],actual_turn)):
                                    return position(i), position(i+17)
                    elif (i-17)<=255 and (i-17)>=0:
                        if mboard[(i-17)] != ' ':
                            if not(pieza_aliada(mboard[(i-17)],actual_turn)):
                                    return position(i), position(i-17)
                    elif (i-15)<=255 and (i-15)>=0:
                        if mboard[(i-15)] != ' ':
                            if not(pieza_aliada(mboard[(i-15)],actual_turn)):
                                    return position(i), position(i-15)
                    elif (i+15)<=255 and (i+15)>=0:
                        if mboard[(i+15)] != ' ':
                            if not(pieza_aliada(mboard[(i+15)],actual_turn)):
                                    return position(i), position(i+15)

            elif i<=255:
                if mboard[i] == ' ':
                    return None
            i+=1 

def strategy(mboard,actual_turn):
    if pawneat(mboard,actual_turn) !=None:
        return pawneat(mboard,actual_turn)
    elif rookmove(mboard,actual_turn) !=None:
        return rookmove(mboard,actual_turn)
    elif bishopmove(mboard,actual_turn) !=None:
        return bishopmove(mboard,actual_turn)
    elif kingmove(mboard,actual_turn) !=None:
        return kingmove(mboard,actual_turn)
    elif select_pawn(mboard,actual_turn) != None:
        return select_pawn(mboard,actual_turn)

async def send(websocket, action, data):
    message = json.dumps(
        {
            'action': action,
            'data': data,
        }
    )
    print("*****************************************")
    print("servidor:",message)
    print("*****************************************")
    await websocket.send(message)


async def start(auth_token):
    uri = "ws://megachess.herokuapp.com/service?authtoken={}".format(auth_token)
    while True:
        print('connection to {}'.format(uri))
        async with websockets.connect(uri) as websocket:
            await play(websocket)


async def play(websocket):
    while True:
        try:
            response = await websocket.recv()
            data = json.loads(response)
            if data['event'] == 'update_user_list':
                pass
            if data['event'] == 'gameover':
                pass
            if data['event'] == 'ask_challenge':
                # if data['data']['username'] == 'favoriteopponent':
                await send(
                    websocket,
                    'accept_challenge',
                    {
                        'board_id': data['data']['board_id'],
                    },
                )
            if data['event'] == 'your_turn':
                print("BOARD ID:",data['data']['board_id'],'\n' "TURN TOKEN:",data['data']['turn_token'],'\n' "USERNAME:",data['data']['username'],'\n' "ACTUAL TURN:",data['data']['actual_turn'],'\n' "MOVE LEFT:",data['data']['move_left'],'\n' "OPONENT USERNAME:",data['data']['opponent_username'],'\n' "RAW BOARD:{",data['data']['board'],"}")
                mboard = data['data']['board']
                print('\n',mboard[0:16],'\n', mboard[16:32],'\n',mboard[32:48],'\n',mboard[48:64],'\n',mboard[64:80],'\n',mboard[80:96],'\n',mboard[96:112],'\n',mboard[112:128],'\n',mboard[128:144],'\n',mboard[144:160],'\n',mboard[160:176],'\n',mboard[176:192],'\n',mboard[192:208],'\n',mboard[208:224],'\n',mboard[224:240],'\n',mboard[240:256])                
                fromto=strategy(mboard,data['data']['actual_turn'])
                fr=fromto[0]
                to=fromto[1]
                await send(
                        websocket,
                        'move',
                        {
                            'board_id': data['data']['board_id'],
                            'turn_token': data['data']['turn_token'],
                            'from_row': fr[0],
                            'from_col': fr[1],
                            'to_row': to[0],
                            'to_col': to[1],
                        },
                    )


        except Exception as e:
            print('error {}'.format(str(e)))
            break  # force login again


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        auth_token = sys.argv[1]
        asyncio.get_event_loop().run_until_complete(start(auth_token))
    else:
        print('please provide your auth_token')
