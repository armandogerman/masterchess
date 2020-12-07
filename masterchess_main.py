import websockets
from turn import calc
fromto = ()
def mov(data):
    board_id = data['data']['board_id']
    turn_token = data['data']["turn_token"]                       
    username = data['data']["username"]                  
    actual_turn = data['data']["actual_turn"]            
    move_left = data['data']['move_left']
    opponent_username = data['data']['opponent_username'] 
    mboard = data['data']["board"]
    print("*****************************************************")
    print("BOARD ID:",board_id,'\n' "TURN TOKEN:",turn_token,'\n' "USERNAME:",username,'\n' "ACTUAL TURN:",actual_turn,'\n' "MOVE LEFT:",move_left,'\n' "OPONENT USERNAME:",opponent_username)
    print('\n',mboard[0:16],'\n', mboard[16:32],'\n',mboard[32:48],'\n',mboard[48:64],'\n',mboard[64:80],'\n',mboard[80:96],'\n',mboard[96:112],'\n',mboard[112:128],'\n',mboard[128:144],'\n',mboard[144:160],'\n',mboard[160:176],'\n',mboard[176:192],'\n',mboard[192:208],'\n',mboard[208:224],'\n',mboard[224:240],'\n',mboard[224:240],'\n',mboard[240:256])
    if username == "armandogerman":
        fromto = calc(mboard,actual_turn)
        fr=fromto[0]                                               #Asigno la tupla from
        to=fromto[1]                                               #Asigno la tupla to
        print(fr[0],fr[1],to[0],to[1])
        print("pieza que se Seleccionada:", mboard[fr[1]+fr[0]*16])
    return fr[0],fr[1],to[0],to[1]
 