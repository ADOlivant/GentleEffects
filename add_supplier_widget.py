from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import re

class AddSupplier(QWidget):
	"""Adding Supplier data to SQL Database with PyQt4"""

	def __init__(self):
		super().__init__()

		self.setWindowTitle("Add Customer Details | Gentle Effects CMS")

		#self.db = QSqlDatabase.addDatabase("QSQLITE")
		#self.db.setDatabaseName("GentleEffects.db")
		#self.db.open()

		#self.pragma_on = QSqlQuery()
		#self.pragma_on.prepare("""PRAGMA foreign_keys = ON""")
		#self.pragma_on.exec_()

		self.title_label = QLabel("""<html>
					  <body>
					       <p><span style=" font-size:16pt; font-weight:1000;">New Supplier</span></p>
					  </body>
				     </html>""")

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
		self.main_layout.addWidget(self.error_label)
		self.main_layout.addWidget(self.data_widget)
		self.main_layout.addWidget(self.button_widget)
		#self.main_widget = QWidget()
		self.setLayout(self.main_layout)

		self.error_label.hide()

		#self.setCentralWidget(self.main_widget)

		#connections
		self.reset_button.clicked.connect(self.reset_data)
		self.save_button.clicked.connect(self.save_data)

	def validate_data(self):
		pass


	def save_data(self):
                details = self.customer_details()
		self.query = QSqlQuery()
		self.query.prepare("""INSERT INTO Customer(FirstName,LastName,DateOfBirth,
                                                           House,Road,City,County,PostCode,
                                                           MobileNum,HomeNum,Preferred,Email)
                                      VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""")
		self.query.addBindValue(details['FirstName'])
		self.query.addBindValue(details['LastName'])
		self.query.addBindValue(details['DateOfBirth'])
		self.query.addBindValue(details['House'])
		self.query.addBindValue(details['Road'])
		self.query.addBindValue(details['City'])
		self.query.addBindValue(details['County'])
		self.query.addBindValue(details['PostCode'])
		self.query.addBindValue(details['MobileNum'])
		self.query.addBindValue(details['HomeNum'])
		self.query.addBindValue(details['Preferred'])
		self.query.addBindValue(details['Email'])
		self.query.exec_()
		self.save_button.setEnabled(False)
		self.error_label.setText("Customer Added Succesfully")
		self.error_label.show()

	def reset_data(self):
		self.fName_lineedit.clear()
		self.lName_lineedit.clear()
		self.year_lineedit.setText("YYYY")
		self.month_lineedit.setText("MM")
		self.day_lineedit.setText("DD")
		self.number_lineedit.clear()
		self.road_lineedit.clear()
		self.city_lineedit.clear()
		self.county_lineedit.clear()
		self.postcode_lineedit.clear()
		self.mobile_lineedit.clear()
		self.home_lineedit.clear()
		self.email_lineedit.clear()
		if self.mobile_radio.isChecked():
			self.preferred_groupbox.setChecked(False)

	def customer_details(self):
		self.dateofbirth = str("{0}/{1}/{2}".format(self.year_lineedit.text(),
							    self.month_lineedit.text(),
							    self.day_lineedit.text()))
		if self.mobile_radio.isChecked():
			self.preferred = "Mobile"
		if self.home_radio.isChecked():
			self.preferred = "Home"
		details = {'FirstName':self.fName_lineedit.text(),
			   'LastName':self.lName_lineedit.text(),
			   'DateOfBirth':self.dateofbirth,
			   'House':self.number_lineedit.text(),
			   'Road':self.road_lineedit.text(),
			   'City':self.city_lineedit.text(),
			   'County':self.county_lineedit.text(),
			   'PostCode':self.postcode_lineedit.text(),
			   'MobileNum':self.mobile_lineedit.text(),
			   'HomeNum':self.home_lineedit.text(),
			   'Preferred':self.preferred,
			   'Email':self.email_lineedit.text()}
		return details

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = AddCustomer()
    window.show()
    window.raise_()
    application.exec_()
