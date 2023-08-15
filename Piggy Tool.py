import time
import pandas as pd
from lib.piggy_lib import API_Piggy
from lib.piggy_lib import API_Login
import json
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog,Toplevel

fcmtoken = "fm446RpWSIa6E56hxAXWfU:APA91bEEPMbMIA6GwphJFAETzMd-uyL3MGPIHckXOgSeBH5TPDnb3OytYJGhvlR53ECloU9bWHoq_0qTyL7uW_j5eipLCSO1N4I11SUr-Hyg9MILQCRburlQtK9CXd5wxcsQ9hMwARXs"
line_token ="vrxieWZ0i7pNJADIISaD8tPkxmFw0At06eHP0lbZd7q"

logins = []
logins.clear()
with open('login.json', 'r') as file:
    logins = json.load(file)
print(logins)

token_data = []
with open('credentials.json', 'r') as file:
    token_data = json.load(file)
print(token_data)

root = tk.Tk()
root.title("Piggy Bot")
root.geometry("710x500")
combobox_id = tk.ttk.Combobox(root, values=list(token_data.keys()),width=17, height=25)
combobox_id.place(x=10, y=10)
first_user_id = list(token_data.keys())[0]
combobox_id.set(first_user_id)

global userid, token
friend = []
def gen_token():
    global userid, token,logins,token_data
    logins.clear()
    with open('login.json', 'r') as file:
        logins = json.load(file)
    print(logins)
    combobox_id['values'] = []
    for ligin in logins:
        token_login = API_Login.login(ligin["userid"], ligin["fbtoken"], fcmtoken)
        print(token_login)
        userid = token_login['userid']
        token = token_login['jwttoken']
        combobox_id['values'] = (*combobox_id['values'], userid)
        save_credentials(userid, token)

    token_data.clear()
    with open('credentials.json', 'r') as file:
        token_data = json.load(file)
    print(token_data)


def login():
        global userid, token,game
        friend.clear()
        userid = combobox_id.get()
        token = token_data[userid]
        print(userid)
        print(token)
        game = API_Piggy(userid, token, line_token)
        user_data = game.user_info()
        user_data = user_data['users_data']
        print(user_data)
        leafcoin = user_data["leafcoins"]
        formatted_leafcoin = "{:,}".format(int(leafcoin))
        coins = user_data["coins"]
        formatted_coins = "{:,}".format(int(coins))
        cash = user_data["cash"]
        formatted_cash = "{:,}".format(int(cash))
        text.insert(tk.END,f'\nName: {user_data["fbname"]}\nLV.: {user_data["level"]}\nCoins: {formatted_coins}\nCash: {formatted_cash}\nLeafcoin: {formatted_leafcoin}\n')
        text.see(tk.END)
        combobox_IDS.delete(0, tk.END)  # ลบข้อมูลเดิมใน entry_id
        user_da = {
            'userid': userid,
            'fbname': user_data['fbname'],
            'level': user_data['level']
        }
        friend.append(user_da)
        friend_list = game.friends_lists()
        for item in friend_list:
            user_info = {
                'userid': item['userid'],
                'fbname': item['fbname'],
                'level': item['level']
            }
            friend.append(user_info)
        combobox_IDS['values'] = [info['fbname'] for info in friend]

def save_credentials(userid, token):
    try:
        with open('credentials.json', 'r') as file:
            # โหลดข้อมูลเดิมจากไฟล์
            credentials = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        credentials = {}

    # อัพเดทหรือเพิ่มรายการใหม่ด้วย userid และ token
    credentials[userid] = token

    # เขียนข้อมูลลงในไฟล์
    with open('credentials.json', 'w') as file:
        json.dump(credentials, file)

def load_credentials():
    try:
        # เปิดไฟล์สำหรับการอ่าน
        with open('credentials.json', 'r') as file:
            # โหลดข้อมูลจากไฟล์และแปลงเป็น dictionary
            credentials = json.load(file)
            return credentials['userid'], credentials['token']
    except FileNotFoundError:
        print("Credentials file not found.")
        return None, None

