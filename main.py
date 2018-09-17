
from selenium import webdriver
import time
import datetime
import random
import re

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

#答题
browser.find_element_by_xpath("html/body/div[2]/div[2]/form/table[1]/tbody/tr[3]/td/input").click()

#交卷
browser.find_element_by_xpath("html/body/div[2]/div[2]/form/center/input").click()

#确定
browser.switch_to_alert().accept()

#存下正确答案
#题号
tihao=browser.find_element_by_xpath("html/body/div/table/tbody/tr[2]/td[1]").text
#答案
daan=browser.find_element_by_xpath("html/body/div/table/tbody/tr[2]/td[3]").text
#判卷
pajuan=browser.find_element_by_xpath("html/body/div/table/tbody/tr[2]/td[4]").text

# if pajuan=="×":

dui="√"
cuo="×"
