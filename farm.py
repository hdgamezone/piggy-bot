import time
import pandas as pd
from lib.lib_farm import API_Piggy
from lib.lib_farm import API_login
import json

fcmtoken = "cHRXV3hxQoeuOsMP3rYfqd:APA91bG-CzprE-YW6AeokG1pJe9lvGM034UUCZgoHVfYLL8RDixvbBMwCcjii93iehwOeRORZNbLvWP38-dTHwOWxah1CbPNUpEEQRj_JFgpZCjWApcr8L4aWDB6rIbfuEz7-RYdCCnJ"

logins = [
    {
        "userid": "1799869087014887",
        "fbtoken": ",xev*,xaz*,xaz*tuy,xaz*,xgt*4PKo,xby*O85PkqnZ,xcx*5aHsyonyIf,xcx*4g,xev*vKxpp5n3OJ9Z,xby*Q9sY3J0U,xaz*UkXk4qq1qrfw9OUxSyNIT,xev*,xev*4I16PZ,xby*T6iOZ,xby*,xfu*Pd7LJx,xcx*X4TQP1UV,xfu*W,xcx*uks,xev*MJeQN,xdw*Oso1Z,xaz*RMp7,xfu*,xcx*2V,xgt*kVfzR,xdw*,xaz*6ygfzYO7,xev*gImuZ,xby*V7IdaZ,xaz*ViXT2YKo4I3IV,xaz*gImcT,xfu*xseaTz1K3,xaz*,xev*,xev*HZ,xcx*t8uRy,xfu*qudKmIh,xev*0M51RTU,xev*w,xgt*u3tO8VtJh5Z,xaz*i5m,xfu*fub,xcx*0QZ,xdw*Z,xdw*",
        "fcmtoken": fcmtoken
    },
    {
        "userid": "845934969786079",
        "fbtoken": ",xev*,xaz*,xaz*tuy,xaz*,xgt*4PKo,xby*O6Iiqqn,xev*pZ,xby*xlkT1d,xby*,xaz*be2Uqu41mguwLus44,xgt*dxuy,xfu*Z,xcx*kZ,xcx*YSX,xaz*oIf6biH6RHWUif,xgt*p77YZ,xcx*vnUhJZ,xaz*Q0euYTcHmUWU5ehpcvrK1K,xdw*9K02,xaz*NIgVvlNcH2cgVckQo6L5KrTKTb1,xfu*6m,xdw*lhadXpxS9,xaz*a,xcx*fxgmJmw8,xev*9b,xby*,xdw*pRke788,xfu*1,xfu*RU2ITXLZ,xby*z8,xby*xvo1Z,xcx*b4Q4amwwW,xev*vnXts9feJgo,xev*2q,xaz*Z,xaz*,xby*gv4PZ,xcx*,xfu*9TRUZ,xby*Sh9gZ,xdw*Z,xdw*&",
        "fcmtoken": fcmtoken
    },
    {
        "userid": "3365062063757296",
        "fbtoken": ",xev*,xaz*,xaz*tuy,xaz*,xgt*4PKo,xby*O7TT,xev*UfTKtvZ,xby*xigZ,xcx*RTWc13wx4Z,xby*Xj,xev*i9OMPpZ,xcx*uZ,xaz*funHmJifx1,xdw*wm0,xfu*7Z,xaz*,xdw*p3,xfu*,xcx*xvHZ,xby*q2Hv1,xgt*Xv,xcx*Y7H28d3uoVu,xaz*RJ,xgt*8y625TY,xcx*1Z,xby*96oI,xaz*I,xdw*mPZ,xby*,xgt*qIsOYn,xdw*Y8UOzdT8K2trd0pMoOd,xby*wLXLVwQdnOvMiHZ,xcx*khdj,xdw*SKJgQj,xcx*Z,xcx*tMzJYvQ,xgt*4,xgt*6,xby*onw5fZ,xby*,xby*4XyM4IzmpZ,xby*RUblnljvLZ,xcx*K,xby*Pk9,xdw*dSVZ,xaz*,xdw*qbsZ,xby*lRrR7tSgZ,xdw*Z,xdw*",
        "fcmtoken": fcmtoken
    },
{
        "userid": "1559670881126206",
        "fbtoken": ",xev*,xaz*,xaz*tuy,xaz*,xgt*4PKo,xby*O2avwwQ3MIWK,xcx*Hwf3Y,xby*,xby*a2MhPoSM23c,xev*y8jerYUOlZ,xcx*NvNlTY,xdw*ewXK,xby*m4wqtzmItTyztWROHL,xcx*pZ,xby*Z,xaz*Z,xaz*PaXLfrksZ,xby*Ht,xby*4WkWyylQ6aWe4,xdw*f3WzOT,xdw*RbWe5,xfu*a4dn,xaz*6Pwu,xfu*0JneYQj5169N,xby*KcZ,xby*QnVV7hcoyUK8,xfu*eKQZ,xcx*bMr8p,xby*PXi4,xaz*q7VYwpqonhxsTU4bjkpz,xcx*KOU8c8,xcx*Js83pds6,xev*,xaz*2087pocUefXn0260wQZ,xdw*Z,xdw*",
        "fcmtoken": fcmtoken
    },
{
        "userid": "102304696053715",
        "fbtoken": ",xev*,xaz*,xaz*tuy,xaz*,xgt*4PKo,xby*O3PIVXiMH6,xev*4WaN6y,xdw*Omy8wV4QSsPw7IVR7vOjX6,xgt*hH,xby*0XZ,xaz*n8yh8HOaHPgkkV3,xgt*5wrTSlHabyd7gWk1nMhz2Z,xcx*,xaz*tz6yaWRrITZ,xaz*cs,xdw*7Z,xby*gPP9qZ,xcx*JY926I6iN61NqyZ,xby*MqL9aQrmZ,xby*KZ,xaz*gwxQs60n2Ifmw6K,xev*M,xdw*wr,xaz*k,xaz*RTPJzryaRe,xev*jo,xdw*,xdw*,xaz*dPZ,xcx*,xgt*o,xdw*RfSrcyf,xcx*y,xcx*S1Z,xaz*Lj,xcx*v,xfu*,xgt*6QjUMeoz5Kzmj,xby*OQqolhaQXO,xev*QHRZ,xby*MRmols,xaz*Z,xdw*Z,xdw*",
        "fcmtoken": fcmtoken
    }
]

