# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Qt\HMI_Lakban\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pb_rework = QtWidgets.QPushButton(self.centralWidget)
        self.pb_rework.setGeometry(QtCore.QRect(570, 70, 201, 381))
        self.pb_rework.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.pb_rework.setFlat(False)
        self.pb_rework.setObjectName("pb_rework")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(570, 20, 201, 41))
        self.label_9.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 255);")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.horizontalGroupBox.setGeometry(QtCore.QRect(29, 69, 521, 41))
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.horizontalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 131);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.label_8 = QtWidgets.QLabel(self.horizontalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 131);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.gridGroupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.gridGroupBox.setGeometry(QtCore.QRect(30, 120, 521, 331))
        self.gridGroupBox.setObjectName("gridGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.gridGroupBox)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_line24 = QtWidgets.QPushButton(self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_line24.sizePolicy().hasHeightForWidth())
        self.pb_line24.setSizePolicy(sizePolicy)
        self.pb_line24.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 255);\n"
"border-color: rgb(0, 0, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pb_line24.setFlat(False)
        self.pb_line24.setObjectName("pb_line24")
        self.gridLayout.addWidget(self.pb_line24, 1, 0, 1, 1)
        self.val_line23 = QtWidgets.QLabel(self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val_line23.sizePolicy().hasHeightForWidth())
        self.val_line23.setSizePolicy(sizePolicy)
        self.val_line23.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(214, 214, 214);")
        self.val_line23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.val_line23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.val_line23.setWordWrap(False)
        self.val_line23.setObjectName("val_line23")
        self.gridLayout.addWidget(self.val_line23, 0, 1, 1, 1)
        self.pb_line23 = QtWidgets.QPushButton(self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_line23.sizePolicy().hasHeightForWidth())
        self.pb_line23.setSizePolicy(sizePolicy)
        self.pb_line23.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 255);\n"
"border-color: rgb(0, 0, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pb_line23.setFlat(False)
        self.pb_line23.setObjectName("pb_line23")
        self.gridLayout.addWidget(self.pb_line23, 0, 0, 1, 1)
        self.pb_line25 = QtWidgets.QPushButton(self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_line25.sizePolicy().hasHeightForWidth())
        self.pb_line25.setSizePolicy(sizePolicy)
        self.pb_line25.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 255);\n"
"border-color: rgb(0, 0, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pb_line25.setFlat(False)
        self.pb_line25.setObjectName("pb_line25")
        self.gridLayout.addWidget(self.pb_line25, 2, 0, 1, 1)
        self.pb_line26 = QtWidgets.QPushButton(self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_line26.sizePolicy().hasHeightForWidth())
        self.pb_line26.setSizePolicy(sizePolicy)
        self.pb_line26.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 255);\n"
"border-color: rgb(0, 0, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pb_line26.setFlat(False)
        self.pb_line26.setObjectName("pb_line26")
        self.gridLayout.addWidget(self.pb_line26, 3, 0, 1, 1)
        self.val_line24 = QtWidgets.QLabel(self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val_line24.sizePolicy().hasHeightForWidth())
        self.val_line24.setSizePolicy(sizePolicy)
        self.val_line24.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(214, 214, 214);")
        self.val_line24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.val_line24.setObjectName("val_line24")
        self.gridLayout.addWidget(self.val_line24, 1, 1, 1, 1)
        self.val_line25 = QtWidgets.QLabel(self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val_line25.sizePolicy().hasHeightForWidth())
        self.val_line25.setSizePolicy(sizePolicy)
        self.val_line25.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(214, 214, 214);")
        self.val_line25.setTextFormat(QtCore.Qt.AutoText)
        self.val_line25.setScaledContents(False)
        self.val_line25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.val_line25.setWordWrap(False)
        self.val_line25.setIndent(-1)
        self.val_line25.setObjectName("val_line25")
        self.gridLayout.addWidget(self.val_line25, 2, 1, 1, 1)
        self.val_line26 = QtWidgets.QLabel(self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val_line26.sizePolicy().hasHeightForWidth())
        self.val_line26.setSizePolicy(sizePolicy)
        self.val_line26.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(214, 214, 214);")
        self.val_line26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.val_line26.setObjectName("val_line26")
        self.gridLayout.addWidget(self.val_line26, 3, 1, 1, 1)
        self.horizontalWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(30, 20, 160, 41))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.time_lbl = QtWidgets.QLabel(self.horizontalWidget)
        self.time_lbl.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.time_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.time_lbl.setObjectName("time_lbl")
        self.horizontalLayout.addWidget(self.time_lbl)
        self.label = QtWidgets.QLabel(self.horizontalWidget)
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.shift_lbl = QtWidgets.QLabel(self.horizontalWidget)
        self.shift_lbl.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.shift_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.shift_lbl.setObjectName("shift_lbl")
        self.horizontalLayout.addWidget(self.shift_lbl)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb_rework.setText(_translate("MainWindow", "REWORK"))
        self.label_9.setText(_translate("MainWindow", "HMI Lakban"))
        self.label_10.setText(_translate("MainWindow", "Total"))
        self.label_8.setText(_translate("MainWindow", "Line"))
        self.pb_line24.setText(_translate("MainWindow", "Line 24"))
        self.val_line23.setText(_translate("MainWindow", "1500"))
        self.pb_line23.setText(_translate("MainWindow", "Line 23"))
        self.pb_line25.setText(_translate("MainWindow", "Line 25"))
        self.pb_line26.setText(_translate("MainWindow", "Line 26"))
        self.val_line24.setText(_translate("MainWindow", "1500"))
        self.val_line25.setText(_translate("MainWindow", "1500"))
        self.val_line26.setText(_translate("MainWindow", "1500"))
        self.time_lbl.setText(_translate("MainWindow", "09:45"))
        self.label.setText(_translate("MainWindow", "|"))
        self.shift_lbl.setText(_translate("MainWindow", "Shift 1"))

