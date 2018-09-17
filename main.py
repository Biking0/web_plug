
from selenium import webdriver
import time
import datetime
import random
import re

#判断对错
dui="√"
cuo="×"

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs',prefs)
browser = webdriver.Chrome("D:\softInstall\chromedriver.exe",chrome_options = options)




# browser = webdriver.Chrome("D:\softInstall\chromedriver.exe")

#登陆
browser.get("http://jxjyxx.xidian.edu.cn/cesp/index_backup.jsp")
browser.find_element_by_name("loginName").send_keys("610115199504167264")   
browser.find_element_by_name("loginPassword").send_keys("19950416")
browser.find_element_by_xpath("html/body/form/div[1]/div[1]/div[6]").click()

#课程考试
browser.find_element_by_id("win-test-shortcut").click()

# time.sleep(4)


#切换到弹出窗口
browser.switch_to_frame("iframe-win-test")
#切换到课程考试申请表格
browser.switch_to_frame("mFrame")
#点击申请
browser.find_element_by_xpath("html/body/div/table[2]/tbody/tr[2]/td[9]").click()

#切换到弹出窗口
browser.switch_to_frame("iframe-win-test")

#用map处理

ti={}
timu_list=[]
#答题
for i in range(1,30,1):
    # browser.find_element_by_xpath("html/body/div[2]/div[2]/form/table[1]/tbody/tr[3]/td/input").click()
    #选择按钮
    browser.find_element_by_xpath("html/body/div[2]/div[2]/form/table["+str(i)+"]/tbody/tr[2]/td/input").click()
    
    #题目
    timu=browser.find_element_by_xpath("html/body/div[2]/div[2]/form/table["+str(i)+"]/tbody/tr[1]/td").text[3:].split(".")
    if len(timu)>1:
        timu_str=timu[1]
    else : timu_str=timu[0]

    #答案，不规则问题处理
    daan=browser.find_element_by_xpath("html/body/div[2]/div[2]/form/table["+str(i)+"]/tbody/tr[2]/td").text[3:]
    pass
    ti[timu_str]=daan
    timu_list.append(timu_str)


#交卷
browser.find_element_by_xpath("html/body/div[2]/div[2]/form/center/input").click()

#确定
browser.switch_to_alert().accept()

#存下正确答案

for i in range(2,31,1):
    #题号
    tihao=browser.find_element_by_xpath("html/body/div/table/tbody/tr["+str(i)+"]/td[1]").text
    #答案
    daan=browser.find_element_by_xpath("html/body/div/table/tbody/tr["+str(i)+"]/td[3]").text
    #判卷
    pajuan=browser.find_element_by_xpath("html/body/div/table/tbody/tr["+str(i)+"]/td[4]").text

    if pajuan==dui:
        f=open("./test.txt",'a')
        f.write(timu_list[i-2]+"--"+ti[timu_list[i-2]]+"\n")

# if pajuan=="×":

print(ti)


