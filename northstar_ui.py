# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\northstar.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(909, 569)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(147, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.w_icons = QtWidgets.QWidget(self.centralwidget)
        self.w_icons.setObjectName("w_icons")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.w_icons)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MainIcon = QtWidgets.QLabel(self.w_icons)
        self.MainIcon.setMinimumSize(QtCore.QSize(40, 40))
        self.MainIcon.setMaximumSize(QtCore.QSize(40, 40))
        self.MainIcon.setText("")
        self.MainIcon.setPixmap(QtGui.QPixmap(":/icon/4.jpg"))
        self.MainIcon.setScaledContents(True)
        self.MainIcon.setObjectName("MainIcon")
        self.verticalLayout_2.addWidget(self.MainIcon)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.icon1 = QtWidgets.QPushButton(self.w_icons)
        self.icon1.setMinimumSize(QtCore.QSize(0, 40))
        self.icon1.setText("")
        self.icon1.setObjectName("icon1")
        self.verticalLayout.addWidget(self.icon1)
        self.icon2 = QtWidgets.QPushButton(self.w_icons)
        self.icon2.setMinimumSize(QtCore.QSize(0, 40))
        self.icon2.setText("")
        self.icon2.setObjectName("icon2")
        self.verticalLayout.addWidget(self.icon2)
        self.icon3 = QtWidgets.QPushButton(self.w_icons)
        self.icon3.setMinimumSize(QtCore.QSize(0, 40))
        self.icon3.setText("")
        self.icon3.setObjectName("icon3")
        self.verticalLayout.addWidget(self.icon3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 313, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.icon4 = QtWidgets.QPushButton(self.w_icons)
        self.icon4.setMinimumSize(QtCore.QSize(0, 40))
        self.icon4.setText("")
        self.icon4.setObjectName("icon4")
        self.verticalLayout_2.addWidget(self.icon4)
        self.gridLayout.addWidget(self.w_icons, 0, 0, 2, 1)
        self.w_widget = QtWidgets.QWidget(self.centralwidget)
        self.w_widget.setObjectName("w_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.w_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.w_page = QtWidgets.QStackedWidget(self.w_widget)
        self.w_page.setObjectName("w_page")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.page1)
        self.label_5.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/icon/3.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.w_page.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.page2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.w_page.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.page3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.w_page.addWidget(self.page3)
        self.verticalLayout_4.addWidget(self.w_page)
        self.gridLayout.addWidget(self.w_widget, 0, 1, 1, 1)
        self.w_console = QtWidgets.QWidget(self.centralwidget)
        self.w_console.setMaximumSize(QtCore.QSize(16777215, 250))
        self.w_console.setObjectName("w_console")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.w_console)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.messageArea = QtWidgets.QHBoxLayout()
        self.messageArea.setSpacing(0)
        self.messageArea.setObjectName("messageArea")
        spacerItem3 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.messageArea.addItem(spacerItem3)
        self.sendmsg = QtWidgets.QLineEdit(self.w_console)
        self.sendmsg.setMinimumSize(QtCore.QSize(250, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.sendmsg.setFont(font)
        self.sendmsg.setObjectName("sendmsg")
        self.messageArea.addWidget(self.sendmsg)
        self.send = QtWidgets.QPushButton(self.w_console)
        self.send.setMinimumSize(QtCore.QSize(0, 20))
        self.send.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.send.setFont(font)
        self.send.setFlat(False)
        self.send.setObjectName("send")
        self.messageArea.addWidget(self.send)
        self.verticalLayout_7.addLayout(self.messageArea)
        self.terminalArea = QtWidgets.QWidget(self.w_console)
        self.terminalArea.setObjectName("terminalArea")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.terminalArea)
        self.horizontalLayout_2.setContentsMargins(0, 8, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.infoArea = QtWidgets.QVBoxLayout()
        self.infoArea.setContentsMargins(20, 0, 0, 5)
        self.infoArea.setSpacing(0)
        self.infoArea.setObjectName("infoArea")
        self.infoLabelArea = QtWidgets.QVBoxLayout()
        self.infoLabelArea.setSpacing(5)
        self.infoLabelArea.setObjectName("infoLabelArea")
        self.connectionLabel = QtWidgets.QLabel(self.terminalArea)
        self.connectionLabel.setMinimumSize(QtCore.QSize(115, 0))
        self.connectionLabel.setMaximumSize(QtCore.QSize(115, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.connectionLabel.setFont(font)
        self.connectionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.connectionLabel.setObjectName("connectionLabel")
        self.infoLabelArea.addWidget(self.connectionLabel)
        self.comportLabel = QtWidgets.QLabel(self.terminalArea)
        self.comportLabel.setMinimumSize(QtCore.QSize(115, 0))
        self.comportLabel.setMaximumSize(QtCore.QSize(115, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.comportLabel.setFont(font)
        self.comportLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.comportLabel.setObjectName("comportLabel")
        self.infoLabelArea.addWidget(self.comportLabel)
        self.baudrateLabel = QtWidgets.QLabel(self.terminalArea)
        self.baudrateLabel.setMinimumSize(QtCore.QSize(115, 0))
        self.baudrateLabel.setMaximumSize(QtCore.QSize(115, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.baudrateLabel.setFont(font)
        self.baudrateLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.baudrateLabel.setObjectName("baudrateLabel")
        self.infoLabelArea.addWidget(self.baudrateLabel)
        self.infoArea.addLayout(self.infoLabelArea)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.infoArea.addItem(spacerItem4)
        self.versionLabel = QtWidgets.QLabel(self.terminalArea)
        self.versionLabel.setMinimumSize(QtCore.QSize(115, 0))
        self.versionLabel.setMaximumSize(QtCore.QSize(115, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.versionLabel.setFont(font)
        self.versionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.versionLabel.setObjectName("versionLabel")
        self.infoArea.addWidget(self.versionLabel)
        self.horizontalLayout_2.addLayout(self.infoArea)
        self.line = QtWidgets.QFrame(self.terminalArea)
        self.line.setMaximumSize(QtCore.QSize(16777215, 190))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.terminalLabel = QtWidgets.QLabel(self.terminalArea)
        self.terminalLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.terminalLabel.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.terminalLabel.setFont(font)
        self.terminalLabel.setObjectName("terminalLabel")
        self.verticalLayout_3.addWidget(self.terminalLabel)
        self.console = QtWidgets.QTextBrowser(self.terminalArea)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.console.setFont(font)
        self.console.setObjectName("console")
        self.verticalLayout_3.addWidget(self.console)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addWidget(self.terminalArea)
        self.gridLayout.addWidget(self.w_console, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 909, 24))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(215, 215, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(215, 215, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.menubar.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(11)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSerial = QtWidgets.QMenu(self.menubar)
        self.menuSerial.setObjectName("menuSerial")
        self.menuBaudrate = QtWidgets.QMenu(self.menuSerial)
        self.menuBaudrate.setObjectName("menuBaudrate")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionBaudRate = QtWidgets.QAction(MainWindow)
        self.actionBaudRate.setObjectName("actionBaudRate")
        self.action9600 = QtWidgets.QAction(MainWindow)
        self.action9600.setObjectName("action9600")
        self.action19200 = QtWidgets.QAction(MainWindow)
        self.action19200.setObjectName("action19200")
        self.action38400 = QtWidgets.QAction(MainWindow)
        self.action38400.setObjectName("action38400")
        self.action57600 = QtWidgets.QAction(MainWindow)
        self.action57600.setObjectName("action57600")
        self.action115200 = QtWidgets.QAction(MainWindow)
        self.action115200.setObjectName("action115200")
        self.menuFile.addAction(self.actionSave)
        self.menuBaudrate.addAction(self.action9600)
        self.menuBaudrate.addAction(self.action19200)
        self.menuBaudrate.addAction(self.action38400)
        self.menuBaudrate.addAction(self.action57600)
        self.menuBaudrate.addAction(self.action115200)
        self.menuSerial.addAction(self.actionBaudRate)
        self.menuSerial.addAction(self.menuBaudrate.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSerial.menuAction())

        self.retranslateUi(MainWindow)
        self.w_page.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Northstar"))
        self.label_7.setText(_translate("MainWindow", "PAGE 2"))
        self.label_8.setText(_translate("MainWindow", "PAGE 3"))
        self.send.setText(_translate("MainWindow", "Send"))
        self.connectionLabel.setText(_translate("MainWindow", "Connection"))
        self.comportLabel.setText(_translate("MainWindow", "COM"))
        self.baudrateLabel.setText(_translate("MainWindow", "115200"))
        self.versionLabel.setText(_translate("MainWindow", "V0.1 Alpha"))
        self.terminalLabel.setText(_translate("MainWindow", "Terminal"))
        self.console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Test</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSerial.setTitle(_translate("MainWindow", "Serial"))
        self.menuBaudrate.setTitle(_translate("MainWindow", "Baudrate"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionBaudRate.setText(_translate("MainWindow", "COM"))
        self.action9600.setText(_translate("MainWindow", "9600"))
        self.action19200.setText(_translate("MainWindow", "19200"))
        self.action38400.setText(_translate("MainWindow", "38400"))
        self.action57600.setText(_translate("MainWindow", "57600"))
        self.action115200.setText(_translate("MainWindow", "115200"))
import resource_rc
