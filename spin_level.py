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

game = API_Piggy(game_id,game_token,line_token)

for i in range(1000):
    try:
        spin = game.spin()
        time.sleep(0.2)
        print(f'{i} : {spin}')
    except:
        time.sleep(2)
        pass
