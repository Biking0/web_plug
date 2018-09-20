#试图代码模拟post登陆,失败

import urllib.request
import requests

url="http://jxjyxx.xidian.edu.cn/login.action"



keywords = {
         'userType':'1',
         'loginName':'610115199504167264',
         'loginPassword':'4ca41f9d27d92f51899a96dd178b7000tnateh'
        }

# params = {"username": (None, "dengqingyong"), "password": (None, "abcd1234")}

data=requests.post(url,files=keywords)

print("\n")
print (data.text)