# web_plug
挂机学习Windows小程序

开发环境：
    python3.5
    GUI：pyqt(5.11.2)
    seleium，自动化浏览,（尚在计划）
功能特性：
    自动登录账户
    多账户视频挂机学习
    自动答题测试


纯代码登陆失败
单个浏览器，多标签

 2018/09/18 13:04 
seleium，自动化浏览，（确认）


开发进度：

 2018/09/16
自动答题软件开发：
网址：http://jxjyxx.xidian.edu.cn/cesp/index_backup.jsp
测试账号： 610115199504167264，19950416
开发步骤：

 2018/09/17
准备用户界面：
pyqt安装成功
先安装sip
pip install sip
后面安装pyqt5
pip install pyqt5
版本会自动选择

尝试代码登陆失败：
登入后地址
http://jxjyxx.xidian.edu.cn/cesp/main

javascript:window.top.location.href='http://jxjyxx.xidian.edu.cn:80/cesp/index_backup.jsp'

http://jxjyxx.xidian.edu.cn/cesp/index_backup.jsp/login.action


题型
单项选择，1-30
多项选择（四项），31-35
多项选择（五项），36-40
判断题，

 2018/09/18 10:32 
答案不规则
倒序处理
答案末尾空格

 2018/09/18 13:11 
加入简单界面，用户交付
界面设计
开始答题，采集阶段
结束答题，结束答题，不退出程序	