def loadpig():
    selected_name = combobox_IDS.get()  # รับข้อมูลที่เลือกจาก combobox_IDS
    selected_user = None
    for user_info in friend:
        if user_info['fbname'] == selected_name:
            selected_user = user_info
            break
    if selected_user:
        game = API_Piggy(userid, token, line_token)
        stall = game.stall_count(selected_user['userid'], 1)
        stall_list = list(range(1, int(stall) + 1))  # แปลง stall เป็นตัวเลข
        combobox_stall['values'] = stall_list
        selected_stall = combobox_stall.get()

        pig_data = game.farm_load(selected_user['userid'],selected_stall)
        listbox.delete(0, tk.END)
        print(pig_data['users_pigs'])
        if pig_data['users_pigs'] is not None:
            for pig in pig_data['users_pigs']:
                pig_info = f"ID: {pig['id']} - pig id: {pig['pig_id']} - weight: {pig['pig_weight']}"
                print(pig_info)
                listbox.insert(tk.END, pig_info)
        else:
            listbox.insert(tk.END,"ไม่มีหมู")



def steal():
    selected_name = combobox_IDS.get()  # รับข้อมูลที่เลือกจาก combobox_IDS
    selected_user = None
    for user_info in friend:
        if user_info['fbname'] == selected_name:
            selected_user = user_info
            break
    if selected_user:
        selected_item_index = listbox.curselection()
        game = API_Piggy(userid, token, line_token)
        if selected_item_index:
            selected_item = listbox.get(selected_item_index[0])
            id_value = selected_item.split(" - ")[0].split(": ")[1]
            chack_steal = game.chack_steal(selected_user['userid'],id_value)
            #text.insert(tk.END, f"Chack steal: {chack_steal}\n")
            steal = game.steal(selected_user['userid'],id_value)
            text.insert(tk.END, f"Steal: {steal}\n")
            text.see(tk.END)

def craftitems():
    selected_craf = combobox_craf.get()
    if selected_craf =="หมูโทเมะ":
        claf_id = 4
    if selected_craf =="หมูคอร์น":
        claf_id = 5
    game = API_Piggy(userid, token, line_token)
    craft_amount = simpledialog.askinteger("Craft Items", "Enter craft amount:")
    if craft_amount is None:
        return
    result = messagebox.askokcancel("Confirmation", f"Do you want to craft {selected_craf} ?")
    if result:
        craf = game.craftitems(claf_id,craft_amount)
        print(craf)

def add_friend():
    game = API_Piggy(userid, token, line_token)
    user = entry_id.get()
    add = game.add_friend(user)
    text.insert(tk.END, f"addfriend: {add}\n")
    text.see(tk.END)

def delete_friend():
    selected_name = combobox_IDS.get()  # รับข้อมูลที่เลือกจาก combobox_IDS
    selected_user_id = None
    for user_info in friend:
        if user_info['fbname'] == selected_name:
            selected_user_id = user_info['userid']
            break
    if selected_user_id:
        game = API_Piggy(userid, token, line_token)
        result = game.delete_friend(selected_user_id)
        if result:  # ตรวจสอบว่าการลบเพื่อนสำเร็จหรือไม่
            # อัปเดต combobox_IDS โดยลบรายการที่ถูกเลือก
            current_values = list(combobox_IDS['values'])
            current_values.remove(selected_name)
            combobox_IDS['values'] = current_values
            text.insert(tk.END, f"ลบเพื่อน: {selected_name}\n")
            text.see(tk.END)
        else:
            text.insert(tk.END, f"ไม่สามารถลบเพื่อน: {selected_name}\n")
            text.see(tk.END)
        print(result)
def search():
    game = API_Piggy(userid, token, line_token)
    user = entry_id.get()
    search_friend = game.search_friends(user)
    if search_friend['friends_lists'] is not None:
        for item in search_friend['friends_lists']:
            user_info = {
                'userid': item['userid'],
                'fbname': item['fbname'],
                'level': item['level']
            }
        if user_info not in friend:
            friend.append(user_info)
        combobox_values = list(combobox_IDS['values'])
        new_friend_names = [info['fbname'] for info in friend if info['fbname'] not in combobox_values]
        # เพิ่มรายการใหม่เข้าไปใน list
        combobox_values += new_friend_names
        # แปลงกลับเป็น tuple และอัปเดตค่าใน Combobox
        combobox_IDS['values'] = tuple(combobox_values)

def use_poison():
    selected_name = combobox_IDS.get()  # รับข้อมูลที่เลือกจาก combobox_IDS
    selected_user = None
    for user_info in friend:
        if user_info['fbname'] == selected_name:
            selected_user = user_info
            break
    if selected_user:
        game = API_Piggy(userid, token, line_token)
        stall = game.stall_count(selected_user['userid'], 1)
        stall_list = list(range(1, int(stall) + 1))  # แปลง stall เป็นตัวเลข
        combobox_stall['values'] = stall_list
        selected_stall = combobox_stall.get()
        selected_poison = combobox_poison.get()
        if selected_poison == "ยาถ่าย":
            poison_id = "6"
            check_poison = game.check_poison(selected_user['userid'])
            poison = game.poison(selected_user['userid'],selected_stall,poison_id)
            print(poison)
            text.insert(tk.END, f"Poison: {poison}\n")
            text.see(tk.END)
            loadpig()

