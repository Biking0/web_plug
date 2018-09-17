
import urllib.request
import urllib.parse
import selenium

url="http://jxjyxx.xidian.edu.cn/login.action"


postdata = urllib.parse.urlencode({
    "userType":"1",
    "loginName":"610115199504167264",
    "loginPassword":"4ca41f9d27d92f51899a96dd178b70001oq53b"
    
}).encode("utf-8")

response=urllib.request.Request(url,postdata)

print("response",response)

data = urllib.request.urlopen(response).read().decode("utf-8")

print(data)