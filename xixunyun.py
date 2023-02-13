import requests
import json
import os

# 配置开始 
user = os.environ["USER"]
account = user.split( )[0] # 账号
password = user.split( )[1] # 密码
school_id = user.split( )[2] # 学校ID
sign_gps = os.environ["SIGN_GPS"]  # 签到坐标（注意小数点取后6位）
longitude = sign_gps.split(",")[0] # 经度
latitude = sign_gps.split(",")[1] # 纬度
data = {
  "account":account,
  "password":password,
  "school_id":school_id,
  "longitude":longitude,
  "latitude":latitude,
  "address_name":os.environ["ADDRESS_NAME"] 
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url='https://service-nm4jylpg-1251957121.gz.apigw.tencentcs.com/release/xixunyun', headers=headers, data=json.dumps(data))
print(response.json()["data"])



SCKEY=os.environ["SCKEY"]
token = 'db37004bad284d5c8bef538488130e6e' #在pushpush网站中可以找到
title= '签到推送' #改成你要的标题内容
content = response.json()["data"] #改成你要的正文内容
url = 'http://www.pushplus.plus/send'
data = {
    "token":SCKEY,
    "title":title,
    "content":content
}
body=json.dumps(data).encode(encoding='utf-8')
headers = {'Content-Type':'application/json'}
requests.post(url,data=body,headers=headers)
