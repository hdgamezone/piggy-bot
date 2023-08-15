import time
import pandas as pd
from lib.piggy_lib import API_Piggy
from lib.piggy_lib import API_Login
import json

fcmtoken = "fm446RpWSIa6E56hxAXWfU:APA91bEEPMbMIA6GwphJFAETzMd-uyL3MGPIHckXOgSeBH5TPDnb3OytYJGhvlR53ECloU9bWHoq_0qTyL7uW_j5eipLCSO1N4I11SUr-Hyg9MILQCRburlQtK9CXd5wxcsQ9hMwARXs"
userid = "2004861643218023"
fbtoken = ",xev*,xaz*,xaz*tuy,xaz*,xgt*4PKo,xby*O1TpqS,xdw*1Rl4UPO5Z,xcx*s7HV,xgt*w1Z,xcx*x,xcx*zL4Kz2TZ,xaz*KsNkme8cR,xfu*JHH,xcx*T2tPbYPt84cKZ,xaz*K,xby*Z,xby*fa0VrKInuaKPpJutlhb,xby*Oix,xfu*j,xby*8,xby*cpOcqyYj,xgt*Oyly,xfu*MqaTYlXTTo89,xaz*7aZ,xby*9Q,xcx*o9WaJnde,xdw*r6Z,xby*,xby*Z,xaz*rZ,xaz*,xby*KjeLZ,xcx*YtSIPv2Pmw65,xcx*V,xgt*Z,xcx*yYuZ,xcx*9TS7P6,xev*d2dM5R,xgt*ORw3czMXi5mQT2Z,xaz*Y,xdw*Z,xaz*n7UWvoyhSZ,xaz*Z,xby*kUVbTmk4s,xdw*IJQclwZ,xdw*Z,xdw*"
line_token = "vrxieWZ0i7pNJADIISaD8tPkxmFw0At06eHP0lbZd7q"


login = API_Login.login(userid,fbtoken,fcmtoken)
print(login)

game_id = login['userid']
game_token = login['jwttoken']

game = API_Piggy(game_id,game_token,line_token)

bag = game.backpack()
print(bag)
for item in bag['users_backpack']:
    if item['item_id'] == '14' and item['item_category'] == 'food':
        item_amount = int(item['item_amount'])


def update_profile():
    user_data = game.user_info()
    userdata = user_data['users_data']
    coins = int(userdata["coins"])/1000000
    if coins < 5:
        quit()
    coinsm = '%.1f' %(coins)
    print(f'==============================\naccount : {userdata["fbname"]}\ncoin : {coinsm} M\ncash : {userdata["cash"]}\nleafcoins : {userdata["leafcoins"]}\nlevel : {userdata["level"]}\nexp : {userdata["exp"]}\nmission points : {userdata["mission_points"]}\n==========================================')
    info_json_str = user_data["level_lists"]["info"]
    info_data = json.loads(info_json_str)
    levelup_exp = info_data["exp"]
    return levelup_exp

def get_exp(feed):
    users_update = feed.get('users_update', {})
    exp = users_update.get('exp', '0')
    return int(exp)



while True:
    try:
        levelup_exp = update_profile()
        for i in range(100):
            try:
                spin = game.spin()
                time.sleep(0.1)
            except:
                time.sleep(5)
                pass
            print(f'{i} : {spin}')

        bag = game.backpack()
        item_amount = 0
        for item in bag['users_backpack']:
            if item['item_id'] == '14' and item['item_category'] == 'food':
                item_amount = int(item['item_amount'])
                print(f'item feed : {item_amount}')
        if item_amount > 200:
            item_feed = 200
        else:
            item_feed = item_amount

        for i in range(item_amount):
            try:
                feed = game.feed_confirm(userid,1,14) # 14 = เยลลี่ 34 = เค้ก
                time.sleep(0.1)
            except:
                time.sleep(5)
                pass

            exp = get_exp(feed)
            per = (int(exp)/int(levelup_exp))*100
            print(f'{i} : {feed} {int(per)}%')
            if int(exp) == int(levelup_exp):
                levelup = game.levelup()
                print(levelup)
                levelup_exp = update_profile()
                print(f'update exp : {levelup_exp}')
    except:
        pass


