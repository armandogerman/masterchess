import websockets
from random import randint
#from masterchess import fr,fc,tr,tc
#data = {"event":"your_turn","data":{"board_id":"tournament:4e4cf244-6dc4-4ade-8622-7f2dfa5290d8::41e005a2-7829-43e0-86bc-161544b79bb4","turn_token":"183286cc-ed27-4470-a89b-14430c510bf2","username":"armandogerman","actual_turn":"black","board":"rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                  Q                                              P                              P P PPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR","move_left":190,"opponent_username":"EnzoC"}}
fromr = ''
fromc = ''
tor = ''
toc = ''
fromto = ()

def mov(data):
    board_id = data['data']['board_id'],
    turn_token = data['data']["turn_token"],                       # 7e68c0b0-ad81-4b31-956c-fd595755ea34
    username = ''.join(data['data']["username"])                   # armandogerman
    actual_turn = ''.join(data['data']["actual_turn"])             # black
    move_left = data['data']["move_left"],                         # 199
    opponent_username = ''.join(data['data']['opponent_username']) # pepe
    mboard = ''.join(data['data']["board"])                        #[0:256]
    print("*****************************************************")
    print("BOARD ID:",board_id,'\n' "TURN TOKEN:",turn_token,'\n' "USERNAME:",username,'\n' "ACTUAL TURN:",actual_turn,'\n' "MOVE LEFT:",move_left,'\n' "OPONENT USERNAME:",opponent_username)
    print('\n',mboard[0:16],'\n', mboard[16:32],'\n',mboard[32:48],'\n',mboard[48:64],'\n',mboard[64:80],'\n',mboard[80:96],'\n',mboard[96:112],'\n',mboard[112:128],'\n',mboard[128:144],'\n',mboard[144:160],'\n',mboard[160:176],'\n',mboard[176:192],'\n',mboard[192:208],'\n',mboard[208:224],'\n',mboard[224:240],'\n',mboard[224:240],'\n',mboard[240:256])
    print("*****************************************************")
    if username == "armandogerman":
        if actual_turn == "black":
            print("hello black")
            fromr = int(3)
            fromc = int(randint(0, 15))
            tor = int(5)
            toc = int(fromc)
            print("from:",fromr,"-",fromc,"to:",tor,"-",toc)
            fromto = fromr, fromc, tor, toc
            print("pieza que se Mueve:", mboard[fromc+fromr*16])
            return fromto
        else:
            print("hello white")
            fromr = int(12)
            fromc = int(randint(0, 15))
            tor = int(10)
            toc = int(fromc)
            print("from:",fromr,"-",fromc,"to:",tor,"-",toc)
            fromto = fromr, fromc, tor, toc
            print("pieza que se Mueve:", mboard[fromc+fromr*16])
            return fromto