from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import re

class AddSupplier(QWidget):
	"""Adding Supplier data to SQL Database with PyQt4"""

	supplierAddedSignal = pyqtSignal()

	def __init__(self):
		super().__init__()
		
		self.title_label = QLabel("""<html>
					  <body>
					       <p><span style=" font-size:16pt; font-weight:1000;">New Supplier</span></p>
					  </body>
				     </html>""")

		#AMMENDMENT FUNCTIONALITY
		self.combo_box = QComboBox()
		self.combo_box.hide()
		self.re_amend_button = QPushButton("Amend Previously Amended Details")
		self.re_amend_button.hide()
		

		self.name_label = QLabel("Supplier Name")
		self.number_label = QLabel("House Name / Number")
		self.road_label = QLabel("Road")
		self.city_label = QLabel("Town / City")
		self.county_label = QLabel("County")
		self.postcode_label = QLabel("Postcode")
		self.contact_label = QLabel("Contact Number")
		self.email_label = QLabel("Email")
		self.website_label = QLabel("Website")
		
		self.name_lineedit = QLineEdit()
		self.number_lineedit = QLineEdit()
		self.road_lineedit = QLineEdit()
		self.city_lineedit = QLineEdit()
		self.county_lineedit = QLineEdit()
		self.postcode_lineedit = QLineEdit()
		self.contact_lineedit = QLineEdit()
		self.email_lineedit = QLineEdit()
		self.website_lineedit = QLineEdit()

		self.save_button = QPushButton("Save New Supplier")
		self.reset_button = QPushButton("Reset")

		self.error_label = QLabel("Errors to Appear Here")

		self.data_layout = QGridLayout()
		self.data_layout.addWidget(self.name_label,0,0)
		self.data_layout.addWidget(self.name_lineedit,0,1)
		self.data_layout.addWidget(self.number_label,1,0)
		self.data_layout.addWidget(self.number_lineedit,1,1)
		self.data_layout.addWidget(self.road_label,2,0)
		self.data_layout.addWidget(self.road_lineedit,2,1)
		self.data_layout.addWidget(self.city_label,3,0)
		self.data_layout.addWidget(self.city_lineedit,3,1)
		self.data_layout.addWidget(self.county_label,4,0)
		self.data_layout.addWidget(self.county_lineedit,4,1)
		self.data_layout.addWidget(self.postcode_label,5,0)
		self.data_layout.addWidget(self.postcode_lineedit,5,1)
		self.data_layout.addWidget(self.contact_label,6,0)
		self.data_layout.addWidget(self.contact_lineedit,6,1)
		self.data_layout.addWidget(self.email_label,7,0)
		self.data_layout.addWidget(self.email_lineedit,7,1)
		self.data_layout.addWidget(self.website_label,8,0)
		self.data_layout.addWidget(self.website_lineedit,8,1)
		self.data_widget = QWidget()
		self.data_widget.setLayout(self.data_layout)

		self.button_layout = QHBoxLayout()
		self.button_layout.addWidget(self.save_button)
		self.button_layout.addWidget(self.reset_button)
		self.button_widget = QWidget()
		self.button_widget.setLayout(self.button_layout)

		self.main_layout = QVBoxLayout()
		self.main_layout.addWidget(self.title_label)
		self.main_layout.addWidget(self.combo_box)
		self.main_layout.addWidget(self.error_label)
		self.main_layout.addWidget(self.data_widget)
		self.main_layout.addWidget(self.button_widget)
		self.main_layout.addWidget(self.re_amend_button)
		self.setLayout(self.main_layout)

		self.error_label.hide()

		#connections
		self.reset_button.clicked.connect(self.reset_data)
		self.save_button.clicked.connect(self.save_data)

	def validate_data(self):
		pass


	def save_data(self):
		details = self.product_details()
		self.supplierAddedSignal.emit()
		self.save_button.setEnabled(False)
		self.error_label.setText("Supplier Added Succesfully")
		self.error_label.show()

	def reset_data(self):
		self.name_lineedit.clear()
		self.number_lineedit.clear()
		self.road_lineedit.clear()
		self.city_lineedit.clear()
		self.county_lineedit.clear()
		self.postcode_lineedit.clear()
		self.contact_lineedit.clear()
		self.email_lineedit.clear()
		self.website_lineedit.clear()
		self.save_button.setEnabled(True)
		self.error_label.hide()

	def product_details(self):
		details = {'Name':self.name_lineedit.text(),
			   'House':self.number_lineedit.text(),
			   'Road':self.road_lineedit.text(),
			   'City':self.city_lineedit.text(),
			   'County':self.county_lineedit.text(),
			   'PostCode':self.postcode_lineedit.text(),
			   'ContactNum':self.contact_lineedit.text(),
			   'Email':self.email_lineedit.text(),
			   'Website':self.website_lineedit.text()}
		return details

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = AddCustomer()
    window.show()
    window.raise_()
    application.exec_()
