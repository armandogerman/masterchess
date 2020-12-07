import asyncio
import json
from random import randint
import sys
import websockets

def position(i):                #esta funcion calcula la posicion enviada de la cadena y devuelve fila y columna
    for j in range(0, 16):
        colum = i - j * 16
        if colum < 16 and colum >= 0:
            return j,colum

def pawnmove(mboard,actual_turn):
    if actual_turn == "white":
        i=143
        while i <= 256:
            if mboard[i] == 'P':
                if i > 191:
                    if mboard[i-32] == ' ':
                        if mboard[i-16] == ' ':
                            print("pawn: x+2,y",i)
                            return position(i), position(i-32)
                elif i <= 191:
                    print("pawn: x+1,y",i)
                    if mboard[i-16] == ' ':
                        return position(i),position(i-16)
            i += 1
    elif actual_turn == "black":
        n=143
        while n <= 255:
            i=255-n
            if mboard[i] == 'p':
                if i < 64:
                    if mboard[i+32] == ' ':
                        if mboard[i+16] == ' ':
                            print("pawn: x+2,y",i)                         
                            return position(i),position(i+32)
                elif i >= 64:
                    if mboard[i+16] == ' ':
                        print("pawn: x+1,y",i)
                        return position(i),position(i+16)
            n += 1

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
                print("BOARD ID:",data['data']['board_id'],'\n' "TURN TOKEN:",data['data']['turn_token'],'\n' "USERNAME:",data['data']['username'],'\n' "ACTUAL TURN:",data['data']['actual_turn'],'\n' "MOVE LEFT:",data['data']['move_left'],'\n' "OPONENT USERNAME:",data['data']['opponent_username'])
                mboard = data['data']['board']
                print('\n',mboard[0:16],'\n', mboard[16:32],'\n',mboard[32:48],'\n',mboard[48:64],'\n',mboard[64:80],'\n',mboard[80:96],'\n',mboard[96:112],'\n',mboard[112:128],'\n',mboard[128:144],'\n',mboard[144:160],'\n',mboard[160:176],'\n',mboard[176:192],'\n',mboard[192:208],'\n',mboard[208:224],'\n',mboard[224:240],'\n',mboard[224:240],'\n',mboard[240:256])
                fromto=pawnmove(mboard,data['data']['actual_turn'])
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
