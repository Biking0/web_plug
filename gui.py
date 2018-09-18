
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
         
    @pyqtSlot()
    def on_click(self):
        main.login()
        

    def initUI(self):
         
        QToolTip.setFont(QFont('SansSerif', 10))
         
        self.setToolTip('挂机学习工具')
         
        btn = QPushButton('开始答题', self)
        btn.setToolTip('点击开始答题')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)    
        btn.clicked.connect(self.on_click)

        lable=QLabel("",self)

        
         
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')   
        self.show()

    
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
