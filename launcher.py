import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_RailSpotter import Ui_MainWindow
from aip import AipImageClassify
import shutil
import os
import exifread

class launcher(QMainWindow, Ui_MainWindow): 
    imgLocation = ""
    fileLocation=''
    def __init__(self, parent=None): 
        super().__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.basicUi()
        # Controller
        self.ui.btnInput.clicked.connect(self.imageOpen)
        self.ui.btnSave.clicked.connect(self.saveAll)
        self.ui.btnMU.clicked.connect(self.setMU)
        self.ui.btnLocationSelect.clicked.connect(self.locationSelect)

    def basicUi(self): 
        self.ui.status=self.statusBar()
        self.ui.status.showMessage('RailSpotter Desktop by JiaxueG v0.1')
         
    def locationSelect(self): 
        try: 
            self.fileLocation = QFileDialog.getExistingDirectory()
            self.ui.LineLocation.setText(self.fileLocation)
            # print(self.fileLocation)
        except: 
            self.ui.LineLocation.setText('选择根目录文件夹')

    def imageOpen(self): 
        try: 
            self.imgLocation, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;All Files(*)")
            self.ui.LineAddress.setText(self.imgLocation)
            self.imageShow()
            # print('next')
            #self.imageOpen()
        except: 
            self.ui.labelPicview.setText('图片预览')
    
    def imageShow(self): 
        image=QtGui.QPixmap(self.imgLocation)
        if image.width() > self.ui.labelPicview.width() or image.height() > self.ui.labelPicview.height():
            scaleWidth = image.width()/self.ui.labelPicview.width()
            scaleHeight = image.height()/self.ui.labelPicview.height()
            if scaleWidth >= scaleHeight:
                scale = scaleWidth
            else:
                scale = scaleHeight
        imageDisplay = QtGui.QPixmap(self.imgLocation).scaled(image.width()/scale, image.height()/scale)
        self.ui.labelPicview.setPixmap(imageDisplay)  # display      
    
    def isEmpty(self): 
        return self.length==0
    
    def setMU(self): 
        if self.ui.checkBoxMU.isChecked()==False: 
            self.ui.checkBoxMU.setCheckState(2)
            self.ui.btnCarriage.setEnabled(False)
            self.ui.lineEditCarriage.setEnabled(False)
            self.ui.listWidgetCarriage.setEnabled(False)
            self.ui.lineEditCarriage.setText('')
        else: 
            self.ui.checkBoxMU.setCheckState(0)
            self.ui.btnCarriage.setEnabled(True)
            self.ui.lineEditCarriage.setEnabled(True)
            self.ui.listWidgetCarriage.setEnabled(True)
        
    


    #def dateSet(self): 
        # self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 2), QtCore.QTime(0, 0, 0)))

    def saveAll(self): #Incompleted
        # copy everything to history
        if self.ui.lineEditCountry.text(): # is not empty
            self.ui.listWidgetCountry.addItem(self.ui.lineEditCountry.text())
        if self.ui.lineEditLocation.text(): 
            self.ui.listWidgetLocation.addItem(self.ui.lineEditLocation.text())
        if self.ui.lineEditLoco.text(): 
            self.ui.listWidgetLoco.addItem(self.ui.lineEditLoco.text())
        if self.ui.lineEditNumber.text(): 
            self.ui.listWidgetNumber.addItem(self.ui.lineEditNumber.text())
        if self.ui.lineEditCarriage.text(): 
            self.ui.listWidgetCarriage.addItem(self.ui.lineEditCarriage.text())
        if self.ui.lineEditCompany.text(): 
            self.ui.listWidgetCompany.addItem(self.ui.lineEditCompany.text())
        if self.ui.lineEditLine.text(): 
            self.ui.listWidgetLine.addItem(self.ui.lineEditLine.text())
        if self.ui.lineEditService.text(): 
            self.ui.listWidgetService.addItem(self.ui.lineEditService.text())
        if self.ui.lineEditCamera.text(): 
            self.ui.listWidgetCamera.addItem(self.ui.lineEditCamera.text())
        if self.ui.lineEditLens.text(): 
            self.ui.listWidgetLens.addItem(self.ui.lineEditLens.text())
        if self.ui.lineEditMemo.text(): 
            self.ui.listWidgetMemo.addItem(self.ui.lineEditMemo.text())
        self.picSaveVehicle()
        # File system check
        #if self.ui.checkBoxFStime.isChecked()==True: 
            # Save as file system => file
        #if self.ui.checkBoxFSvehicle.isChecked()==True: 
            # Save as file system => vehicle
    def picSaveVehicle(self): 
        source=self.imgLocation
        country='/'+self.ui.lineEditCountry.text()
        loco = '/'+self.ui.lineEditLoco.text()
        number = '/'+self.ui.lineEditNumber.text()
        target = self.fileLocation+country+loco+number+'/'
        if not os.path.exists(self.fileLocation+country):
            os.mkdir(self.fileLocation+country)
        if not os.path.exists(self.fileLocation+country+loco):
            os.mkdir(self.fileLocation+country+loco)
        if not os.path.exists(self.fileLocation+country+loco+number):
            os.mkdir(self.fileLocation+country+loco+number)
        try:
            shutil.copy(source, target)
            self.ui.status.showMessage('RailSpotter Desktop by JiaxueG v0.1 - 图片已保存到'+target)
        except: 
            self.ui.status.showMessage('RailSpotter Desktop by JiaxueG v0.1 - 图片未成功保存')


if __name__=='__main__': 
    app=QApplication(sys.argv)
    window=launcher()
    window.show()
    sys.exit(app.exec_())
