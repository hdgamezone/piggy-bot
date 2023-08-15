import time
import pandas as pd
from lib.lib_farm import API_Piggy
from lib.lib_farm import API_login
import json

user_id = "1799869087014887"
fb_token = ",xev*,xaz*,xaz*tuy,xaz*,xgt*4PKo,xby*O85PkqnZ,xcx*5aHsyonyIf,xcx*4g,xev*vKxpp5n3OJ9Z,xby*Q9sY3J0U,xaz*UkXk4qq1qrfw9OUxSyNIT,xev*,xev*4I16PZ,xby*T6iOZ,xby*,xfu*Pd7LJx,xcx*X4TQP1UV,xfu*W,xcx*uks,xev*MJeQN,xdw*Oso1Z,xaz*RMp7,xfu*,xcx*2V,xgt*kVfzR,xdw*,xaz*6ygfzYO7,xev*gImuZ,xby*V7IdaZ,xaz*ViXT2YKo4I3IV,xaz*gImcT,xfu*xseaTz1K3,xaz*,xev*,xev*HZ,xcx*t8uRy,xfu*qudKmIh,xev*0M51RTU,xev*w,xgt*u3tO8VtJh5Z,xaz*i5m,xfu*fub,xcx*0QZ,xdw*Z,xdw*"
fcmtoken = "cHRXV3hxQoeuOsMP3rYfqd:APA91bG-CzprE-YW6AeokG1pJe9lvGM034UUCZgoHVfYLL8RDixvbBMwCcjii93iehwOeRORZNbLvWP38-dTHwOWxah1CbPNUpEEQRj_JFgpZCjWApcr8L4aWDB6rIbfuEz7-RYdCCnJ"
line_token = ""

login = API_login.login(user_id,fb_token,fcmtoken)
game_id = login['userid']
game_token = login['jwttoken']

users = [
    {
        "user_id": game_id,
        "Token_id": game_token,
        "line": "vrxieWZ0i7pNJADIISaD8tPkxmFw0At06eHP0lbZd7q",
        "plots_to_check": ["1", "2", "3", "4"],
        "stall_id": [2,3,4,5,6,7,8,9,10,13]
    },
]

time_farm = []

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
                for stall_time in time_farm:
                    if stall_time['stall'] == stall:
                        if stall_time['time_food'] < time.time():
                            pig_food = pig.pig_data(stall)[0]["pig_food"]
                            print(f'Stall {stall} : Food : {pig_food}')
                            time.sleep(0.1)

                        chack_massage = pig.chack_massage(stall)['pig_massage_time']
                        print(f'Stall {stall} : Message : {chack_massage}')
                        time.sleep(0.1)

                        chack_shower = pig.chack_shower(stall)['pig_shower_time']
                        print(f'Stall {stall} : Shower : {chack_shower}')
                        time.sleep(0.1)

                time_data = {
                    'stall': stall,
                    'time_food': time.time() + int(pig_food),
                    'time_massage': time.time() + int(chack_massage),
                    'time_shower': time.time() + int(chack_shower),
                }
                time_farm.append(time_data)

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

