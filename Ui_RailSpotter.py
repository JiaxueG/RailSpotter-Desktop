# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\JIAXUE GONG\Documents\GitHub\RailSpotter-Desktop\RailSpotter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 900))
        MainWindow.setMaximumSize(QtCore.QSize(2560, 1440))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(14, 11, 1556, 829))
        self.widget.setObjectName("widget")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelPicview = QtWidgets.QLabel(self.widget)
        self.labelPicview.setMinimumSize(QtCore.QSize(600, 400))
        self.labelPicview.setMaximumSize(QtCore.QSize(600, 400))
        self.labelPicview.setAcceptDrops(True)
        self.labelPicview.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPicview.setObjectName("labelPicview")
        self.verticalLayout.addWidget(self.labelPicview)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LineAddress = QtWidgets.QLineEdit(self.widget)
        self.LineAddress.setAcceptDrops(True)
        self.LineAddress.setObjectName("LineAddress")
        self.horizontalLayout.addWidget(self.LineAddress)
        self.btnInput = QtWidgets.QPushButton(self.widget)
        self.btnInput.setMinimumSize(QtCore.QSize(100, 0))
        self.btnInput.setObjectName("btnInput")
        self.horizontalLayout.addWidget(self.btnInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.LineLocation = QtWidgets.QLineEdit(self.widget)
        self.LineLocation.setAcceptDrops(True)
        self.LineLocation.setObjectName("LineLocation")
        self.horizontalLayout_13.addWidget(self.LineLocation)
        self.btnLocationSelect = QtWidgets.QPushButton(self.widget)
        self.btnLocationSelect.setMinimumSize(QtCore.QSize(100, 0))
        self.btnLocationSelect.setObjectName("btnLocationSelect")
        self.horizontalLayout_13.addWidget(self.btnLocationSelect)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.labelTimeSpace = QtWidgets.QLabel(self.widget)
        self.labelTimeSpace.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTimeSpace.setFont(font)
        self.labelTimeSpace.setScaledContents(False)
        self.labelTimeSpace.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTimeSpace.setObjectName("labelTimeSpace")
        self.verticalLayout_6.addWidget(self.labelTimeSpace)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelCountry = QtWidgets.QLabel(self.widget)
        self.labelCountry.setMinimumSize(QtCore.QSize(130, 24))
        self.labelCountry.setMaximumSize(QtCore.QSize(2910, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCountry.setFont(font)
        self.labelCountry.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCountry.setObjectName("labelCountry")
        self.verticalLayout_3.addWidget(self.labelCountry)
        self.lineEditCountry = QtWidgets.QLineEdit(self.widget)
        self.lineEditCountry.setMinimumSize(QtCore.QSize(130, 32))
        self.lineEditCountry.setMaximumSize(QtCore.QSize(1920, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditCountry.setFont(font)
        self.lineEditCountry.setObjectName("lineEditCountry")
        self.verticalLayout_3.addWidget(self.lineEditCountry)
        self.listWidgetCountry = QtWidgets.QListWidget(self.widget)
        self.listWidgetCountry.setMinimumSize(QtCore.QSize(130, 200))
        self.listWidgetCountry.setMaximumSize(QtCore.QSize(1920, 16777215))
        self.listWidgetCountry.setObjectName("listWidgetCountry")
        self.verticalLayout_3.addWidget(self.listWidgetCountry)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelLocation = QtWidgets.QLabel(self.widget)
        self.labelLocation.setMinimumSize(QtCore.QSize(100, 24))
        self.labelLocation.setMaximumSize(QtCore.QSize(1920, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLocation.setFont(font)
        self.labelLocation.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLocation.setObjectName("labelLocation")
        self.verticalLayout_2.addWidget(self.labelLocation)
        self.lineEditLocation = QtWidgets.QLineEdit(self.widget)
        self.lineEditLocation.setMinimumSize(QtCore.QSize(100, 32))
        self.lineEditLocation.setMaximumSize(QtCore.QSize(1920, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditLocation.setFont(font)
        self.lineEditLocation.setObjectName("lineEditLocation")
        self.verticalLayout_2.addWidget(self.lineEditLocation)
        self.listWidgetLocation = QtWidgets.QListWidget(self.widget)
        self.listWidgetLocation.setMinimumSize(QtCore.QSize(100, 200))
        self.listWidgetLocation.setMaximumSize(QtCore.QSize(1920, 16777215))
        self.listWidgetLocation.setObjectName("listWidgetLocation")
        self.verticalLayout_2.addWidget(self.listWidgetLocation)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_14.addLayout(self.verticalLayout_6)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.labelVehicleInfo = QtWidgets.QLabel(self.widget)
        self.labelVehicleInfo.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelVehicleInfo.setFont(font)
        self.labelVehicleInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVehicleInfo.setObjectName("labelVehicleInfo")
        self.verticalLayout_10.addWidget(self.labelVehicleInfo)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelLoco = QtWidgets.QLabel(self.widget)
        self.labelLoco.setMinimumSize(QtCore.QSize(120, 24))
        self.labelLoco.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLoco.setFont(font)
        self.labelLoco.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLoco.setObjectName("labelLoco")
        self.horizontalLayout_6.addWidget(self.labelLoco)
        self.checkBoxMU = QtWidgets.QCheckBox(self.widget)
        self.checkBoxMU.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBoxMU.setFont(font)
        self.checkBoxMU.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBoxMU.setText("")
        self.checkBoxMU.setChecked(False)
        self.checkBoxMU.setObjectName("checkBoxMU")
        self.horizontalLayout_6.addWidget(self.checkBoxMU)
        self.btnMU = QtWidgets.QPushButton(self.widget)
        self.btnMU.setObjectName("btnMU")
        self.horizontalLayout_6.addWidget(self.btnMU)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.lineEditLoco = QtWidgets.QLineEdit(self.widget)
        self.lineEditLoco.setMinimumSize(QtCore.QSize(120, 32))
        self.lineEditLoco.setMaximumSize(QtCore.QSize(16777215, 32))
        self.lineEditLoco.setObjectName("lineEditLoco")
        self.verticalLayout_7.addWidget(self.lineEditLoco)
        self.listWidgetLoco = QtWidgets.QListWidget(self.widget)
        self.listWidgetLoco.setMinimumSize(QtCore.QSize(120, 0))
        self.listWidgetLoco.setObjectName("listWidgetLoco")
        self.verticalLayout_7.addWidget(self.listWidgetLoco)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelNumber = QtWidgets.QLabel(self.widget)
        self.labelNumber.setMinimumSize(QtCore.QSize(120, 24))
        self.labelNumber.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNumber.setFont(font)
        self.labelNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNumber.setObjectName("labelNumber")
        self.horizontalLayout_3.addWidget(self.labelNumber)
        self.btnNumber = QtWidgets.QPushButton(self.widget)
        self.btnNumber.setObjectName("btnNumber")
        self.horizontalLayout_3.addWidget(self.btnNumber)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.lineEditNumber = QtWidgets.QLineEdit(self.widget)
        self.lineEditNumber.setMinimumSize(QtCore.QSize(120, 32))
        self.lineEditNumber.setMaximumSize(QtCore.QSize(16777215, 32))
        self.lineEditNumber.setObjectName("lineEditNumber")
        self.verticalLayout_8.addWidget(self.lineEditNumber)
        self.listWidgetNumber = QtWidgets.QListWidget(self.widget)
        self.listWidgetNumber.setMinimumSize(QtCore.QSize(120, 0))
        self.listWidgetNumber.setObjectName("listWidgetNumber")
        self.verticalLayout_8.addWidget(self.listWidgetNumber)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelCarriage = QtWidgets.QLabel(self.widget)
        self.labelCarriage.setMinimumSize(QtCore.QSize(120, 24))
        self.labelCarriage.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCarriage.setFont(font)
        self.labelCarriage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCarriage.setObjectName("labelCarriage")
        self.horizontalLayout_5.addWidget(self.labelCarriage)
        self.btnCarriage = QtWidgets.QPushButton(self.widget)
        self.btnCarriage.setObjectName("btnCarriage")
        self.horizontalLayout_5.addWidget(self.btnCarriage)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.lineEditCarriage = QtWidgets.QLineEdit(self.widget)
        self.lineEditCarriage.setMinimumSize(QtCore.QSize(120, 32))
        self.lineEditCarriage.setMaximumSize(QtCore.QSize(16777215, 32))
        self.lineEditCarriage.setObjectName("lineEditCarriage")
        self.verticalLayout_11.addWidget(self.lineEditCarriage)
        self.listWidgetCarriage = QtWidgets.QListWidget(self.widget)
        self.listWidgetCarriage.setMinimumSize(QtCore.QSize(120, 0))
        self.listWidgetCarriage.setObjectName("listWidgetCarriage")
        self.verticalLayout_11.addWidget(self.listWidgetCarriage)
        self.horizontalLayout_7.addLayout(self.verticalLayout_11)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.verticalLayout_15.addLayout(self.verticalLayout_10)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.labelServiceInfo = QtWidgets.QLabel(self.widget)
        self.labelServiceInfo.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelServiceInfo.setFont(font)
        self.labelServiceInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelServiceInfo.setObjectName("labelServiceInfo")
        self.verticalLayout_14.addWidget(self.labelServiceInfo)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelCompany = QtWidgets.QLabel(self.widget)
        self.labelCompany.setMinimumSize(QtCore.QSize(120, 24))
        self.labelCompany.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCompany.setFont(font)
        self.labelCompany.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCompany.setObjectName("labelCompany")
        self.horizontalLayout_4.addWidget(self.labelCompany)
        self.btnCompany = QtWidgets.QPushButton(self.widget)
        self.btnCompany.setEnabled(False)
        self.btnCompany.setCheckable(False)
        self.btnCompany.setObjectName("btnCompany")
        self.horizontalLayout_4.addWidget(self.btnCompany)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.lineEditCompany = QtWidgets.QLineEdit(self.widget)
        self.lineEditCompany.setMinimumSize(QtCore.QSize(120, 32))
        self.lineEditCompany.setMaximumSize(QtCore.QSize(16777215, 32))
        self.lineEditCompany.setObjectName("lineEditCompany")
        self.verticalLayout_9.addWidget(self.lineEditCompany)
        self.listWidgetCompany = QtWidgets.QListWidget(self.widget)
        self.listWidgetCompany.setMinimumSize(QtCore.QSize(120, 0))
        self.listWidgetCompany.setObjectName("listWidgetCompany")
        self.verticalLayout_9.addWidget(self.listWidgetCompany)
        self.horizontalLayout_10.addLayout(self.verticalLayout_9)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelLine = QtWidgets.QLabel(self.widget)
        self.labelLine.setMinimumSize(QtCore.QSize(120, 24))
        self.labelLine.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLine.setFont(font)
        self.labelLine.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLine.setObjectName("labelLine")
        self.horizontalLayout_8.addWidget(self.labelLine)
        self.btnLine = QtWidgets.QPushButton(self.widget)
        self.btnLine.setEnabled(False)
        self.btnLine.setObjectName("btnLine")
        self.horizontalLayout_8.addWidget(self.btnLine)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.lineEditLine = QtWidgets.QLineEdit(self.widget)
        self.lineEditLine.setMinimumSize(QtCore.QSize(120, 32))
        self.lineEditLine.setMaximumSize(QtCore.QSize(16777215, 32))
        self.lineEditLine.setObjectName("lineEditLine")
        self.verticalLayout_12.addWidget(self.lineEditLine)
        self.listWidgetLine = QtWidgets.QListWidget(self.widget)
        self.listWidgetLine.setMinimumSize(QtCore.QSize(120, 0))
        self.listWidgetLine.setObjectName("listWidgetLine")
        self.verticalLayout_12.addWidget(self.listWidgetLine)
        self.horizontalLayout_10.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.labelService = QtWidgets.QLabel(self.widget)
        self.labelService.setMinimumSize(QtCore.QSize(120, 24))
        self.labelService.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelService.setFont(font)
        self.labelService.setAlignment(QtCore.Qt.AlignCenter)
        self.labelService.setObjectName("labelService")
        self.horizontalLayout_9.addWidget(self.labelService)
        self.btnService = QtWidgets.QPushButton(self.widget)
        self.btnService.setEnabled(False)
        self.btnService.setObjectName("btnService")
        self.horizontalLayout_9.addWidget(self.btnService)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.lineEditService = QtWidgets.QLineEdit(self.widget)
        self.lineEditService.setMinimumSize(QtCore.QSize(120, 32))
        self.lineEditService.setMaximumSize(QtCore.QSize(16777215, 32))
        self.lineEditService.setObjectName("lineEditService")
        self.verticalLayout_13.addWidget(self.lineEditService)
        self.listWidgetService = QtWidgets.QListWidget(self.widget)
        self.listWidgetService.setMinimumSize(QtCore.QSize(120, 0))
        self.listWidgetService.setObjectName("listWidgetService")
        self.verticalLayout_13.addWidget(self.listWidgetService)
        self.horizontalLayout_10.addLayout(self.verticalLayout_13)
        self.verticalLayout_14.addLayout(self.horizontalLayout_10)
        self.verticalLayout_15.addLayout(self.verticalLayout_14)
        self.verticalLayout_23.addLayout(self.verticalLayout_15)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.labelMemoInfo = QtWidgets.QLabel(self.widget)
        self.labelMemoInfo.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelMemoInfo.setFont(font)
        self.labelMemoInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMemoInfo.setObjectName("labelMemoInfo")
        self.verticalLayout_22.addWidget(self.labelMemoInfo)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.labelCamera = QtWidgets.QLabel(self.widget)
        self.labelCamera.setMinimumSize(QtCore.QSize(120, 24))
        self.labelCamera.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCamera.setFont(font)
        self.labelCamera.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCamera.setObjectName("labelCamera")
        self.verticalLayout_17.addWidget(self.labelCamera)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.lineEditCamera = QtWidgets.QLineEdit(self.widget)
        self.lineEditCamera.setMinimumSize(QtCore.QSize(120, 32))
        self.lineEditCamera.setMaximumSize(QtCore.QSize(16777215, 32))
        self.lineEditCamera.setObjectName("lineEditCamera")
        self.verticalLayout_16.addWidget(self.lineEditCamera)
        self.listWidgetCamera = QtWidgets.QListWidget(self.widget)
        self.listWidgetCamera.setMinimumSize(QtCore.QSize(120, 0))
        self.listWidgetCamera.setMaximumSize(QtCore.QSize(16777215, 60))
        self.listWidgetCamera.setObjectName("listWidgetCamera")
        self.verticalLayout_16.addWidget(self.listWidgetCamera)
        self.verticalLayout_17.addLayout(self.verticalLayout_16)
        self.horizontalLayout_11.addLayout(self.verticalLayout_17)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.labelLens = QtWidgets.QLabel(self.widget)
        self.labelLens.setMinimumSize(QtCore.QSize(120, 24))
        self.labelLens.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLens.setFont(font)
        self.labelLens.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLens.setObjectName("labelLens")
        self.verticalLayout_18.addWidget(self.labelLens)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.lineEditLens = QtWidgets.QLineEdit(self.widget)
        self.lineEditLens.setMinimumSize(QtCore.QSize(120, 32))
        self.lineEditLens.setMaximumSize(QtCore.QSize(16777215, 32))
        self.lineEditLens.setObjectName("lineEditLens")
        self.verticalLayout_19.addWidget(self.lineEditLens)
        self.listWidgetLens = QtWidgets.QListWidget(self.widget)
        self.listWidgetLens.setMinimumSize(QtCore.QSize(120, 0))
        self.listWidgetLens.setMaximumSize(QtCore.QSize(16777215, 60))
        self.listWidgetLens.setObjectName("listWidgetLens")
        self.verticalLayout_19.addWidget(self.listWidgetLens)
        self.verticalLayout_18.addLayout(self.verticalLayout_19)
        self.horizontalLayout_11.addLayout(self.verticalLayout_18)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.labelMemo = QtWidgets.QLabel(self.widget)
        self.labelMemo.setMinimumSize(QtCore.QSize(120, 24))
        self.labelMemo.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelMemo.setFont(font)
        self.labelMemo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMemo.setObjectName("labelMemo")
        self.verticalLayout_20.addWidget(self.labelMemo)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.lineEditMemo = QtWidgets.QLineEdit(self.widget)
        self.lineEditMemo.setMinimumSize(QtCore.QSize(120, 32))
        self.lineEditMemo.setMaximumSize(QtCore.QSize(16777215, 32))
        self.lineEditMemo.setObjectName("lineEditMemo")
        self.verticalLayout_21.addWidget(self.lineEditMemo)
        self.listWidgetMemo = QtWidgets.QListWidget(self.widget)
        self.listWidgetMemo.setMinimumSize(QtCore.QSize(120, 0))
        self.listWidgetMemo.setMaximumSize(QtCore.QSize(16777215, 60))
        self.listWidgetMemo.setObjectName("listWidgetMemo")
        self.verticalLayout_21.addWidget(self.listWidgetMemo)
        self.verticalLayout_20.addLayout(self.verticalLayout_21)
        self.horizontalLayout_11.addLayout(self.verticalLayout_20)
        self.verticalLayout_22.addLayout(self.horizontalLayout_11)
        self.verticalLayout_23.addLayout(self.verticalLayout_22)
        self.horizontalLayout_12.addLayout(self.verticalLayout_23)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.btnClearAll = QtWidgets.QPushButton(self.widget)
        self.btnClearAll.setMinimumSize(QtCore.QSize(130, 0))
        self.btnClearAll.setObjectName("btnClearAll")
        self.verticalLayout_24.addWidget(self.btnClearAll)
        self.groupBoxFSsetting = QtWidgets.QGroupBox(self.widget)
        self.groupBoxFSsetting.setTitle("")
        self.groupBoxFSsetting.setObjectName("groupBoxFSsetting")
        self.verticalLayout_24.addWidget(self.groupBoxFSsetting)
        self.btnSave = QtWidgets.QPushButton(self.widget)
        self.btnSave.setMinimumSize(QtCore.QSize(130, 170))
        self.btnSave.setMaximumSize(QtCore.QSize(130, 170))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.verticalLayout_24.addWidget(self.btnSave)
        self.horizontalLayout_12.addLayout(self.verticalLayout_24)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_12)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditCountry, self.lineEditLocation)
        MainWindow.setTabOrder(self.lineEditLocation, self.lineEditLoco)
        MainWindow.setTabOrder(self.lineEditLoco, self.btnMU)
        MainWindow.setTabOrder(self.btnMU, self.lineEditNumber)
        MainWindow.setTabOrder(self.lineEditNumber, self.btnNumber)
        MainWindow.setTabOrder(self.btnNumber, self.lineEditCarriage)
        MainWindow.setTabOrder(self.lineEditCarriage, self.btnCarriage)
        MainWindow.setTabOrder(self.btnCarriage, self.lineEditCompany)
        MainWindow.setTabOrder(self.lineEditCompany, self.btnCompany)
        MainWindow.setTabOrder(self.btnCompany, self.lineEditLine)
        MainWindow.setTabOrder(self.lineEditLine, self.btnLine)
        MainWindow.setTabOrder(self.btnLine, self.lineEditService)
        MainWindow.setTabOrder(self.lineEditService, self.btnService)
        MainWindow.setTabOrder(self.btnService, self.lineEditCamera)
        MainWindow.setTabOrder(self.lineEditCamera, self.lineEditLens)
        MainWindow.setTabOrder(self.lineEditLens, self.lineEditMemo)
        MainWindow.setTabOrder(self.lineEditMemo, self.btnSave)
        MainWindow.setTabOrder(self.btnSave, self.listWidgetCarriage)
        MainWindow.setTabOrder(self.listWidgetCarriage, self.listWidgetLoco)
        MainWindow.setTabOrder(self.listWidgetLoco, self.listWidgetLine)
        MainWindow.setTabOrder(self.listWidgetLine, self.btnInput)
        MainWindow.setTabOrder(self.btnInput, self.LineAddress)
        MainWindow.setTabOrder(self.LineAddress, self.listWidgetService)
        MainWindow.setTabOrder(self.listWidgetService, self.listWidgetCamera)
        MainWindow.setTabOrder(self.listWidgetCamera, self.listWidgetCountry)
        MainWindow.setTabOrder(self.listWidgetCountry, self.listWidgetNumber)
        MainWindow.setTabOrder(self.listWidgetNumber, self.listWidgetLens)
        MainWindow.setTabOrder(self.listWidgetLens, self.listWidgetCompany)
        MainWindow.setTabOrder(self.listWidgetCompany, self.listWidgetMemo)
        MainWindow.setTabOrder(self.listWidgetMemo, self.btnClearAll)
        MainWindow.setTabOrder(self.btnClearAll, self.listWidgetLocation)
        MainWindow.setTabOrder(self.listWidgetLocation, self.checkBoxMU)
        MainWindow.setTabOrder(self.checkBoxMU, self.LineLocation)
        MainWindow.setTabOrder(self.LineLocation, self.btnLocationSelect)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RailSpotter Desktop"))
        self.labelPicview.setText(_translate("MainWindow", "图片预览"))
        self.btnInput.setText(_translate("MainWindow", "导入"))
        self.btnLocationSelect.setText(_translate("MainWindow", "选择保存根目录"))
        self.labelTimeSpace.setText(_translate("MainWindow", "地理信息"))
        self.labelCountry.setText(_translate("MainWindow", "国家"))
        self.labelLocation.setText(_translate("MainWindow", "地点"))
        self.labelVehicleInfo.setText(_translate("MainWindow", "车辆信息"))
        self.labelLoco.setText(_translate("MainWindow", "本务"))
        self.btnMU.setText(_translate("MainWindow", "动车"))
        self.labelNumber.setText(_translate("MainWindow", "编号"))
        self.btnNumber.setText(_translate("MainWindow", "未知"))
        self.labelCarriage.setText(_translate("MainWindow", "车底"))
        self.btnCarriage.setText(_translate("MainWindow", "未知"))
        self.labelServiceInfo.setText(_translate("MainWindow", "线路信息"))
        self.labelCompany.setText(_translate("MainWindow", "路局（公司）"))
        self.btnCompany.setText(_translate("MainWindow", "未知"))
        self.labelLine.setText(_translate("MainWindow", "路段/路线"))
        self.btnLine.setText(_translate("MainWindow", "未知"))
        self.labelService.setText(_translate("MainWindow", "车次"))
        self.btnService.setText(_translate("MainWindow", "未知"))
        self.labelMemoInfo.setText(_translate("MainWindow", "备注信息（可留空）"))
        self.labelCamera.setText(_translate("MainWindow", "相机"))
        self.labelLens.setText(_translate("MainWindow", "镜头"))
        self.labelMemo.setText(_translate("MainWindow", "其他"))
        self.btnClearAll.setText(_translate("MainWindow", "清空所有"))
        self.btnSave.setText(_translate("MainWindow", "保存"))

