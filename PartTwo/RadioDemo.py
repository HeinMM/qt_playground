# Form implementation generated from reading ui file 'RadioDemo.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(499, 392)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 190, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_result = QtWidgets.QLabel(parent=Dialog)
        self.label_result.setGeometry(QtCore.QRect(30, 350, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(70, 60, 78, 74))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_py = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton_py.setObjectName("radioButton_py")

        self.radioButton_py.toggled.connect(self.radio_selected)

        self.verticalLayout.addWidget(self.radioButton_py)
        self.radioButton_java = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton_java.setObjectName("radioButton_java")

        self.radioButton_java.toggled.connect(self.radio_selected)

        self.verticalLayout.addWidget(self.radioButton_java)
        self.radioButton_js = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton_js.setObjectName("radioButton_js")

        self.radioButton_js.toggled.connect(self.radio_selected)

        self.verticalLayout.addWidget(self.radioButton_js)
        self.widget1 = QtWidgets.QWidget(parent=Dialog)
        self.widget1.setGeometry(QtCore.QRect(70, 240, 60, 74))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_card = QtWidgets.QRadioButton(parent=self.widget1)
        self.radioButton_card.setObjectName("radioButton_card")

        self.radioButton_card.toggled.connect(self.radio_selected)

        self.verticalLayout_2.addWidget(self.radioButton_card)
        self.radioButton_paypal = QtWidgets.QRadioButton(parent=self.widget1)
        self.radioButton_paypal.setObjectName("radioButton_paypal")

        self.radioButton_paypal.toggled.connect(self.radio_selected)

        self.verticalLayout_2.addWidget(self.radioButton_paypal)
        self.radioButton_cash = QtWidgets.QRadioButton(parent=self.widget1)
        self.radioButton_cash.setObjectName("radioButton_cash")

        self.radioButton_cash.toggled.connect(self.radio_selected)

        self.verticalLayout_2.addWidget(self.radioButton_cash)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def radio_selected(self):
        selected1 = ""
        selected2 = ""
        if self.radioButton_py.isChecked() == True:
            selected1 = "Python"
        if self.radioButton_java.isChecked() == True:
            selected1 = "Java"

        if self.radioButton_js.isChecked() == True:
            selected1 = "JavaScript"

        if self.radioButton_card.isChecked() == True:
            selected2 = "Debit/Credit Card"

        if self.radioButton_paypal.isChecked() == True:
            selected2 = "Paypal"

        if self.radioButton_cash.isChecked() == True:
            selected2 = "Cash"

        self.label_result.setText(" Chosen Book " + selected1 + " Chosen Payment Method " + selected2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose Your Book"))
        self.label_2.setText(_translate("Dialog", "Choose Your Payment Method"))
        self.label_result.setText(_translate("Dialog", "TextLabel"))
        self.radioButton_py.setText(_translate("Dialog", "Python"))
        self.radioButton_java.setText(_translate("Dialog", "Java"))
        self.radioButton_js.setText(_translate("Dialog", "JavaScript"))
        self.radioButton_card.setText(_translate("Dialog", "Card"))
        self.radioButton_paypal.setText(_translate("Dialog", "Paypal"))
        self.radioButton_cash.setText(_translate("Dialog", "Cash"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())