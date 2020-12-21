import requests
import json
import os

# 配置开始
user = os.environ["USER"]
account = user.split( )[0] # 账号1
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
  "address_name":"深圳市朗生建材有限公司"
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url='http://xxy.kuileii.cn/release/xixunyun', headers=headers, data=json.dumps(data))
print(response.json())
