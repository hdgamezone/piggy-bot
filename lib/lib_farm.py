import requests
import subprocess
import os
import time
import json
import urllib.parse


class API_login():
    def login(userid, fbtoken, fcmtoken):
        url = "https://api-piggy.codedefeat.com/v29/api/users/register/"

        headers = {
            "Host": "api-piggy.codedefeat.com",
            "User-Agent": "UnityPlayer/2020.3.48f1 (UnityWebRequest/1.0, libcurl/7.84.0-DEV)",
            "Accept": "*/*",
            "X-Unity-Version": "2020.3.48f1"
        }

        data = {
            "userid": userid,
            "fbtoken": fbtoken,
            "fcmtoken": fcmtoken
        }

        response = requests.post(url, headers=headers, data=data)
        return response.json()


class API_Piggy():
    def __init__(self, userid, Tokenid, Token_line):
        self.userid = userid
        self.Tokenid = Tokenid
        self.Token_line = Token_line
        # self.proxy = proxy

    def headers(self):
        headers = {
            'Host': 'api-piggy.codedefeat.com',
            'User-Agent': 'UnityPlayer/2020.3.41f1 (UnityWebRequest/1.0, libcurl/7.84.0-DEV)',
            'Accept': '*/*',
            'Authorization': f'Bearer {self.Tokenid}',
            'X-Unity-Version': '2020.3.41f1',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        return headers

    def headers2(self):
        headers = {
            'Host': 'api-piggy.codedefeat.com',
            'User-Agent': 'UnityPlayer/2020.3.48f1 (UnityWebRequest/1.0, libcurl/7.84.0-DEV)',
            'Accept': '*/*',
            'Authorization': f'Bearer {self.Tokenid}',
            'X-Unity-Version': '2020.3.48f1',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        return headers

    def medicine11(self, pig_id):
        url = "https://api-piggy.codedefeat.com/v29/api/users/backpack/category/medicine/use/"
        headers = {
            "Host": "api-piggy.codedefeat.com",
            "User-Agent": "UnityPlayer/2020.3.48f1 (UnityWebRequest/1.0, libcurl/7.84.0-DEV)",
            "Accept": "*/*",
            "Authorization": f'Bearer {self.Tokenid}',
            "X-Unity-Version": "2020.3.48f1"
        }
        json_data = json.dumps({"pigid": pig_id})
        data = {
            "userid": self.userid,
            "pig_lists": json_data,
            "item_id": "11",
            "item_category": "medicine"
        }

        response = requests.post(url, headers=headers, data=data)
        return response.json()

    def pick_item(self, user_id, item_id):
        url = "https://api-piggy.codedefeat.com/v29/api/users/itempickup/"
        headers = {
            "Host": "api-piggy.codedefeat.com",
            "User-Agent": "UnityPlayer/2020.3.48f1 (UnityWebRequest/1.0, libcurl/7.84.0-DEV)",
            "Accept": "*/*",
            "Authorization": f'Bearer {self.Tokenid}',
            "X-Unity-Version": "2020.3.48f1"
        }
        json_data = json.dumps({"itemid": item_id})
        data = {
            "userid": user_id,
            "item_list": json_data
        }

        response = requests.post(url, headers=headers, data=data)
        return response.json()

    def chack_food(self, item_id, stall_id):
        data = {
            'userid': self.userid,
            'stall_id': stall_id,
            'food_id': item_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/feed/check/',
                                 headers=self.headers(), data=data)
        return response.json()

    def food(self, item_id, stall_id):
        data = {
            'userid': self.userid,
            'stall_id': stall_id,
            'food_id': item_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/feed/confirm/',
                                 headers=self.headers(), data=data)
        return response.json()

    def water(self, stall_id):
        self.stall_id = stall_id
        data = {
            'userid': self.userid,
            'stall_id': stall_id,
            'food_id': '0',
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/feed/confirm/',
                                 headers=self.headers(), data=data)
        return response.json()

    def chack_shower(self, stall_id):
        self.stall_id = stall_id
        data = {
            'userid': self.userid,
            'stall_id': stall_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/shower/check/',
                                 headers=self.headers(), data=data)
        return response.json()

    def shower(self, stall_id):
        self.stall_id = stall_id
        data = {
            'userid': self.userid,
            'stall_id': stall_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/shower/confirm/',
                                 headers=self.headers(), data=data)
        return response.json()

    def chack_massage(self, stall_id):
        self.stall_id = stall_id
        data = {
            'userid': self.userid,
            'stall_id': stall_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/massage/check/',
                                 headers=self.headers(), data=data)
        return response.json()

    def massage(self, stall_id):
        self.stall_id = stall_id
        data = {
            'userid': self.userid,
            'stall_id': stall_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/massage/confirm/',
                                 headers=self.headers(), data=data)
        return response.json()

    def userinfo(self):
        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/userinfo/backpack/',
                                 headers=self.headers())
        return response.json()

    def buyfood(self, item_id, amount):
        data = {
            'food_id': item_id,
            'amount': amount,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/shopmanager/buy/foods/',
                                 headers=self.headers(), data=data)

    def line(self, msgtex):
        self.msgtex = msgtex
        url = 'https://notify-api.line.me/api/notify'
        token = self.Token_line
        headersline = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}

        msg = self.msgtex
        r = requests.post(url, headers=headersline, data={'message': msg})
        print(r.text)

    def friend_massage_chack(self, friend_id, stall_id):
        self.friend_id = friend_id
        self.stall_id = stall_id
        data = {
            'userid': self.friend_id,
            'stall_id': self.stall_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/massage/check/',
                                 headers=self.headers(), data=data)
        return response.json()

    def friend_massage(self, friend_id, stall_id):
        self.friend_id = friend_id
        data = {
            'userid': self.friend_id,
            'stall_id': stall_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/massage/confirm/',
                                 headers=self.headers(), data=data)
        return response.json()

    def friends_list(self):

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/friends/lists/',
                                 headers=self.headers())
        return response.json()['friends_lists']

    def frirnds_chack_shower(self, friend_id, stall_id):
        data = {
            'userid': friend_id,
            'stall_id': stall_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/shower/check/',
                                 headers=self.headers(), data=data)
        return response.json()

    def frirnds_shower(self, friend_id, stall_id):
        data = {
            'userid': friend_id,
            'stall_id': stall_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/shower/confirm/',
                                 headers=self.headers(), data=data)
        return response.json()

    def friends_stall_count(self, friend_id):
        data = {
            'userid': friend_id,
            'stall_id': '1',
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/userinfo/farm/load/',
                                 headers=self.headers(), data=data)
        return response.json()['users_buildings']['stall_count']

    def friend_chack_food(self, friend_id, stall_id):
        data = {
            'userid': friend_id,
            'stall_id': stall_id,
            'food_id': '9',
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/feed/check/',
                                 headers=self.headers(), data=data)
        return response.json()

    def friend_food(self, friend_id, stall_id, item_id):
        data = {
            'userid': friend_id,
            'stall_id': stall_id,
            'food_id': item_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/feed/confirm/',
                                 headers=self.headers(), data=data)
        return response.json()

    def user_data(self):
        data = {
            'userid': self.userid,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/userinfo/data/',
                                 headers=self.headers(), data=data)
        return response.json()

    def friend_water(self, friend_id, stall_id):
        data = {
            'userid': friend_id,
            'stall_id': stall_id,
            'food_id': '0',
        }
        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/feed/confirm/',
                                 headers=self.headers(), data=data)
        return response.json()

    def level_up(self):
        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/levelup/', headers=self.headers())
        return response.json()

    def spin(self):

        data = {
            'type': '1',
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/spins/confirm/',
                                 headers=self.headers(), data=data)
        return response.json()['reward']

    def open_box(self, boxid):
        self.boxid = boxid
        data = {
            'box_id': boxid,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/backpack/category/box/use/',
                                 headers=self.headers(), data=data)
        return response.json()

    def stall_count(self):
        data = {
            'userid': self.userid,
            'stall_id': '1',
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/userinfo/farm/load/',
                                 headers=self.headers(), data=data)
        return response.json()['users_buildings']['stall_count']

    def get_ip(self):
        response = requests.get("https://ipinfo.io/", proxies=self.proxies)
        return response.json()

    def item_amount(self, item):
        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/userinfo/backpack/',
                                 headers=self.headers())
        for i in response.json()['users_backpack']:
            if item == "food14":
                if i['item_id'] == '14' and i['item_category'] == 'food':
                    return i['item_amount']
            if item == "box1":
                if i['item_id'] == '1' and i['item_category'] == 'box':
                    return i['item_amount']
            if item == "box2":
                if i['item_id'] == '2' and i['item_category'] == 'box':
                    return i['item_amount']
            if item == "medicine5":
                if i['item_id'] == '5' and i['item_category'] == 'medicine':
                    return i['item_amount']
            if item == "food5":
                if i['item_id'] == '5' and i['item_category'] == 'food':
                    return i['item_amount']
            if item == "food9":
                if i['item_id'] == '9' and i['item_category'] == 'food':
                    return i['item_amount']

    def get_id(self):
        hwid = str(
            str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
        return hwid

    def pig_data(self, stall_id):
        data = {
            'userid': self.userid,
            'stall_id': stall_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/userinfo/farm/refresh/',
                                 headers=self.headers(), data=data)
        return response.json()['users_pigs']

    def item_data(self, stall_id):
        data = {
            'userid': self.userid,
            'stall_id': stall_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/userinfo/farm/refresh/',
                                 headers=self.headers(), data=data)
        return response.json()['users_pigs_items']

    def item_pickup(self, item_id):
        data = f'userid=1799869087014887&item_list=%7b%22itemid%22%3a%5b{item_id}%5d%7d'

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/itempickup/', headers=self.headers2(),
                                 data=data)
        return response.json

    def sell_pig(self, pigid):
        data = {
            'pigid': pigid,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/sells/', headers=self.headers(),
                                 data=data)
        return response.json()

    def buy_pig(self, stall_id, pig_id, amount):
        data = {
            'stall_id': stall_id,
            'pig_id': pig_id,
            'amount': amount,
        }
        response = requests.post('https://api-piggy.codedefeat.com/v28/api/shopmanager/buy/pigs/',
                                 headers=self.headers(), data=data)
        return response.json()

    def user_info(self, stall_id):
        data = {
            'userid': self.userid,
            'stall_id': stall_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/userinfo/farm/refresh/',
                                 headers=self.headers(), data=data)
        return response.json()['users_pigs']

    def use_medicine_11(self, pig_id):
        data = f'userid=1799869087014887&pig_lists=%7b%22pigid%22%3a%5b{pig_id}%5d%7d&item_id=11&item_category=medicine'

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/backpack/category/medicine/use/',
                                 headers=self.headers(), data=data, )
        return response.json()

    def load_pig(self, userid, stall_id):
        data = {
            'userid': userid,
            'stall_id': stall_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/userinfo/farm/load/',
                                 headers=self.headers(), data=data)
        return response.json()["users_pigs"]

    def load_item(self, userid, stall_id):
        data = {
            'userid': userid,
            'stall_id': stall_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/userinfo/farm/load/',
                                 headers=self.headers(), data=data)
        return response.json()["users_pigs_items"]

    def pig_sick(self, stall_id, pigid):
        data = {
            'userid': '1799869087014887',
            'stall_id': stall_id,
            'pigid': pigid,
            'item_id': '4',
            'item_category': 'medicine',
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/backpack/category/medicine/use/',
                                 headers=self.headers(), data=data)
        return response.json()

    def pig_soul(self, pig_id):
        data = {
            'userid': self.userid,
            'pigid': pig_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/pigs/dead/soul/',
                                 headers=self.headers(), data=data)
        return response.json()

    def friend_delete(self, friend_id):
        data = {
            'userid': friend_id,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/friends/delete/',
                                 headers=self.headers(), data=data)
        return response.json()

    # ================farm===============================================================
    def farm_load(self):
        data = {
            'userid': self.userid,
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/farm/plot/load/',
                                 headers=self.headers(), data=data)
        return response.json()

    def harvest(self, plot_object_id):
        data = f'plot_objectids=%7b%22data%22%3a%5b{plot_object_id}%5d%7d'
        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/farm/plant/harvest/',
                                 headers=self.headers(), data=data)
        return response.json()

    def harvest_all(self, plot_object_ids):
        data = f'plot_objectids=%7b%22data%22%3a%5b{",".join(plot_object_ids)}%5d%7d'
        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/farm/plant/harvest/',
                                 headers=self.headers(), data=data)
        return response.json()

    def sowseed(self, plot_object_id):
        data = f'id=1&plot_objectids=%7b%22data%22%3a%5b{plot_object_id}%5d%7d'

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/farm/shop/sowseed/',
                                 headers=self.headers(), data=data)
        return response.json()

    def sowseed_all(self, plot_object_id):
        data = f'id=1&plot_objectids=%7b%22data%22%3a%5b{",".join(plot_object_id)}%5d%7d'

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/farm/shop/sowseed/',
                                 headers=self.headers(), data=data)
        return response.json()

    def barn(self):
        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/userinfo/backpack/',
                                 headers=self.headers())
        for i in response.json()['users_backpack']:
            if i['item_id'] == '57' and i['item_category'] == 'item':
                return i['item_amount']

    def farm_sell(self):
        data = {
            'id': '1',
            'amount': '1000',
        }

        response = requests.post('https://api-piggy.codedefeat.com/v28/api/users/farm/barn/market/sell/',
                                 headers=self.headers(), data=data)
        return response.json()

    def farm_water(self, plot_object_id):
        data = f'userid=1799869087014887&plot_objectids=%7b%22data%22%3a%5b{",".join(plot_object_id)}%5d%7d'

        response = requests.post('https://api-piggy.codedefeat.com/v29/api/users/farm/plant/water/',
                                 headers=self.headers(), data=data)
        return response.json()