#/////////////////////////////////////////////////////////////////////////////////////////////////
def send_pig():
    root_sendpig = tk.Toplevel(root)  # สร้างหน้าต่างย่อย
    root_sendpig.title("Send Pig")
    root_sendpig.geometry("665x500")
    list_pig = tk.Listbox(root_sendpig, width=50, height=25, selectmode='multiple')
    list_pig.place(x=10, y=10)
    list_pigresive = tk.Listbox(root_sendpig, width=50, height=25, selectmode='multiple')
    list_pigresive.place(x=350, y=10)
    bt_S_load_pig = tk.Button(root_sendpig, text="Load Pig", command=lambda: send_loadpig(list_pig, list_pigresive))
    bt_S_load_pig.place(x=10, y=420)
    bt_S_move_back = tk.Button(root_sendpig, text="Move Back", command=lambda: move_back_pig(list_pig, list_pigresive))
    bt_S_move_back.place(x=350, y=420)
    bt_S_move_to = tk.Button(root_sendpig, text="Move TO", command=lambda: move_pig(list_pig, list_pigresive))
    bt_S_move_to.place(x=250, y=420)
    entry_idf = tk.Entry(root_sendpig)
    entry_idf.place(x=430, y=425)
    bt_confirm_send = tk.Button(root_sendpig, text="Confirm Send", command=lambda:confirm_send(list_pigresive,entry_idf))
    bt_confirm_send.place(x=570, y=420)

    send_loadpig(list_pig, list_pigresive)

def send_loadpig(list_pig, list_pigresive):
    selected_name = combobox_IDS.get()  # รับข้อมูลที่เลือกจาก combobox_IDS
    selected_user = None
    for user_info in friend:
        if user_info['fbname'] == selected_name:
            selected_user = user_info
            break
    if selected_user:
        game = API_Piggy(userid, token, line_token)
        stall = game.stall_count(selected_user['userid'], 1)
        stall_list = list(range(1, int(stall) + 1))  # แปลง stall เป็นตัวเลข
        combobox_stall['values'] = stall_list
        selected_stall = combobox_stall.get()

        pig_data = game.farm_load(selected_user['userid'], selected_stall)
        list_pig.delete(0, tk.END)
        list_pigresive.delete(0, tk.END)
        if pig_data['users_pigs'] is not None:
            for pig in pig_data['users_pigs']:
                pig_info = f"ID: {pig['id']} - pig id: {pig['pig_id']} - weight: {pig['pig_weight']}"
                list_pig.insert(tk.END, pig_info)

        else:
            list_pig.insert(tk.END, "ไม่มีหมู")

def move_pig(list_pig, list_pigresive):
    selected_indices = list_pig.curselection()
    for index in selected_indices:
        pig_info = list_pig.get(index)
        list_pigresive.insert(tk.END, pig_info)
    for index in reversed(selected_indices):
        list_pig.delete(index)


def move_back_pig(list_pig, list_pigresive):
    print("Move back function called")  # เพิ่มเพื่อตรวจสอบการเรียกใช้ฟังก์ชัน
    selected_indices = list_pigresive.curselection()
    for index in selected_indices:
        pig_info = list_pigresive.get(index)
        list_pig.insert(tk.END, pig_info)
    for index in reversed(selected_indices):
        list_pigresive.delete(index)

def confirm_send(list_pigresive,entry_idf):
    pig_gifts = []
    game = API_Piggy(userid, token, line_token)
    id = entry_idf.get()

    for line in list_pigresive.get(0, tk.END):
        id_value = line.split(" - ")[0].split(": ")[1]
        pig_gifts.append(int(id_value))
    print(pig_gifts)
    send = game.send_gift(id,pig_gifts)
    print(send)
    text.insert(tk.END, f"Send Pig: {send}\n")
    text.see(tk.END)

#/////////////////////////////////////////////////////////////////////////
def load_data():
    with open('login.json', 'r') as file:
        return json.load(file)

def save_data(logins):
    with open('login.json', 'w') as file:
        json.dump(logins, file)

