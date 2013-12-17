from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import re

class AddCustomer(QWidget):
	"""Adding Customer data to SQL Database with PyQt4"""

	def __init__(self):
		super().__init__()

		self.title_label = QLabel("""<html>
					  <body>
					       <p><span style=" font-size:16pt; font-weight:1000;">Search Customer</span></p>
					  </body>
				     </html>""")

		self.customer_id_label = QLabel("Customer ID:")
		self.customer_fName = QLabel("First Name:")
		self.customer_lName = QLabel("Last Name:")
		self.customer_number = QLabel("House No or Name:")
		self.customer_postcode = QLabel("Postcode")

		self.customer_id_ledit = QLineEdit()
		self.customer_fName_ledit = QLineEdit()
		self.customer_fName_ledit.setEnabled(False)
		self.customer_lName_ledit = QLineEdit()
		self.customer_lName_ledit.setEnabled(False)
		self.customer_number_ledit = QLineEdit()
		self.customer_number_ledit.setEnabled(False)
		self.customer_postcode_ledit = QLineEdit()
		self.customer_postcode_ledit.setEnabled(False)

		self.find_customer_button = QPushButton("Find Customer")

		self.radio_button_box = QGroupBox()
                self.radio_button_group = QButtonGroup()

                self.id_radio = QRadioButton()
                self.postcode_radio = QRadioButton()
                self.name_radio = QRadioButton()

                self.id_radio.setChecked(True)

                self.radio_button_group.addButton(self.number_radio)
                self.radio_button_group.setID(self.number_radio,0)
                self.radio_button_group.addButton(self.name_radio)
                self.radio_button_group.setID(self.name_radio,1)
                self.radio_button_group.addButton(self.postcode_radio)
                self.radio_button_group.setID(self.postcode_radio,2)

                self.customer_id_layout = QGridLayout()
                self.customer_id_layout.addWidget(self.customer_id_label,0,0)
                self.customer_id_layout.addWidget(self.customer_id_ledit,0,1)

                self.customer_name_layout = QGridLayout()
                self.customer_name_layout.addWidget(self.customer_fName_label,0,0)
                self.customer_name_layout.addWidget(self.customer_fName_ledit,0,1)
                self.customer_name_layout.addWidget(self.customer_lName_ledit,1,0)
                self.customer_name_layout.addWidget(self.customer_lName_ledit,1,1)

		#connections
