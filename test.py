import requests

headers = {
    "Host": "api-piggy.codedefeat.com",
    "User-Agent": "UnityPlayer/2020.3.48f1 (UnityWebRequest/1.0, libcurl/7.84.0-DEV)",
    "Accept": "*/*",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiIxNTU5NjcwODgxMTI2MjA2IiwiZmJuYW1lIjoiTm9uIEhheWRheSIsImFjY2Vzc3Rva2VuIjoiOURXSTlpcHNtT3BBcnRteUVWTlp1VEtKd2RFZXdmYnIiLCJkYXRlX3RpbWUiOiIyMDIzLTA4LTEzIDEzOjI1OjI0IiwiZXhwIjoxNjkxOTk0MzI0fQ.l4TECg5HSYYc6owrg3WP1040fJbW0cil34kp07ByXxQ",
    "X-Unity-Version": "2020.3.48f1"
}

data = {
    "userid": "1799869087014887",
    "stall_id": "9",
    "item_id": "6"
}

url = "https://api-piggy.codedefeat.com/v29/api/users/pigs/poison/confirm/"

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.text)
