from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from MainWindow import *

import sys
import os

class PasswordWindow(QMainWindow):
	"""Password Access onto the System"""

	def __init__(self):
		super().__init__()

		#Set Window Title
		self.setWindowTitle("Gentle Effects Customer Managment System")

		#"Database Connection"
		self.user_name = "plawrence"
		self.password = "open"

		#create actions
		self.open_program = QAction("Submit",self)
		self.reset = QAction("Reset",self)

		self.logo_image = QPixmap(os.getcwd() + "\gelogo.png")
		self.logo = QLabel()
		self.logo.setPixmap(self.logo_image)
		self.login_button = QPushButton("Login")
		self.reset_button = QPushButton("Reset")
		self.username_lineedit = QLineEdit()
		self.password_lineedit = QLineEdit()
		self.password_lineedit.setEchoMode(2)
		self.username_label = QLabel("Username")
		self.password_label = QLabel("Password")

		self.grid_widget = QGridLayout()
		self.grid_widget.addWidget(self.username_label,0,0)
		self.grid_widget.addWidget(self.username_lineedit,0,1)
		self.grid_widget.addWidget(self.password_label,1,0)
		self.grid_widget.addWidget(self.password_lineedit,1,1)
		self.grid_widget.addWidget(self.reset_button,2,0)
		self.grid_widget.addWidget(self.login_button,2,1)

		self.grid = QWidget()
		self.grid.setLayout(self.grid_widget)

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.logo)
		self.layout.addWidget(self.grid)

		self.widget = QWidget()
		self.widget.setLayout(self.layout)

		self.setCentralWidget(self.widget)

		#Connections
		self.login_button.clicked.connect(self.check_details)
		#self.reset_button.clicked.connect()

	def check_details(self):
		password_error = True
		username_error = True

		if self.username_lineedit.text() == self.user_name:
			#print("Username Checked")
			username_error = False
		if self.password_lineedit.text() == self.password:
			#print("Password Checked")
			password_error = False

		if not username_error and not password_error:
			window1 = MainWindow()
			window1.show()
			window1.raise_()
		else:
			self.error = QErrorMessage()
			self.error.showMessage("Error P001 - Incorrect Username and/or Password","Password Error")
			self.error.setWindowTitle("Username / Password Error")
			
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = PasswordWindow()
    window.show()
    window.raise_()
    application.exec_()
