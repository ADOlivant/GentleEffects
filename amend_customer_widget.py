from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import re

from add_customer_widget import * 

class EditCustomer(QWidget):
	"""docstring for EditCustomer"""

	def __init__(self):
		super().__init__()

		self.edit_customer_widget = AddCustomer() 

		self.edit_customer_widget.title_label.setText("""<html>
                                          <body>
                                                   <p><span style=" font-size:16pt; font-weight:1000;">Edit Customer</span></p>
                                          </body>
                                         </html>""")
		self.edit_customer_widget.rest_button.hide()
		self.edit_customer_widget.save_button.setText("Amend Customer Details")
