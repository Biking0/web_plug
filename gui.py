
import main
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication,QLabel)
from PyQt5.QtGui import QFont  
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
        btn.clicked.connect(self.on_click)
 
        #提示内容
        lable=QLabel("点击按钮开始自动答题",self)
        lable.move(80,50)


        # lable.setText("123")

        # self.l

        # self.label=QLabel()
        
        # self.label.move(50,80)
        # self.label.setText

        btn.clicked.connect(lable.setText)
        

         
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')   
        self.show()         
    
    @pyqtSlot()
    def on_click(self):
        main.login()


    # @pyqtSlot()
    # def setText(self):
    #     print(61)
        
        
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()

    try :
        sys.exit(app.exec_())    
    except:
        print("退出")


