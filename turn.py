#response = {}
#response = {"board_id":"8deca84e-ab14-493b-9e6c-98bc0f3072ff","turn_token":"7e68c0b0-ad81-4b31-956c-fd595755ea34","username":"armandogerman","actual_turn":"white","board":"orhhbbqqkkbbhhrkhrhhbbqqkkbbhhrqpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR","move_left":199,"opponent_username":"armandogerman"}


class Turn:
    def __init__(self,data):
        self.board_id = data['data']['board_id']                       # 8deca84e-ab14-493b-9e6c-98bc0f3072ff
        self.turn_token = data['data']["turn_token"]                   # 7e68c0b0-ad81-4b31-956c-fd595755ea34
        self.username = data['data']["username"]                       # armandogerman
        self.actual_turn = data['data']["actual_turn"]                 # white
        self.board = data['data']["board"]                             # rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR
        self.move_left = data['data']["move_left"]                     # 199
        self.opponent_username = data['data']["opponent_username"]     # armandogerman
    def mov(self):
        if self.actual_turn == white:
            if self.board


        

#class Move:
#    def __init__(self,data):
#        self.board_id = data['data']['board_id']                       # 8deca84e-ab14-493b-9e6c-98bc0f3072ff
#        self.turn_token = data['data']["turn_token"]                   # 7e68c0b0-ad81-4b31-956c-fd595755ea34
#        self.board = data['data']["board"]
#        self.from_row = 6
#        self.from_col = 3
#        self.to_row = 6
#        self.to_col = 4
#    def __str__(self):
#        pass
        #if ['data']['actual_turn'] == white
        #    if ['data']['board'] = 
        

class Board:
    def __init__(self,data):
        pass

class Square:
    pass

class PieceSet:
    pass

class Piece:
    def __init_(self):
        pass


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



#class Player:
#    def__init__(self,)










#data={'event': 'your_turn', 'data': {'board_id': 'e7c741e9-2727-4a4f-8ab8-5d50dfc1345e', 'turn_token': 'b684410f-7075-4cea-9874-7552b234ce13', 'username': 'armandogerman', 'actual_turn': 'white', 'board': 'rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR', 'move_left': 148, 'opponent_username': 'armandogerman'}}
#print(type(data))
#print(data['data']['board_id'])
#theplay = Turn(data)
#print("--------------------vamos que saleeee--------")
#print(theplay.username)





#class Turn:
#    def __init__(self,data):
#        self.board_id = data["board_id"]
#        self.turn_token = data["turn_token"]
#        self.username = data["username"]
#        self.actual_turn = data["actual_turn"]
#        self.board = data["board"]
#        self.move_left = data["move_left"]

#obj = turn(response)
#print("   ",obj.board[0:16],"\n   ",obj.board[16:32],"\n   ",obj.board[32:48],"\n   ",obj.board[48:64],"\n   ",obj.board[64:80],"\n   ",obj.board[80:96],"\n   ",obj.board[96:112],"\n   ",obj.board[112:128],"\n   ",obj.board[128:144],"\n   ",obj.board[144:160],"\n   ",obj.board[160:176],"\n   ",obj.board[176:192],"\n   ",obj.board[192:208],"\n   ",obj.board[208:224],"\n   ",obj.board[224:240],"\n   ",obj.board[240:256])

#recorrer los valores del diccionario
#for value in response.values():
#    print(value)
#recorrer los indices del diccionario
# for key in response:
#   print(key)

#print(type(obj.board))
#print(type (response))
#print(response["board_id"])