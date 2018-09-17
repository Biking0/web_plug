

import urllib.request
import urllib.parse

url="http://jxjyxx.xidian.edu.cn/login.action?userType=1&loginName=610115199504167264&loginPassword=4ca41f9d27d92f51899a96dd178b70001oq53b"



# postdata = urllib.parse.urlencode({
#     "userType":"1",
#     "loginName":"610115199504167264",
#     "loginPassword":"4ca41f9d27d92f51899a96dd178b70001oq53b"
    
# }).encode("utf-8")

# response=urllib.request.urlopen(url)

# print("response",response)

data = urllib.request.urlopen(url).read().decode("utf-8")

print(data)