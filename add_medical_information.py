from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import re
import datetime

from search_customer_widget import *

class AddMedicalInfo(QWidget):
    """Adding medical information into a customers record."""

    #MedicalInfo Signal to fire when details are added.
    medicalInfoAddedSignal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)

        self.search_customer()

    def search_customer(self):
        self.search_customer_widget = SearchCustomer()
        self.stacked_layout.addWidget(self.search_customer_widget)
        self.stacked_layout.setCurrentIndex(0)

        #connections
        self.search_customer_widget.customerSelectedSignal.connect(self.add_medical_info)

    def add_medical_info(self):

        self.title_label = QLabel("""<html>
                                          <body>
                                               <p><span style=" font-size:16pt; font-weight:1000;">Add Medical Infomation</span></p>
                                          </body>
                                     </html>""")

        self.error_label = QLabel()
        self.error_label.hide()

        self.customer_name = QLabel()
        self.customer_name.setText("Customer Name: {0} {1}".format("Test","Test"))

        self.customer_address = QLabel()
        self.customer_address.setText("Customer Address: {0} {1}, {2}, {3}".format("Test","Test","Test","Test"))

        self.customer_contact = QLabel()
        self.customer_contact.setText("Contact Details: {0}, {1}, {2}".format("Test","Test","Test"))

        self.date_time = QLabel()
        self.date_time_stamp = datetime.datetime.now()
        #For Data Save
        self.date_time_stamp_save = self.date_time_stamp.strftime("%Y-%m-%d %H:%M")
        #For Display
        self.date_time_stamp_display = self.date_time_stamp.strftime("%Y-%m-%d %H:%M")
        self.date_time.setText("Date & Time Stamp: {0}".format(self.date_time_stamp_display))

        self.medical_information_label = QLabel("Medical Information")
        self.medical_information_ledit = QLineEdit()

        self.submit_button = QPushButton("Submit Medical Information")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.error_label)
        self.layout.addWidget(self.customer_name)
        self.layout.addWidget(self.customer_address)
        self.layout.addWidget(self.customer_contact)
        self.layout.addWidget(self.date_time)
        self.layout.addWidget(self.medical_information_label)
        self.layout.addWidget(self.medical_information_ledit)
        self.layout.addWidget(self.submit_button)

        self.add_medical_information_widget = QWidget()
        self.add_medical_information_widget.setLayout(self.layout)

        self.stacked_layout.addWidget(self.add_medical_information_widget)
        self.stacked_layout.setCurrentIndex(1)
        
        
