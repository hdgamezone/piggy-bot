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