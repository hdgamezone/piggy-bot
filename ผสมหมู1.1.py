import time
import pandas as pd
from lib.piggy_lib import API_Piggy
from lib.piggy_lib import API_Login
import json
import tkinter as tk
from tkinter import Spinbox

fcmtoken = "cHRXV3hxQoeuOsMP3rYfqd:APA91bG-CzprE-YW6AeokG1pJe9lvGM034UUCZgoHVfYLL8RDixvbBMwCcjii93iehwOeRORZNbLvWP38-dTHwOWxah1CbPNUpEEQRj_JFgpZCjWApcr8L4aWDB6rIbfuEz7-RYdCCnJ"
line_token ="vrxieWZ0i7pNJADIISaD8tPkxmFw0At06eHP0lbZd7q"

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
global userid, token
def login():
    global userid, token
    token_login = API_Login.login(logins[0]["userid"], logins[0]["fbtoken"], logins[0]["fcmtoken"])
    userid = token_login['userid']
    token = token_login['jwttoken']
    print(token_login)
    text.insert(tk.END, f"ID: {token_login['userid']}\n")
    text.insert(tk.END, f"Token: {token_login['jwttoken']}\n")

def loadpig():
    input_id = entry_id.get()
    game = API_Piggy(userid,token,line_token)
    pig_data = game.farm_load(input_id,13)
    listbox.delete(0, tk.END)
    for pig in pig_data['users_pigs']:
        pig_info = f"ID: {pig['id']} - pig id: {pig['pig_id']}"
        print(pig_info)
        listbox.insert(tk.END, pig_info)




root = tk.Tk()
root.title("Piggy Bot")
root.geometry("700x500")

bt_login = tk.Button(root, text="Login", command=login)
bt_login.place(x=20, y=10)

bt_load_pig = tk.Button(root, text="Load Pig", command=loadpig)
bt_load_pig.place(x=300, y=40)

text = tk.Text(root,width=82, height=10)
text.place(x=20, y=320)

listbox = tk.Listbox(root,width=40, height=18)
listbox.place(x=440, y=10)

entry_id = tk.Entry(root)
entry_id.place(x=300, y=10)


root.mainloop()