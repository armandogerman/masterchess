
'''
from turn import *

data={'event': 'your_turn', 'data': {'board_id': 'e7c741e9-2727-4a4f-8ab8-5d50dfc1345e', 'turn_token': 'b684410f-7075-4cea-9874-7552b234ce13', 'username': 'armandogerman', 'actual_turn': 'white', 'board': 'rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR', 'move_left': 148, 'opponent_username': 'armandogerman'}}

print("________________________")
a = (data['data']['board'])
print("   ",a[0:16],"\n   ",a[16:32],"\n   ",a[32:48],"\n   ",a[48:64],"\n   ",a[64:80],"\n   ",a[80:96],"\n   ",a[96:112],"\n   ",a[112:128],"\n   ",a[128:144],"\n   ",a[144:160],"\n   ",a[160:176],"\n   ",a[176:192],"\n   ",a[192:208],"\n   ",a[208:224],"\n   ",a[224:240],"\n   ",a[240:256])
theplay = Turn(data)
print("El chango que mueve:",theplay.username)
themove = Move(data)
print("________________________")
print("Informacion de jugada")
print("the piece's place is: (", themove.from_row,",", themove.from_col,")")
print("the piece's Move is:  (", themove.to_row,",",themove.to_col,")")

themove.__str__()
'''

#from turn import Turn

#theplay = Turn(data)
#board = data['data']['board']
#print (board[1])
#data = {"event":"your_turn","data":{"board_id":"tournament:4e4cf244-6dc4-4ade-8622-7f2dfa5290d8::41e005a2-7829-43e0-86bc-161544b79bb4","turn_token":"183286cc-ed27-4470-a89b-14430c510bf2","username":"armandogerman","actual_turn":"black","board":"rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                  Q                                              P                              P P PPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR","move_left":190,"opponent_username":"EnzoC"}}
def mov(data):
    board_id = data['data']['board_id'],
    turn_token = data['data']["turn_token"],                   # 7e68c0b0-ad81-4b31-956c-fd595755ea34
    username = data['data']["username"],                       # armandogerman
    actual_turn = data['data']["actual_turn"],                 # black
    board = data['data']["board"],                             # rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR)
    move_left = data['data']["move_left"],                     # 199
    opponent_username = data['data']["opponent_username"],     # pepe
    mboard = ''.join(data['data']["board"][0:256])
    print("BOARD ID:",board_id,'\n' "TURN TOKEN:",turn_token,"BOARD ID:",username,'\n' "ACTUAL TURN:",actual_turn,'\n' "MOVE LEFT:",move_left,'\n' "OPONENT USERNAME:",opponent_username)
    print('\n',mboard[0:16],'\n', mboard[16:32],'\n',mboard[32:48],'\n',mboard[48:64],'\n',mboard[64:80],'\n',mboard[80:96],'\n',mboard[96:112],'\n',mboard[112:128],'\n',mboard[128:144],'\n',mboard[144:160],'\n',mboard[160:176],'\n',mboard[176:192],'\n',mboard[192:208],'\n',mboard[208:224],'\n',mboard[224:240],'\n',mboard[224:240],'\n',mboard[240:256])
    
    if actual_turn == "white":
        print("hello white")
    else:
        print("hello black")

#mov(data),