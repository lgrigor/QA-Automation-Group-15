# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(937, 713)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.App = QtWidgets.QGridLayout()
        self.App.setObjectName("App")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.App.addItem(spacerItem, 4, 2, 1, 1)
        self.Terminal = QtWidgets.QGridLayout()
        self.Terminal.setObjectName("Terminal")
        self.features_line = QtWidgets.QFrame(Dialog)
        self.features_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.features_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.features_line.setObjectName("features_line")
        self.Terminal.addWidget(self.features_line, 5, 1, 1, 1)
        self.terminal_title_lbl = QtWidgets.QLabel(Dialog)
        self.terminal_title_lbl.setObjectName("terminal_title_lbl")
        self.Terminal.addWidget(self.terminal_title_lbl, 2, 1, 1, 1)
        self.terminal_output = QtWidgets.QTextEdit(Dialog)
        self.terminal_output.setReadOnly(True)
        self.terminal_output.setObjectName("terminal_output")
        self.Terminal.addWidget(self.terminal_output, 3, 1, 1, 1)
        self.features = QtWidgets.QGridLayout()
        self.features.setObjectName("features")
        self.to_fld = QtWidgets.QLineEdit(Dialog)
        self.to_fld.setObjectName("to_fld")
        self.features.addWidget(self.to_fld, 2, 1, 1, 1)
        self.to_lbl = QtWidgets.QLabel(Dialog)
        self.to_lbl.setObjectName("to_lbl")
        self.features.addWidget(self.to_lbl, 2, 0, 1, 1)
        self.from_lbl = QtWidgets.QLabel(Dialog)
        self.from_lbl.setObjectName("from_lbl")
        self.features.addWidget(self.from_lbl, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.features.addItem(spacerItem1, 1, 5, 1, 1)
        self.filter_btn = QtWidgets.QPushButton(Dialog)
        self.filter_btn.setObjectName("filter_btn")
        self.features.addWidget(self.filter_btn, 1, 4, 1, 1)
        self.from_fld = QtWidgets.QLineEdit(Dialog)
        self.from_fld.setObjectName("from_fld")
        self.features.addWidget(self.from_fld, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.features.addItem(spacerItem2, 1, 6, 1, 1)
        self.reset_btn = QtWidgets.QPushButton(Dialog)
        self.reset_btn.setObjectName("reset_btn")
        self.features.addWidget(self.reset_btn, 1, 7, 1, 1)
        self.Terminal.addLayout(self.features, 6, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Terminal.addItem(spacerItem3, 4, 1, 1, 1)
        self.App.addLayout(self.Terminal, 5, 2, 1, 1)
        self.terminal_line = QtWidgets.QFrame(Dialog)
        self.terminal_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.terminal_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.terminal_line.setObjectName("terminal_line")
        self.App.addWidget(self.terminal_line, 3, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.App.addItem(spacerItem4, 6, 2, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.App.addWidget(self.line, 1, 2, 1, 1)
        self.AddItem = QtWidgets.QGridLayout()
        self.AddItem.setObjectName("AddItem")
        self.add_item_title_lbl = QtWidgets.QLabel(Dialog)
        self.add_item_title_lbl.setObjectName("add_item_title_lbl")
        self.AddItem.addWidget(self.add_item_title_lbl, 0, 0, 1, 1)
        self.name_fld = QtWidgets.QLineEdit(Dialog)
        self.name_fld.setObjectName("name_fld")
        self.AddItem.addWidget(self.name_fld, 2, 0, 1, 1)
        self.name_lbl = QtWidgets.QLabel(Dialog)
        self.name_lbl.setObjectName("name_lbl")
        self.AddItem.addWidget(self.name_lbl, 1, 0, 1, 1)
        self.add_item_btn = QtWidgets.QPushButton(Dialog)
        self.add_item_btn.setObjectName("add_item_btn")
        self.AddItem.addWidget(self.add_item_btn, 2, 3, 1, 1)
        self.quantity_lbl = QtWidgets.QLabel(Dialog)
        self.quantity_lbl.setObjectName("quantity_lbl")
        self.AddItem.addWidget(self.quantity_lbl, 1, 2, 1, 1)
        self.price_lbl = QtWidgets.QLabel(Dialog)
        self.price_lbl.setObjectName("price_lbl")
        self.AddItem.addWidget(self.price_lbl, 1, 1, 1, 1)
        self.quantity_fld = QtWidgets.QLineEdit(Dialog)
        self.quantity_fld.setObjectName("quantity_fld")
        self.AddItem.addWidget(self.quantity_fld, 2, 2, 1, 1)
        self.price_fld = QtWidgets.QLineEdit(Dialog)
        self.price_fld.setObjectName("price_fld")
        self.AddItem.addWidget(self.price_fld, 2, 1, 1, 1)
        self.App.addLayout(self.AddItem, 2, 2, 1, 1)
        self.import_from_csv = QtWidgets.QGridLayout()
        self.import_from_csv.setObjectName("import_from_csv")
        self.select_file_fld = QtWidgets.QLineEdit(Dialog)
        self.select_file_fld.setObjectName("select_file_fld")
        self.select_file_fld.setAcceptDrops(True)
        self.import_from_csv.addWidget(self.select_file_fld, 1, 0, 1, 1)
        self.import_title_lbl = QtWidgets.QLabel(Dialog)
        self.import_title_lbl.setObjectName("import_title_lbl")
        self.import_from_csv.addWidget(self.import_title_lbl, 0, 0, 1, 1)
        self.import_btn = QtWidgets.QPushButton(Dialog)
        self.import_btn.setObjectName("import_btn")
        self.import_from_csv.addWidget(self.import_btn, 1, 1, 1, 1)
        self.App.addLayout(self.import_from_csv, 0, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.App.addItem(spacerItem5, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.App.addItem(spacerItem6, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.App, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.terminal_title_lbl.setText(_translate("Dialog", "Total Items:"))
        self.to_lbl.setText(_translate("Dialog", "to: "))
        self.from_lbl.setText(_translate("Dialog", "from: "))
        self.filter_btn.setText(_translate("Dialog", "Filter"))
        self.reset_btn.setText(_translate("Dialog", "Reset"))
        self.add_item_title_lbl.setText(_translate("Dialog", "Add Item:"))
        self.name_lbl.setText(_translate("Dialog", "Name:"))
        self.add_item_btn.setText(_translate("Dialog", "Add"))
        self.quantity_lbl.setText(_translate("Dialog", "Quantity:"))
        self.price_lbl.setText(_translate("Dialog", "Price:"))
        self.import_title_lbl.setText(_translate("Dialog", "Import items from csv file:"))
        self.import_btn.setText(_translate("Dialog", "Import"))
