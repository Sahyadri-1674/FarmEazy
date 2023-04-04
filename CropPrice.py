# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CropPrice.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QTableWidgetItem, QLabel,QPushButton
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QColor,QIcon
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
class Ui_Dialog(object):
    def setupUi(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1184, 628)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        # font1 = QFont()
        # font1.setPointSize(18)
        # self.comboBox.setFont(font1)
        self.comboBox.setGeometry(QtCore.QRect(330, 160, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setEditable(True)

        # Set the placeholder text for the QLineEdit widget
        line_edit = self.comboBox.lineEdit()
        line_edit.setPlaceholderText('Select an option')
        self.comboBox.setStyleSheet('''
                    QComboBox {
                        background-color: lightgreen;
                        border-style: solid;
                        border-width: 3px;
                        border-color: black;
                        border-radius: 5px;
                        padding: 1px 18px 1px 3px;
                        min-width: 6em;
                    }
                ''')
        self.comboBox.addItems(['Apple','Bajri','Banana','Beet Root','Bitter Gourd','Brinjal','Cabbage','Capsicum','Carrot','Chavli(Pala)','Chavli(Shenga)','Chickoo','Coriander','Cotton','Cucumber','Farshi','Flower','Gram','Grapes','Green Chilli','Green Gram(mug)','Guava','Ladies Finger','Lemon','Maize','Mango','Methi','Onion','Orange','Pomegranet','Potato','Pumpkin','Raddish','Shevga','Soyabean','Tomato','Turmeric','Water melon'])

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 160, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label.setStyleSheet('''QLabel{background-color: cyan;border-style: solid;
                        border-width: 2px;
                        border-color: black;
                        border-radius: 5px;
                        
                        min-width: 6em;}''')

        # rq = self.comboBox.currentText()
        # print(type(rq))
        # print(rq)


        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(910, 160, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('QPushButton { background-color: #00FFFF; color: black; border: 2px solid #000000;}'
                             'QPushButton:hover { background-color: #3E8E41; }')

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(100, 290, 971, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setStyleSheet("QTableWidget {border: 2px solid black;}")
        self.tableWidget.setColumnWidth(0, 200)

        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color: lightblue; border: 1px solid black;}")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        button = QPushButton(Dialog)
        pixmap = QPixmap('images/eco-home.png')
        icon = QIcon(pixmap)
        button.setIcon(icon)
        button.setIconSize(pixmap.size())

        # Set the button's size and position
        button.resize(pixmap.width(), pixmap.height())
        button.move(50, 550)
        button.clicked.connect(self.on_button_click)


    def on_button_click(self):
        print('Button clicked')
        import newDashboard
        self.close()
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select Crop "))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "APMC"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Variety"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Unit"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Lrate"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Hrate"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Modal"))




# Import the user interface code


class MyDialog(QtWidgets.QDialog):

    def __init__(self):

        super().__init__()
        self.setStyleSheet("background-color: white;")
        label = QLabel(self)
        pixmap = QPixmap('images/cropimage2.png')
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        opacity_effect = QGraphicsOpacityEffect(self)
        opacity_effect.setOpacity(0.8)
        label.setGraphicsEffect(opacity_effect)
        # pixmap = QPixmap("images/cropimage.png")
        #
        # # Create a QLabel object and set the pixmap as its content
        # label = QLabel(self)
        # label.setPixmap(pixmap)
        #
        # # Resize the label to the width of the window and maintain its aspect ratio
        # label.setScaledContents(True)
        # label.setFixedSize(800, 205)

        # Set up the user interface from the Designer file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # reqCrop = self.ui.comboBox.currentText()
        # print(reqCrop)
        # Connect signals to slots
        self.ui.pushButton.clicked.connect(self.submit)

    def submit(self):
        print("hi")
        try:
            import pandas as pd

            # readFile = input("Enter the Commodity")
            # readFile = readFile.capitalize()
            # s1 = rq
            # print("I am s1",s1,type(s1))
            # s2=".csv"
            # s3 = "".join([s1, s2])
            # print(s3)
            # print(type(s3))
            reqCrop = self.ui.comboBox.currentText()
            print(reqCrop)
            datafile = pd.read_csv('CsvFiles/'+reqCrop+'.csv')

            df = pd.DataFrame(datafile)
            self.ui.tableWidget.setRowCount(df.shape[0])
            self.ui.tableWidget.setColumnCount(df.shape[1])

            # Add the data from the dataframe to the table.
            for i in range(df.shape[0]):
                for j in range(df.shape[1]):
                    item = QTableWidgetItem(str(df.iloc[i, j]))
                    self.ui.tableWidget.setItem(i, j, item)
            # Handle the submit button click event
            print("Submit button clicked")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Create and show the dialog
    dialog = MyDialog()
    dialog.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
    dialog.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
    dialog.show()

    sys.exit(app.exec_())

