import time
import pandas as pd
from lib.piggy_lib import API_Piggy
from lib.piggy_lib import API_Login
import json

fcmtoken = "cHRXV3hxQoeuOsMP3rYfqd:APA91bG-CzprE-YW6AeokG1pJe9lvGM034UUCZgoHVfYLL8RDixvbBMwCcjii93iehwOeRORZNbLvWP38-dTHwOWxah1CbPNUpEEQRj_JFgpZCjWApcr8L4aWDB6rIbfuEz7-RYdCCnJ"
userid = "1559670881126206"
fbtoken = ",xev*,xaz*,xaz*tuy,xaz*,xgt*4PKo,xby*O2avwwQ3MIWK,xcx*Hwf3Y,xby*,xby*a2MhPoSM23c,xev*y8jerYUOlZ,xcx*NvNlTY,xdw*ewXK,xby*m4wqtzmItTyztWROHL,xcx*pZ,xby*Z,xaz*Z,xaz*PaXLfrksZ,xby*Ht,xby*4WkWyylQ6aWe4,xdw*f3WzOT,xdw*RbWe5,xfu*a4dn,xaz*6Pwu,xfu*0JneYQj5169N,xby*KcZ,xby*QnVV7hcoyUK8,xfu*eKQZ,xcx*bMr8p,xby*PXi4,xaz*q7VYwpqonhxsTU4bjkpz,xcx*KOU8c8,xcx*Js83pds6,xev*,xaz*2087pocUefXn0260wQZ,xdw*Z,xdw*"
line_token = "vrxieWZ0i7pNJADIISaD8tPkxmFw0At06eHP0lbZd7q"


login = API_Login.login(userid,fbtoken,fcmtoken)

game_id = login['userid']
game_token = login['jwttoken']

game = API_Piggy(game_id,game_token,line_token)

bag = game.backpack()
for item in bag['users_backpack']:
    if item['item_id'] == '14' and item['item_category'] == 'food':
        item_amount = int(item['item_amount'])


def update_profile():
    user_data = game.user_info()
    userdata = user_data['users_data']
    coins = int(userdata["coins"])/1000000
    coinsm = '%.1f' %(coins)
    print(f'==============================\naccount : {userdata["fbname"]}\ncoin : {coinsm} M\ncash : {userdata["cash"]}\nleafcoins : {userdata["leafcoins"]}\nlevel : {userdata["level"]}\nexp : {userdata["exp"]}\nmission points : {userdata["mission_points"]}\n==========================================')
    info_json_str = user_data["level_lists"]["info"]
    info_data = json.loads(info_json_str)
    levelup_exp = info_data["exp"]
    return levelup_exp

levelup_exp = update_profile()


while True:
    for i in range(50):
        try:
            spin = game.spin()
        except:
            time.sleep(1)
            pass
        print(f'{i} : {spin}')

    bag = game.backpack()
    for item in bag['users_backpack']:
        if item['item_id'] == '14' and item['item_category'] == 'food':
            item_amount = int(item['item_amount'])
            print(f'item feed : {item_amount}')
    if item_amount > 200:
        item_feed = 200
    else:
        item_feed = item_amount

    for i in range(item_feed):
        try:
            feed = game.feed_confirm(userid,1,14) # 14 = เยลลี่
            time.sleep(0.1)
        except:
            time.sleep(1)
            pass

        exp = feed['users_update']['exp']
        per = (int(exp)/int(levelup_exp))*100
        print(f'{i} : {feed} {int(per)}%')
        if int(exp) == int(levelup_exp):
            levelup = game.levelup()
            print(levelup)
            levelup_exp = update_profile()
            print(f'update exp : {levelup_exp}')



