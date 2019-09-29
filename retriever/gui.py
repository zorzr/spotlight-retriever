import os
import sys
import ctypes
from PyQt5 import QtWidgets, QtGui
from base import Ui_BaseRetrieverWindow
import retriever

default_output = os.path.abspath(retriever.name)


class RetrieverWindow(QtWidgets.QMainWindow, Ui_BaseRetrieverWindow):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.setupUi(self)
		self.initUi()
		# self.show()
	
	def initUi(self):
		self.folder_edit.setText(default_output)
		self.none_radio.setChecked(True)
		self.close_option.setChecked(True)
		self.open_option.setChecked(True)

		self.folder_edit.setReadOnly(True)
		self.select_button.clicked.connect(self.select_folder)

		self.toggle_custom_group()
		self.custom_radio.toggled.connect(self.toggle_custom_group)
		self.custom_width.setValidator(QtGui.QIntValidator(1, 5000))
		self.custom_height.setValidator(QtGui.QIntValidator(1, 5000))
		self.custom_width.setText("1080")
		self.custom_height.setText("1920")

		self.run_button.clicked.connect(self.run)

	def toggle_custom_group(self):
		value = not self.custom_radio.isChecked()
		self.width_label.setDisabled(value)
		self.custom_width.setDisabled(value)
		self.height_label.setDisabled(value)
		self.custom_height.setDisabled(value)
	
	def select_folder(self):
		selected_folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select folder")
		if selected_folder:
			self.folder_edit.setText(selected_folder)

	def run(self):
		retriever.name = self.folder_edit.text()
		if not os.path.exists(retriever.name):
			os.mkdir(retriever.name)

		image_list = retriever.retrieve_images()

		if self.fullhd_radio.isChecked():
			filter1 = retriever.filter_images(image_list, 1920, 1080)
			filter2 = retriever.filter_images(image_list, 1080, 1920)
			retriever.remove_unfiltered(image_list, filter1 + filter2)
		elif self.widescr_radio.isChecked():
			image_filter = retriever.filter_images(image_list, 1920, 1080)
			retriever.remove_unfiltered(image_list, image_filter)
		elif self.custom_radio.isChecked():
			image_filter = retriever.filter_images(image_list, int(self.custom_width.text()), int(self.custom_height.text()))
			retriever.remove_unfiltered(image_list, image_filter)
		
		if self.open_option.isChecked():
			os.startfile(retriever.name)
		
		if self.close_option.isChecked():
			self.close()
		else:
			notify_success()


def notify_success():
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setWindowTitle("Success!")
    msg.setText("The task was completed successfully!")
    msg.setStyleSheet("QLabel { margin-right: 7px; }")
    msg.exec_()


def error_message(text):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setWindowTitle("Error")
    msg.setText(text)
    msg.setStyleSheet("QLabel { margin-right: 7px; }")
    msg.exec_()


def check_spotlight():
	if not os.path.isdir(retriever.folder):
		error_message("Cannot find Spotlight folder")
		exit(1)
	
	if len(os.listdir(retriever.folder)) == 0:
		error_message("Spotlight folder is empty.\nPlease make sure it is enabled")
		exit(2)


def start():
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('zorzr.spotlight')
	app = QtWidgets.QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon('icon.png'))

	check_spotlight()
	window = RetrieverWindow()
	window.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	start()