login_user = []
login_token = []

for login in logins:
    token = API_login.login(login["userid"], login["fbtoken"], login["fcmtoken"])
    login_user.append(token['userid'])
    login_token.append(token['jwttoken'])

users = [
    {
        "user_id": login_user[0],
        "Token_id": login_token[0],
        "line": "vrxieWZ0i7pNJADIISaD8tPkxmFw0At06eHP0lbZd7q",
        "plots_to_check": ["1", "2", "3", "4"],
        "stall_id": [2,3,4,5,6,7,8,9,10,13]
    },
    {
        "user_id": login_user[1],
        "Token_id": login_token[1],
        "line": "vrxieWZ0i7pNJADIISaD8tPkxmFw0At06eHP0lbZd7q",
        "plots_to_check": ["1", "2", "3", "4"],
        "stall_id": [2,3,4]
    },
    {
        "user_id": login_user[2],
        "Token_id": login_token[2],
        "line": "vrxieWZ0i7pNJADIISaD8tPkxmFw0At06eHP0lbZd7q",
        "plots_to_check": ["1", "2", "3", "4"],
        "stall_id": [2,3,4]
    },
{
        "user_id": login_user[3],
        "Token_id": login_token[3],
        "line": "vrxieWZ0i7pNJADIISaD8tPkxmFw0At06eHP0lbZd7q",
        "plots_to_check": ["1", "2", "3","4"],
        "stall_id": [2,3,4,5]
    },
{
        "user_id": login_user[4],
        "Token_id": login_token[4],
        "line": "vrxieWZ0i7pNJADIISaD8tPkxmFw0At06eHP0lbZd7q",
        "plots_to_check": ["1", "2", "3","4"],
        "stall_id": [2,3,4,4]
    },
    # เพิ่ม user_id และ Token_id อื่น ๆ ตามต้องการ
]

stop_time = time.time() - 1

