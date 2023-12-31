# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(486, 436)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        Dialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(150, 390, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.author_input = QtWidgets.QLineEdit(Dialog)
        self.author_input.setGeometry(QtCore.QRect(160, 300, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.author_input.setFont(font)
        self.author_input.setObjectName("author_input")
        self.name_input = QtWidgets.QLineEdit(Dialog)
        self.name_input.setGeometry(QtCore.QRect(160, 110, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.name_input.setFont(font)
        self.name_input.setObjectName("name_input")
        self.description_input = QtWidgets.QLineEdit(Dialog)
        self.description_input.setGeometry(QtCore.QRect(160, 150, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.description_input.setFont(font)
        self.description_input.setObjectName("description_input")
        self.id_input = QtWidgets.QSpinBox(Dialog)
        self.id_input.setEnabled(True)
        self.id_input.setGeometry(QtCore.QRect(160, 70, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.id_input.setFont(font)
        self.id_input.setMaximum(10000)
        self.id_input.setObjectName("id_input")
        self.page_count_input = QtWidgets.QSpinBox(Dialog)
        self.page_count_input.setGeometry(QtCore.QRect(160, 230, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.page_count_input.setFont(font)
        self.page_count_input.setMaximum(10000)
        self.page_count_input.setObjectName("page_count_input")
        self.isbn_input = QtWidgets.QLineEdit(Dialog)
        self.isbn_input.setGeometry(QtCore.QRect(160, 190, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.isbn_input.setFont(font)
        self.isbn_input.setObjectName("isbn_input")
        self.yes_button = QtWidgets.QRadioButton(Dialog)
        self.yes_button.setGeometry(QtCore.QRect(160, 270, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.yes_button.setFont(font)
        self.yes_button.setObjectName("yes_button")
        self.no_button = QtWidgets.QRadioButton(Dialog)
        self.no_button.setGeometry(QtCore.QRect(310, 270, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.no_button.setFont(font)
        self.no_button.setObjectName("no_button")
        self.year_input = QtWidgets.QSpinBox(Dialog)
        self.year_input.setGeometry(QtCore.QRect(160, 340, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.year_input.setFont(font)
        self.year_input.setMaximum(5000)
        self.year_input.setObjectName("year_input")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 70, 134, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ADD BOOK"))
        self.yes_button.setText(_translate("Dialog", "Yes"))
        self.no_button.setText(_translate("Dialog", "No"))
        self.label_2.setText(_translate("Dialog", "ID"))
        self.label_3.setText(_translate("Dialog", "Name"))
        self.label_5.setText(_translate("Dialog", "Description"))
        self.label_6.setText(_translate("Dialog", "ISBN"))
        self.label_7.setText(_translate("Dialog", "Page Count"))
        self.label_4.setText(_translate("Dialog", "Issued"))
        self.label_9.setText(_translate("Dialog", "Author"))
        self.label_8.setText(_translate("Dialog", "Year"))