def edit_data():
    top_level = tk.Toplevel(root)
    top_level.geometry("665x500")
    tree = ttk.Treeview(top_level, columns=("UserID", "FBToken"), show="headings", height=17)
    tree.column("UserID", width=150)
    tree.column("FBToken", width=490)
    tree.heading("UserID", text="User ID")
    tree.heading("FBToken", text="FB Token")
    tree.place(x=10, y=10)

    logins = load_data()
    for login in logins:
        tree.insert('', tk.END, values=(login['userid'], login['fbtoken']))

    def add_data():
        userid = entry_userid.get()
        fbtoken = entry_fbtoken.get()
        logins.append({'userid': userid, 'fbtoken': fbtoken})
        save_data(logins)
        tree.insert('', tk.END, values=(userid, fbtoken))

    def delete_data():
        selected_item = tree.selection()[0]
        index = tree.index(selected_item)
        logins.pop(index)
        save_data(logins)
        tree.delete(selected_item)

    def update_data():
        selected_item = tree.selection()[0]
        index = tree.index(selected_item)
        userid = entry_userid.get()
        fbtoken = entry_fbtoken.get()
        logins[index] = {'userid': userid, 'fbtoken': fbtoken}
        save_data(logins)
        tree.item(selected_item, values=(userid, fbtoken))

    entry_userid = tk.Entry(top_level,width=25)
    entry_fbtoken = tk.Entry(top_level,width=60)
    entry_userid.place(x=20, y=390)
    entry_fbtoken.place(x=190, y=390)

    btn_add = tk.Button(top_level, text="Add", command=add_data)
    btn_add.place(x=580, y=385)

    btn_delete = tk.Button(top_level, text="Delete", command=delete_data)
    btn_delete.place(x=20, y=420)

    btn_update = tk.Button(top_level, text="Update", command=update_data)
    btn_update.place(x=80, y=420)

#////////////////////////////////////////////////////////////////////////
def toggle_loop():
    global running
    if running:
        running = False
        bt_openbox.config(text="Openbox")
    else:
        running = True
        bt_openbox.config(text="Stop")
        while running:
            box = game.open_box(combobox_box.get())
            text.insert(tk.END, f"Box: {box}\n")
            text.see(tk.END)
            time.sleep(0.1)
            root.update_idletasks()
            root.update()



running = False
bt_login = tk.Button(root, text="Login", command=login)
bt_login.place(x=10, y=40)
btn_edit = tk.Button(root, text="Edit Data", command=edit_data)
btn_edit.place(x=60, y=40)

bt_gen = tk.Button(root, text="GENTOKEN", command=gen_token)
bt_gen.place(x=10, y=70)

bt_load_pig = tk.Button(root, text="Load Pig", command=loadpig)
bt_load_pig.place(x=640, y=6)
bt_steal = tk.Button(root, text="Steal Pig", command=steal)
bt_steal.place(x=150, y=6)
bt_craftitems = tk.Button(root, text="craftitems", command=craftitems)
bt_craftitems.place(x=150, y=40)
bt_addf = tk.Button(root, text="add", command=add_friend)
bt_addf.place(x=150, y=70)
bt_delete_friend = tk.Button(root, text="ลบเพื่อน", command=delete_friend)
bt_delete_friend.place(x=185, y=70)
bt_search = tk.Button(root, text="search", command=search)
bt_search.place(x=240, y=70)
bt_search = tk.Button(root, text="poison", command=use_poison)
bt_search.place(x=150, y=100)
bt_sendpig = tk.Button(root, text="Send Pig", command=send_pig)
bt_sendpig.place(x=150, y=130)
bt_openbox = tk.Button(root, text="Openbox", command=toggle_loop)
bt_openbox.place(x=150, y=160)

text = tk.Text(root,width=82, height=10)
text.place(x=20, y=320)

listbox = tk.Listbox(root,width=40, height=17)
listbox.place(x=435, y=40)

combobox_IDS = ttk.Combobox(root,width=17, height=25)
combobox_IDS.place(x=435, y=10)

combobox_stall = ttk.Combobox(root, values=["1"],width=7, height=25)
combobox_stall.set("1")
combobox_stall.place(x=570, y=10)

combobox_craf = ttk.Combobox(root, values=["หมูโทเมะ","หมูคอร์น"],width=10, height=25)
combobox_craf.place(x=220, y=42)

combobox_poison = ttk.Combobox(root,width=10, height=25,values=["ยาถ่าย","น้ำแร่วิเศษ"])
combobox_poison.set("ยาถ่าย")
combobox_poison.place(x=200, y=103)

combobox_box = ttk.Combobox(root,width=5, height=25,values=["1","2","3"])
combobox_box.set("1")
combobox_box.place(x=215, y=163)

entry_id = tk.Entry(root)
entry_id.place(x=300, y=73)

root.mainloop()