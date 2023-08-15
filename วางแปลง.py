import requests
import time

def place_object(plot_id,x, y):
    url = "https://api-piggy.codedefeat.com/v29/api/users/farm/shop/placeobject/"
    headers = {
        "Host": "api-piggy.codedefeat.com",
        "User-Agent": "UnityPlayer/2020.3.48f1 (UnityWebRequest/1.0, libcurl/7.84.0-DEV)",
        "Accept": "*/*",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiIzMzY1MDYyMDYzNzU3Mjk2IiwiZmJuYW1lIjoiU2FyYWxhayBTdWtzYW5nIiwiYWNjZXNzdG9rZW4iOiJVTzJYdVBRUUZZT0lXMUF4WlE2bEd5SXlrQ0RROFhmNyIsImRhdGVfdGltZSI6IjIwMjMtMDgtMDcgMTI6Mzc6MzIiLCJleHAiOjE2OTE0NzMwNTJ9.X1jl_lDbChteWT-2mVVpOenHmEWAC5pH_kLaQ9xtFQ4",
        "X-Unity-Version": "2020.3.48f1",
    }

    data = {
        "id": "1",
        "type": "object",
        "plot_id": str(plot_id),
        "position": f'{{"x":{x},"y":{y}}}',  # ใส่ค่า x และ y เข้าไปในข้อมูล
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# เรียกใช้ฟังก์ชัน place_object() และส่งค่า x และ y เพื่อทำการ POST request
x_value = 1
y_value = 1
plot_id = 1
while True:
    try:
        y_value += 2
        if y_value > 23:
            y_value = 1
            x_value += 2
        if x_value > 23:
            x_value = 1
            plot_id +=1
            if plot_id > 1:
                break
        print(f'plot : {plot_id} x : {x_value} y : {y_value}')
        result = place_object(plot_id,x_value, y_value)
        print(result)
        if result:
            print("สำเร็จ! รับข้อมูลจากเซิร์ฟเวอร์:")
            print(result)
        else:
            print("การร้องขอล้มเหลว")
        time.sleep(0.1)
    except:
        pass
