
#主界面，程序启动入口
#网站答题


import main
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication,QLabel)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import pyqtSlot

class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
    
        

    def initUI(self):
         
        QToolTip.setFont(QFont('SansSerif', 10))
         
        self.setToolTip('挂机学习工具')
         
        #答题按钮
        btn = QPushButton('开始答题', self)
        btn.setToolTip('点击开始答题')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        #退出按钮
        btn_stop = QPushButton('停止', self)
        btn_stop.setToolTip('停止答题')
        btn_stop.resize(btn.sizeHint())
        btn_stop.move(250, 50)    

        btn_stop.clicked.connect(QCoreApplication.instance().quit)        
 
        #提示内容
        lable=QLabel("点击按钮开始自动答题，正在运行时，请避免连续点击",self)
        lable.move(50,80)

        #提示
        lable1=QLabel("目前仅运行一个用户：610115199504167264",self)
        lable1.move(50,100)

        btn.clicked.connect(self.on_click)
        btn.clicked.connect(self.setText)
        

         
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('test.png'))
        self.setWindowTitle('挂机学习')   
        self.show()         
    
    @pyqtSlot()
    def on_click(self):
        main.login()


    @pyqtSlot()
    def setText(self):
        print(61)

    # @pyqtSlot()
    # def stop(self):
    #     main.stop()       
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()

    try :
        sys.exit(app.exec_())    
    except:
        print("退出")