while True:
    try:

        if time.time() > stop_time:
            for user in users:
                user_id = user["user_id"]
                Token_id = user["Token_id"]
                print(Token_id)
                line = user["line"]
                pig = API_Piggy(user_id, Token_id, line)
                user_data = pig.user_data()

                info_json_str = user_data["level_lists"]["info"]
                info_data = json.loads(info_json_str)
                levelup_exp = info_data["exp"]

                userdata = user_data['users_data']
                coins = int(userdata["coins"]) / 1000000
                coinsm = '%.1f' % (coins)
                leafcoin = int(userdata["leafcoins"]) / 1000000
                leafcoins = '%.1f' % (leafcoin)
                per = (int(userdata["exp"])/int(levelup_exp))*100
                barn = pig.barn()
                pig.line(
                    f' ข้อมูลบัญชี\naccount : {userdata["fbname"]}\nuser id : {user_id}\ncoin : {coinsm} M\ncash : {userdata["cash"]}\nleafcoins : {leafcoins} M\nlevel : {userdata["level"]}\nexp : {userdata["exp"]}/{levelup_exp} : {int(per)}%\nmission points : {userdata["mission_points"]}\ncorn : {barn}')
            stop_time = time.time() + 300

        for user in users:
            user_id = user["user_id"]
            Token_id = user["Token_id"]
            line = user["line"]
            pig = API_Piggy(user_id, Token_id, line)

            user_data = pig.user_data()

            info_json_str = user_data["level_lists"]["info"]
            info_data = json.loads(info_json_str)
            levelup_exp = info_data["exp"]

            userdata = user_data['users_data']
            coins = int(userdata["coins"]) / 1000000
            coinsm = '%.1f' % (coins)
            print(
                f'==============================\naccount : {userdata["fbname"]}\ncoin : {coinsm} M\ncash : {userdata["cash"]}\nleafcoins : {userdata["leafcoins"]}\nlevel : {userdata["level"]}\nexp : {userdata["exp"]}/{levelup_exp}\nmission points : {userdata["mission_points"]}\n ==========================================')

            plots_to_check = user["plots_to_check"]
            for plot_id in plots_to_check:
                farm = pig.farm_load()
                if 'users_plot_objects' in farm:
                    users_plot_objects = farm['users_plot_objects']
                    plot_id_to_find = plot_id
                    plot_object_harvest = []
                    for plot_obj in users_plot_objects:
                        if plot_obj['plot_id'] == plot_id_to_find:
                            for obj in plot_obj['objects']:
                                if obj['object_data'] is not None:
                                    object_data = json.loads(obj['object_data'])
                                    if object_data['grow_time'] == "0":
                                        plot_object_harvest.append(obj['id'])
                    if len(plot_object_harvest) > 0:
                        harvest = pig.harvest_all(plot_object_harvest)
                        print(f'Plot : {plot_id} : {harvest}')
                        time.sleep(0.1)

                farm = pig.farm_load()
                if 'users_plot_objects' in farm:
                    users_plot_objects = farm['users_plot_objects']
                    plot_id_to_find = plot_id
                    plot_object_sowseed = []
                    for plot_obj in users_plot_objects:
                        if plot_obj['plot_id'] == plot_id_to_find:
                            for obj in plot_obj['objects']:
                                if obj['object_data'] is None:
                                    plot_object_sowseed.append(obj['id'])
                    if len(plot_object_sowseed) > 0:
                        sowseed = pig.sowseed_all(plot_object_sowseed)
                        print(f'Plot : {plot_id} : {sowseed}')
                        time.sleep(0.1)

                farm = pig.farm_load()
                if 'users_plot_objects' in farm:
                    users_plot_objects = farm['users_plot_objects']
                    plot_id_to_find = plot_id
                    plot_object_water = []
                    for plot_obj in users_plot_objects:
                        if plot_obj['plot_id'] == plot_id_to_find:
                            for obj in plot_obj['objects']:
                                if obj['object_data'] is not None:
                                    object_data = json.loads(obj['object_data'])
                                    if object_data['water_time'] == "0":
                                        plot_object_water.append(obj['id'])
                    if len(plot_object_water) > 0:
                        water = pig.farm_water(plot_object_water)
                        print(f'Plot : {plot_id} : {water}')
                        time.sleep(0.1)

            barn = pig.barn()
            print(f'corn : {barn}')
            if int(barn) > 1000:
                sell = pig.farm_sell()
                print(sell)

            stall_id = user["stall_id"]
            for stall in stall_id:
                pig_food = pig.pig_data(stall)[0]["pig_food"]
                print(f'Stall {stall} : Food : {pig_food}')
                time.sleep(0.1)
                chack_massage = pig.chack_massage(stall)['pig_massage_time']
                print(f'Stall {stall} : Message : {chack_massage}')
                time.sleep(0.1)
                chack_shower = pig.chack_shower(stall)['pig_shower_time']
                print(f'Stall {stall} : Shower : {chack_shower}')
                time.sleep(0.1)
                if int(pig_food) < -10:
                    eat_food = pig.food(9, stall)
                    pig.water(stall)
                    print(f'stall {stall} : eat food : {eat_food}')
                    time.sleep(0.1)
                if int(chack_massage) < 0:
                    massage = pig.massage(stall)
                    print(f'stall {stall} : massage : {massage}')
                    time.sleep(0.1)
                if int(chack_shower) < 0:
                    shower = pig.shower(stall)
                    print(f'stall {stall} : Shower : {shower}')
                    time.sleep(0.1)

            stall = user["stall_id"]
            for stall_id in stall:
                item_id = []
                pick_item = pig.load_item(user_id, stall_id)
                time.sleep(0.1)
                print(pick_item)
                if pick_item is not None:
                    for i in pick_item:
                        item_id.append(i['id'])
                    if len(item_id) > 0:
                        pick = pig.pick_item(user_id, item_id)
                        print(pick)
                        time.sleep(0.1)

    except Exception as e:
        print("เกิดข้อผิดพลาด:", e)
