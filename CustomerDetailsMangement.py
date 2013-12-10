from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import os

class CustomerDetailsManagement(QMainWindow):
	"""Customer Details Management Main Screen"""

	def __init__(self):
		super().__init__()

		self.setWindowTitle("Customer Management | Gentle Effects CMS")

		self.logo_image = QPixmap(os.getcwd()+"\gelogo.png")
		self.logo = QLabel()
		self.logo.setPixmap(self.logo_image)

		self.title_label = QLabel("""<html>
					 					 <body>
					       					<p><span style=" font-size:16pt; font-weight:1000;">Customer Details Managment</span></p>
					 					 </body>
				    				 </html>""")

		self.new_pushbutton = QPushButton("Add New Customer")
		self.edit_pushbutton = QPushButton("Edit Existing Customer")
		self.allergy_pushbutton = QPushButton("Add Allergy")
		self.editAllergy_pushbutton = QPushButton("Edit Allergy")
		self.delete_pushbutton = QPushButton("7 Year - Bulk Delete")

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.logo)
		self.layout.addWidget(self.title_label)
		self.layout.addWidget(self.new_pushbutton)
		self.layout.addWidget(self.edit_pushbutton)
		self.layout.addWidget(self.allergy_pushbutton)
		self.layout.addWidget(self.editAllergy_pushbutton)
		self.layout.addWidget(self.delete_pushbutton)

		self.widget = QWidget()
		self.widget.setLayout(self.layout)

		self.setCentralWidget(self.widget)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = CustomerDetailsManagement()
    window.show()
    window.raise_()
    application.exec_()

