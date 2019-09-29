# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './retriever/base.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BaseRetrieverWindow(object):
    def setupUi(self, BaseRetrieverWindow):
        BaseRetrieverWindow.setObjectName("BaseRetrieverWindow")
        BaseRetrieverWindow.resize(439, 232)
        self.centralwidget = QtWidgets.QWidget(BaseRetrieverWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output_box = QtWidgets.QGroupBox(self.centralwidget)
        self.output_box.setGeometry(QtCore.QRect(10, 10, 411, 71))
        self.output_box.setObjectName("output_box")
        self.select_button = QtWidgets.QPushButton(self.output_box)
        self.select_button.setGeometry(QtCore.QRect(340, 30, 61, 23))
        self.select_button.setObjectName("select_button")
        self.folder_edit = QtWidgets.QLineEdit(self.output_box)
        self.folder_edit.setGeometry(QtCore.QRect(10, 30, 321, 22))
        self.folder_edit.setObjectName("folder_edit")
        self.filters_box = QtWidgets.QGroupBox(self.centralwidget)
        self.filters_box.setGeometry(QtCore.QRect(10, 90, 271, 131))
        self.filters_box.setObjectName("filters_box")
        self.fullhd_radio = QtWidgets.QRadioButton(self.filters_box)
        self.fullhd_radio.setGeometry(QtCore.QRect(20, 40, 231, 17))
        self.fullhd_radio.setObjectName("fullhd_radio")
        self.widescr_radio = QtWidgets.QRadioButton(self.filters_box)
        self.widescr_radio.setGeometry(QtCore.QRect(20, 60, 201, 17))
        self.widescr_radio.setObjectName("widescr_radio")
        self.custom_radio = QtWidgets.QRadioButton(self.filters_box)
        self.custom_radio.setGeometry(QtCore.QRect(20, 80, 131, 17))
        self.custom_radio.setObjectName("custom_radio")
        self.none_radio = QtWidgets.QRadioButton(self.filters_box)
        self.none_radio.setGeometry(QtCore.QRect(20, 20, 201, 17))
        self.none_radio.setObjectName("none_radio")
        self.custom_width = QtWidgets.QLineEdit(self.filters_box)
        self.custom_width.setGeometry(QtCore.QRect(90, 100, 42, 22))
        self.custom_width.setObjectName("custom_width")
        self.width_label = QtWidgets.QLabel(self.filters_box)
        self.width_label.setGeometry(QtCore.QRect(50, 103, 31, 16))
        self.width_label.setObjectName("width_label")
        self.height_label = QtWidgets.QLabel(self.filters_box)
        self.height_label.setGeometry(QtCore.QRect(158, 105, 47, 13))
        self.height_label.setObjectName("height_label")
        self.custom_height = QtWidgets.QLineEdit(self.filters_box)
        self.custom_height.setGeometry(QtCore.QRect(200, 100, 42, 22))
        self.custom_height.setObjectName("custom_height")
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(370, 190, 51, 23))
        self.run_button.setObjectName("run_button")
        self.close_option = QtWidgets.QCheckBox(self.centralwidget)
        self.close_option.setGeometry(QtCore.QRect(310, 160, 111, 17))
        self.close_option.setObjectName("close_option")
        self.open_option = QtWidgets.QCheckBox(self.centralwidget)
        self.open_option.setGeometry(QtCore.QRect(310, 140, 111, 17))
        self.open_option.setObjectName("open_option")
        BaseRetrieverWindow.setCentralWidget(self.centralwidget)
        self.credits_menu = QtWidgets.QAction(BaseRetrieverWindow)
        self.credits_menu.setObjectName("credits_menu")
        self.exit_menu = QtWidgets.QAction(BaseRetrieverWindow)
        self.exit_menu.setObjectName("exit_menu")

        self.retranslateUi(BaseRetrieverWindow)
        QtCore.QMetaObject.connectSlotsByName(BaseRetrieverWindow)

    def retranslateUi(self, BaseRetrieverWindow):
        _translate = QtCore.QCoreApplication.translate
        BaseRetrieverWindow.setWindowTitle(_translate("BaseRetrieverWindow", "Spotlight Retriever"))
        self.output_box.setTitle(_translate("BaseRetrieverWindow", "Output folder"))
        self.select_button.setText(_translate("BaseRetrieverWindow", "Select"))
        self.filters_box.setTitle(_translate("BaseRetrieverWindow", "Filters"))
        self.fullhd_radio.setText(_translate("BaseRetrieverWindow", "Full HD images"))
        self.widescr_radio.setText(_translate("BaseRetrieverWindow", "Widescreen images"))
        self.custom_radio.setText(_translate("BaseRetrieverWindow", "Custom size"))
        self.none_radio.setText(_translate("BaseRetrieverWindow", "None"))
        self.width_label.setText(_translate("BaseRetrieverWindow", "Width"))
        self.height_label.setText(_translate("BaseRetrieverWindow", "Height"))
        self.run_button.setText(_translate("BaseRetrieverWindow", "Run"))
        self.close_option.setText(_translate("BaseRetrieverWindow", "Close when done"))
        self.open_option.setText(_translate("BaseRetrieverWindow", "Open folder"))
        self.credits_menu.setText(_translate("BaseRetrieverWindow", "Credits"))
        self.exit_menu.setText(_translate("BaseRetrieverWindow", "Exit"))

