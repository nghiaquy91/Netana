# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nation_analyse.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(717, 517)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 47, 13))
        self.label_3.setObjectName("label_3")
        self.lineEdit2G = QtWidgets.QLineEdit(Dialog)
        self.lineEdit2G.setGeometry(QtCore.QRect(70, 59, 321, 31))
        self.lineEdit2G.setObjectName("lineEdit2G")
        self.lineEdit3G = QtWidgets.QLineEdit(Dialog)
        self.lineEdit3G.setGeometry(QtCore.QRect(70, 100, 321, 31))
        self.lineEdit3G.setObjectName("lineEdit3G")
        self.lineEdit4G = QtWidgets.QLineEdit(Dialog)
        self.lineEdit4G.setGeometry(QtCore.QRect(70, 140, 321, 31))
        self.lineEdit4G.setObjectName("lineEdit4G")
        self.comboBoxFilter = QtWidgets.QComboBox(Dialog)
        self.comboBoxFilter.setGeometry(QtCore.QRect(70, 190, 321, 22))
        self.comboBoxFilter.setObjectName("comboBoxFilter")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(410, 60, 261, 16))
        self.labelResult.setObjectName("labelResult")
        self.listWidgetResult = QtWidgets.QListWidget(Dialog)
        self.listWidgetResult.setGeometry(QtCore.QRect(410, 80, 256, 411))
        self.listWidgetResult.setObjectName("listWidgetResult")
        self.pushButtonCopy = QtWidgets.QPushButton(Dialog)
        self.pushButtonCopy.setGeometry(QtCore.QRect(284, 452, 111, 41))
        self.pushButtonCopy.setObjectName("pushButtonCopy")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "2G Bands"))
        self.label_2.setText(_translate("Dialog", "3G Bands"))
        self.label_3.setText(_translate("Dialog", "4G Bands"))
        self.lineEdit2G.setText(_translate("Dialog", "850, 900, 1800, 1900"))
        self.lineEdit3G.setText(_translate("Dialog", "B1, B2, B5, B8, B34, B39"))
        self.lineEdit4G.setText(_translate("Dialog", "B1, B2, B3, B5, B7, B8, B38, B39, B40, B41"))
        self.comboBoxFilter.setItemText(0, _translate("Dialog", "Tất cả các quốc gia"))
        self.comboBoxFilter.setItemText(1, _translate("Dialog", "3G có thể hoạt động"))
        self.comboBoxFilter.setItemText(2, _translate("Dialog", "4G có thể hoạt động"))
        self.comboBoxFilter.setItemText(3, _translate("Dialog", "3G/4G có thể hoạt động"))
        self.comboBoxFilter.setItemText(4, _translate("Dialog", "3G và 4G đều không thể hoạt động"))
        self.comboBoxFilter.setItemText(5, _translate("Dialog", "2G, 3G và 4G đều không thể hoạt động"))
        self.comboBoxFilter.setItemText(6, _translate("Dialog", "2G không thể hoạt động"))
        self.labelResult.setText(_translate("Dialog", "Result: "))
        self.pushButtonCopy.setText(_translate("Dialog", "Copy to Clipboard"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
