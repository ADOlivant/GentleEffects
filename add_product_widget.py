from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import re

class AddProduct(QWidget):
	"""Adding Product data to SQL Database with PyQt4"""

	def __init__(self):
		super().__init__()

		self.title_label = QLabel("""<html>
					  <body>
					       <p><span style=" font-size:16pt; font-weight:1000;">New Product</span></p>
					  </body>
				     </html>""")

		self.name_label = QLabel("Product Name:")
		self.price_label = QLabel("Product Price:")
		self.code_label = QLabel("Product Code:")
		self.supplier_label = QLabel("Supplier:")

		self.name_lineedit = QLineEdit()
		self.price_dblspinbox = QDoubleSpinBox()
		self.price_dblspinbox.setPrefix("£")
		self.price_dblspinbox.setSingleStep(0.5)
		self.price_dblspinbox.setMaximum(500.00)
		self.code_lineedit = QLineEdit()
		self.supplier_lineeidt = QLineEdit()

		self.data_layout = QGridLayout()
		self.data_layout.addWidget(self.name_label,0,0)
		self.data_layout.addWidget(self.price_label,1,0)
		self.data_layout.addWidget(self.code_label,2,0)
		self.data_layout.addWidget(self.supplier_label,3,0)
		self.data_layout.addWidget(self.name_lineedit,0,1)
		self.data_layout.addWidget(self.price_dblspinbox,1,1)
		self.data_layout.addWidget(self.code_lineedit,2,1)
		self.data_layout.addWidget(self.supplier_lineeidt,3,1)
		self.data_widget = QWidget()
		self.data_widget.setLayout(self.data_layout)

		self.save_pushbutton = QPushButton("Add Product")
		self.rest_pushbutton = QPushButton("Reset")

		self.button_layout = QHBoxLayout()
		self.button_layout.addWidget(self.save_pushbutton)
		self.button_layout.addWidget(self.rest_pushbutton)
		self.button_widget = QWidget()
		self.button_widget.setLayout(self.button_layout)

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.title_label)
		self.layout.addWidget(self.data_widget)
		self.layout.addWidget(self.button_widget)

		self.setLayout(self.layout)

		#connections
		self.save_pushbutton.clicked.connect(self.save_product)
		self.rest_pushbutton.clicked.connect(self.reset_product)

	def save_product(self):
		details = self.product_details()
		self.query = QSqlQuery()
		self.query.prepare("""INSERT INTO Product(Name,Price,Code,SupplierID)
				      VALUES (?,?,?,?)""")
		self.query.addBindValue(details['Name'])
		self.query.addBindValue(details['Price'])
		self.query.addBindValue(details['Code'])
		self.query.addBindValue(details['SupplierID'])
		self.query.exec_()
		self.save_pushbutton.setEnabled(False)

	def reset_product(self):
		self.name_lineedit.clear()

	def product_details(self):
		details = {'Name':self.name_lineedit.text(),
			   'Price':self.price_dblspinbox.value(),
			   'Code':self.code_lineedit.text(),
			   'SupplierID':self.supplier_lineeidt.text()}
		return details
