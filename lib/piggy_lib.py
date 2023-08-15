import requests
import json

class API_Login():
    def login(user_id, fbtoken,fcmtoken,proxy=None):
        url = "https://api-piggy.codedefeat.com/v29/api/users/register/"

        headers = {
            "Host": "api-piggy.codedefeat.com",
            "User-Agent": "UnityPlayer/2020.3.48f1 (UnityWebRequest/1.0, libcurl/7.84.0-DEV)",
            "Accept": "*/*",
            "X-Unity-Version": "2020.3.48f1"
        }

        data = {
            "userid": user_id,
            "fbtoken": fbtoken,
            "fcmtoken": fcmtoken
        }

        response = requests.post(url, headers=headers, data=data, proxies=proxy)
        return response.json()

class API_Piggy():
    def __init__(self, userid, Tokenid, Token_line, proxy=None):
        self.userid = userid
        self.Tokenid = Tokenid
        self.Token_line = Token_line
        self.proxy = proxy

    def headers(self):
        headers = {
            "Host": "api-piggy.codedefeat.com",
            "User-Agent": "UnityPlayer/2020.3.48f1 (UnityWebRequest/1.0, libcurl/7.84.0-DEV)",
            "Accept": "*/*",
            "Authorization": f'Bearer {self.Tokenid}',
            "X-Unity-Version": "2020.3.48f1",
        }
        return headers

    def spin(self,):
        url = "https://api-piggy.codedefeat.com/v29/api/users/spins/confirm/"
        data = {"type": "1"}

        response = requests.post(url, headers=self.headers(), data=data)
        return  response.json()

    def user_info(self):
        url = "https://api-piggy.codedefeat.com/v29/api/users/userinfo/data/"
        data = {"userid": self.userid}

        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()

    def feed_confirm(self,userid,stall_id,food_id):
        url = "https://api-piggy.codedefeat.com/v29/api/users/pigs/feed/confirm/"
        data = {
            "userid": userid,
            "stall_id": stall_id,
            "food_id": food_id
        }

        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()

    def levelup(self):
        url = "https://api-piggy.codedefeat.com/v29/api/users/levelup/"
        data = {}
        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()

    def backpack(self):
        url = "https://api-piggy.codedefeat.com/v29/api/users/userinfo/backpack/"
        data = {}
        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()

    def place_object(self,plot_id, x, y):
        url = "https://api-piggy.codedefeat.com/v29/api/users/farm/shop/placeobject/"
        data = {
            "id": "1",
            "type": "object",
            "plot_id": str(plot_id),
            "position": f'{{"x":{x},"y":{y}}}',  # ใส่ค่า x และ y เข้าไปในข้อมูล
        }

        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()

    def pig_data(self,userid, stall_id):
        url = "https://api-piggy.codedefeat.com/v28/api/users/userinfo/farm/refresh/"
        data = {
            'userid': userid,
            'stall_id': stall_id,
        }

        response = requests.post(url, headers=self.headers(), data=data)

        return response.json()#['users_pigs']

    def farm_load(self,userid,stall_id):
        data = {
            "userid": userid,
            "stall_id": stall_id
        }

        url = "https://api-piggy.codedefeat.com/v29/api/users/userinfo/farm/load/"

        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()

    def steal(self, userid, pig_id):
        url = 'https://api-piggy.codedefeat.com/v29/api/users/pigs/steal/confirm/'
        data = {
            'userid': userid,
            'pigid': pig_id,
        }

        response = requests.post(url, headers=self.headers(), data=data)

        return response.json()

    def chack_steal(self, userid, pig_id):
        url = 'https://api-piggy.codedefeat.com/v29/api/users/pigs/steal/check/'
        data = {
            'userid': userid,
            'stall_id': pig_id,
        }

        response = requests.post(url,headers=self.headers(), data=data)
        return response.json()

    def add_friend(self,userid):
        data = {
            "userid": userid
        }

        url = "https://api-piggy.codedefeat.com/v29/api/users/friends/request/send/"

        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()

    def search_friends(self,text):
        data = {
            "text": text
        }

        url = "https://api-piggy.codedefeat.com/v29/api/users/friends/search/"

        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()

    def stall_count(self,userid,stall_id):
        url = "https://api-piggy.codedefeat.com/v29/api/users/userinfo/farm/load/"
        data = {
            "userid": userid,
            "stall_id": stall_id
        }

        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()['users_buildings']['stall_count']

    def craftitems(self,craft_id,craft_amount):
        url = "https://api-piggy.codedefeat.com/v29/api/users/craftitems/pigs/accept/"
        data = {
            "craft_id": craft_id,
            "craft_amount": craft_amount
        }
        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()

    def friends_lists(self):
        url = "https://api-piggy.codedefeat.com/v29/api/users/friends/lists/"
        data = {
            "search_text": ""
        }
        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()['friends_lists']

    def poison(self,userid,stall_id,item_id):
        data = {
            "userid": str(userid),
            "stall_id": str(stall_id),
            "item_id": str(item_id)
        }

        url = "https://api-piggy.codedefeat.com/v29/api/users/pigs/poison/confirm/"

        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()

    def check_poison(self, userid):
        url = "https://api-piggy.codedefeat.com/v29/api/users/pigs/poison/check/"
        data = {
            "userid": userid
        }
        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()

    def send_gift(self, user_id, pig_gifts):
        url = "https://api-piggy.codedefeat.com/v29/api/users/gifts/send/accept/"
        data = {
            "userid": user_id,
            "pig_lists": json.dumps({"pigid": pig_gifts})
        }
        print(data)
        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()

    def delete_friend(self, user_id):
        url = "https://api-piggy.codedefeat.com/v29/api/users/friends/delete/"
        data = {
            "userid": user_id
        }

        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()

    def open_box(self,box_id):
        url = "https://api-piggy.codedefeat.com/v29/api/users/backpack/category/box/use/"
        data = {
            "box_id": box_id
        }

        response = requests.post(url, headers=self.headers(), data=data)
        return response.json()