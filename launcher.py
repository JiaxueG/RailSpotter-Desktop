import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_RailSpotter import Ui_MainWindow
from aip import AipImageClassify

class launcher(QMainWindow, Ui_MainWindow): 
    imgName = ""
    def __init__(self, parent=None): 
        super().__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.basicUi()
        # Controller
        self.ui.btnInput.clicked.connect(self.imageOpen)

    def basicUi(self): 
        self.ui.status=self.statusBar()
        self.ui.status.showMessage('RailSpotter Desktop by JiaxueG v0.1')

    def imageOpen(self): 
        try: 
            self.imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;All Files(*)")
            self.ui.LineAddress.setText(self.imgName)
            self.imageShow()
        except: 
            self.ui.labelPicview.setText('图片预览')
    
    def imageShow(self): 
        image=QtGui.QPixmap(self.imgName)
        if image.width() > self.ui.labelPicview.width() or image.height() > self.ui.labelPicview.height():
            scaleWidth = image.width()/self.ui.labelPicview.width()
            scaleHeight = image.height()/self.ui.labelPicview.height()
            if scaleWidth >= scaleHeight:
                scale = scaleWidth
            else:
                scale = scaleHeight
        imageDisplay = QtGui.QPixmap(self.imgName).scaled(image.width()/scale, image.height()/scale)
        self.ui.labelPicview.setPixmap(imageDisplay)  # display

if __name__=='__main__': 
    app=QApplication(sys.argv)
    window=launcher()
    window.show()
    sys.exit(app.exec_())    
