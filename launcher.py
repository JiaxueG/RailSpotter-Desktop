import os
import shutil
import sys
import exifread
from aip import AipImageClassify
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QDateTime, QTime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_RailSpotter import Ui_MainWindow
class launcher(QMainWindow, Ui_MainWindow): 
    imgLocation = ''
    fileLocation=''
    target=''
    activateSwitch1 = 0
    activateSwitch2 = 0
    def __init__(self, parent=None): 
        super().__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.basicUi()
        self.widgetDisable()
        self.setWindowIcon(QIcon('logo.ico'))
        # Controller
        self.ui.btnInput.clicked.connect(self.imageOpen)
        self.ui.btnSave.clicked.connect(self.saveAll)
        self.ui.btnMU.clicked.connect(self.setMU)
        self.ui.btnLocationSelect.clicked.connect(self.locationSelect)
        self.ui.btnNumber.clicked.connect(self.unknownNumber)
        self.ui.btnCarriage.clicked.connect(self.unknownCarriage)
        self.ui.btnCompany.clicked.connect(self.unknownCompany)
        self.ui.btnLine.clicked.connect(self.unknownLine)
        self.ui.btnService.clicked.connect(self.unknownService)
        self.ui.btnClearAll.clicked.connect(self.clearAll)
        self.ui.listWidgetCountry.itemDoubleClicked.connect(self.copyCountry)
        self.ui.listWidgetLocation.itemDoubleClicked.connect(self.copyLocation)
        self.ui.listWidgetLoco.itemDoubleClicked.connect(self.copyLoco)
        self.ui.listWidgetNumber.itemDoubleClicked.connect(self.copyNumber)
        self.ui.listWidgetCarriage.itemDoubleClicked.connect(self.copyCarriage)
        self.ui.listWidgetCompany.itemDoubleClicked.connect(self.copyCompany)
        self.ui.listWidgetLine.itemDoubleClicked.connect(self.copyLine)
        self.ui.listWidgetService.itemDoubleClicked.connect(self.copyService)
        self.ui.listWidgetCamera.itemDoubleClicked.connect(self.copyCamera)
        self.ui.listWidgetLens.itemDoubleClicked.connect(self.copyLens)
        self.ui.listWidgetMemo.itemDoubleClicked.connect(self.copyMemo)

    def basicUi(self): 
        self.ui.status=self.statusBar()
        self.ui.status.showMessage('RailSpotter Desktop by JiaxueG v0.1 Beta')
    
    def clearAll(self): 
        self.ui.lineEditCountry.clear()
        self.ui.lineEditLocation.clear()
        self.ui.lineEditLoco.clear()
        self.ui.lineEditNumber.clear()
        self.ui.lineEditCarriage.clear()
        self.ui.lineEditCompany.clear()
        self.ui.lineEditLine.clear()
        self.ui.lineEditService.clear()
        self.ui.lineEditCamera.clear()
        self.ui.lineEditLens.clear()
        self.ui.lineEditMemo.clear()
        self.ui.listWidgetCountry.clear()
        self.ui.listWidgetLocation.clear()
        self.ui.listWidgetLoco.clear()
        self.ui.listWidgetNumber.clear()
        self.ui.listWidgetCarriage.clear()
        self.ui.listWidgetCompany.clear()
        self.ui.listWidgetLine.clear()
        self.ui.listWidgetService.clear()
        self.ui.listWidgetCamera.clear()
        self.ui.listWidgetLens.clear()
        self.ui.listWidgetMemo.clear()
        self.ui.LineAddress.clear()
        self.ui.LineLocation.clear()
         
    def locationSelect(self): 
        try: 
            self.fileLocation = QFileDialog.getExistingDirectory()
            self.ui.LineLocation.setText(self.fileLocation)
            self.activateSwitch2 = 1
            if self.activateSwitch1==1 and self.activateSwitch2==1:
                self.widgetEnable()
            else: 
                self.widgetDisable()
            # print(self.fileLocation)
        except: 
            self.ui.LineLocation.setText('选择根目录文件夹')
    
    def unknownNumber(self): 
        self.ui.lineEditNumber.setText('未知')

    def unknownCarriage(self):
        self.ui.lineEditCarriage.setText('未知')

    def unknownCompany(self):
        self.ui.lineEditCompany.setText('未知')
    
    def unknownLine(self):
        self.ui.lineEditLine.setText('未知')
    
    def unknownService(self):
        self.ui.lineEditService.setText('未知')

    def imageOpen(self): 
        try: 
            self.imgLocation, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;All Files(*)")
            self.ui.LineAddress.setText(self.imgLocation)
            self.imageShow()
            self.activateSwitch1 = 1
            if self.activateSwitch1 == 1 and self.activateSwitch2 == 1:
                self.widgetEnable()
            # print('next')
            # self.imageOpen()
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
    
    def widgetDisable(self): 
        self.ui.lineEditCountry.setEnabled(False)
        self.ui.lineEditLocation.setEnabled(False)
        self.ui.lineEditLoco.setEnabled(False)
        self.ui.lineEditNumber.setEnabled(False)
        self.ui.lineEditCarriage.setEnabled(False)
        self.ui.lineEditCompany.setEnabled(False)
        self.ui.lineEditLine.setEnabled(False)
        self.ui.lineEditService.setEnabled(False)
        self.ui.lineEditCamera.setEnabled(False)
        self.ui.lineEditLens.setEnabled(False)
        self.ui.lineEditMemo.setEnabled(False)
        self.ui.listWidgetCountry.setEnabled(False)
        self.ui.listWidgetLocation.setEnabled(False)
        self.ui.listWidgetLoco.setEnabled(False)
        self.ui.listWidgetNumber.setEnabled(False)
        self.ui.listWidgetCarriage.setEnabled(False)
        self.ui.listWidgetCompany.setEnabled(False)
        self.ui.listWidgetLine.setEnabled(False)
        self.ui.listWidgetService.setEnabled(False)
        self.ui.listWidgetCamera.setEnabled(False)
        self.ui.listWidgetLens.setEnabled(False)
        self.ui.listWidgetMemo.setEnabled(False)
        self.ui.btnSave.setEnabled(False)
        self.ui.btnMU.setEnabled(False)
        self.ui.checkBoxMU.setEnabled(False)
        self.ui.btnNumber.setEnabled(False)
        self.ui.btnCarriage.setEnabled(False)

    def widgetEnable(self):
        self.ui.lineEditCountry.setEnabled(True)
        self.ui.lineEditLocation.setEnabled(True)
        self.ui.lineEditLoco.setEnabled(True)
        self.ui.lineEditNumber.setEnabled(True)
        self.ui.lineEditCarriage.setEnabled(True)
        self.ui.lineEditCompany.setEnabled(True)
        self.ui.lineEditLine.setEnabled(True)
        self.ui.lineEditService.setEnabled(True)
        self.ui.lineEditCamera.setEnabled(True)
        self.ui.lineEditLens.setEnabled(True)
        self.ui.lineEditMemo.setEnabled(True)
        self.ui.listWidgetCountry.setEnabled(True)
        self.ui.listWidgetLocation.setEnabled(True)
        self.ui.listWidgetLoco.setEnabled(True)
        self.ui.listWidgetNumber.setEnabled(True)
        self.ui.listWidgetCarriage.setEnabled(True)
        self.ui.listWidgetCompany.setEnabled(True)
        self.ui.listWidgetLine.setEnabled(True)
        self.ui.listWidgetService.setEnabled(True)
        self.ui.listWidgetCamera.setEnabled(True)
        self.ui.listWidgetLens.setEnabled(True)
        self.ui.listWidgetMemo.setEnabled(True)
        self.ui.btnSave.setEnabled(True)
        self.ui.btnMU.setEnabled(True)
        self.ui.checkBoxMU.setEnabled(True)
        self.ui.btnNumber.setEnabled(True)
        self.ui.btnCarriage.setEnabled(True)
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
        activateSwitch1 = 0
        activateSwitch2 = 0
        self.widgetDisable()
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
        self.target = self.fileLocation+country+loco+number+'/'
        if not os.path.exists(self.fileLocation+country):
            os.mkdir(self.fileLocation+country)
        if not os.path.exists(self.fileLocation+country+loco):
            os.mkdir(self.fileLocation+country+loco)
        if not os.path.exists(self.fileLocation+country+loco+number):
            os.mkdir(self.fileLocation+country+loco+number)
        try:
            shutil.copy(source, self.target)
            self.ui.status.showMessage('RailSpotter Desktop by JiaxueG v0.1 - 图片已保存到'+self.target)
        except: 
            self.ui.status.showMessage('RailSpotter Desktop by JiaxueG v0.1 - 图片未成功保存')
        self.reName()
    
    def reName(self): 
        if self.ui.lineEditLocation.text():
            location = self.ui.lineEditLocation.text()+'_'
        else:
            location = ''
        if self.ui.lineEditLoco.text(): 
            loco = self.ui.lineEditLoco.text()+'_'
        else: 
            loco = ''
        if self.ui.lineEditNumber.text(): 
            number = self.ui.lineEditNumber.text()+'_'
        else: 
            number = ''
        if self.ui.lineEditCarriage.text():
            carriage = self.ui.lineEditCarriage.text()+'_'
        else:
            carriage = ''
        if self.ui.lineEditCompany.text():
            company = self.ui.lineEditCompany.text()+'_'
        else:
            company = ''
        if self.ui.lineEditLine.text():
            line = self.ui.lineEditLine.text()+'_'
        else:
            line = ''
        if self.ui.lineEditService.text():
            service = self.ui.lineEditService.text()+'_'
        else:
            service = ''
        if self.ui.lineEditCamera.text():
            camera = self.ui.lineEditCamera.text()+'_'
        else:
            camera = ''
        if self.ui.lineEditLens.text():
            lens = self.ui.lineEditLens.text()+'_'
        else:
            lens = ''
        if self.ui.lineEditMemo.text():
            memo = self.ui.lineEditMemo.text()+'_'
        else:
            memo = ''
        name=location+loco+number+carriage+company+line+service+camera+lens+memo
        # check num of pics in this file
        fileNum=0
        fileNum=len(os.listdir(self.target))
        # if os.path.isfile(self.target): 
        #     fileNum=fileNum+1
        name=name+'_'+str(fileNum)
        nameOrigin=os.path.split(self.imgLocation)
        os.rename(self.target+str(nameOrigin[1]), self.target+name+'.jpg')
        self.ui.status.showMessage('RailSpotter Desktop by JiaxueG v0.1 - 图片已保存到'+self.target+name+'.jpg')

    def copyCountry(self, item):
        content = item.text()
        self.ui.lineEditCountry.setText(content)

    def copyLocation(self, item):
        content = item.text()
        self.ui.lineEditLocation.setText(content)

    def copyLoco(self, item):
        content = item.text()
        self.ui.lineEditLoco.setText(content)

    def copyNumber(self, item):
        content = item.text()
        self.ui.lineEditNumber.setText(content)

    def copyCarriage(self, item):
        content = item.text()
        self.ui.lineEditCarriage.setText(content)

    def copyCompany(self, item):
        content = item.text()
        self.ui.lineEditCompany.setText(content)

    def copyLine(self, item):
        content = item.text()
        self.ui.lineEditLine.setText(content)

    def copyService(self, item):
        content = item.text()
        self.ui.lineEditService.setText(content)

    def copyCamera(self, item):
        content = item.text()
        self.ui.lineEditCamera.setText(content)

    def copyLens(self, item):
        content = item.text()
        self.ui.lineEditLens.setText(content)

    def copyMemo(self, item):
        content = item.text()
        self.ui.lineEditMemo.setText(content)
  
if __name__=='__main__': 
    app=QApplication(sys.argv)
    window=launcher()
    window.show()
    sys.exit(app.exec_())
