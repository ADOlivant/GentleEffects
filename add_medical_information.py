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

    def __init__(self,connection ):
        super().__init__()

        self.connection = connection

        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)

        self.search_customer()

    def search_customer(self):
        self.search_customer_widget = SearchCustomer()
        self.stacked_layout.addWidget(self.search_customer_widget)
        self.stacked_layout.setCurrentIndex(0)

        #connections
        self.search_customer_widget.customerSelectedSignal.connect(self.medical_info_selection)

    def medical_info_selection(self):

        self.customer_details = self.search_customer_widget.get_customer_details()
        
        self.title_label = QLabel("""<html>
                                          <body>
                                               <p><span style=" font-size:16pt; font-weight:1000;">Customer Medical Infomation</span></p>
                                          </body>
                                     </html>""")
        self.add_push_button = QPushButton("Add Medical Information for {0} {1}".format(self.customer_details['FirstName'],
                                                                                        self.customer_details['LastName']))
        self.edit_push_button = QPushButton("Edit Medical Information for {0} {1}".format(self.customer_details['FirstName'],
                                                                                        self.customer_details['LastName']))

        self.selection_layout = QVBoxLayout()
        self.selection_layout.addWidget(self.title_label)
        self.selection_layout.addWidget(self.add_push_button)
        self.selection_layout.addWidget(self.edit_push_button)

        self.selection_widget = QWidget()
        self.selection_widget.setLayout(self.selection_layout)

        self.stacked_layout.addWidget(self.selection_widget)
        self.stacked_layout.setCurrentIndex(1)

        #connection 
        self.add_push_button.clicked.connect(self.add_medical_info)
        self.edit_push_button.clicked.connect(self.edit_medical_information)
        
    def add_medical_info(self):

        self.title_label = QLabel("""<html>
                                          <body>
                                               <p><span style=" font-size:16pt; font-weight:1000;">Add Medical Infomation</span></p>
                                          </body>
                                     </html>""")

        self.error_label = QLabel()
        self.error_label.hide()

        self.customer_name = QLabel()
        self.customer_name.setText("Customer Name: {0} {1}".format(self.customer_details['FirstName'],
                                                                    self.customer_details['LastName']))

        self.customer_address = QLabel()
        self.customer_address.setText("Customer Address: {0}, {1}, {2}, {3}, {4}".format(self.customer_details['House'],
                                                                                        self.customer_details['Road'],
                                                                                        self.customer_details['City'],
                                                                                        self.customer_details['County'],
                                                                                        self.customer_details['Postcode']))

        self.customer_contact = QLabel()
        self.customer_contact.setText("Contact Details: {0}, {1}, {2}".format(self.customer_details['Home'],
                                                                                self.customer_details['Mobile'],
                                                                                self.customer_details['Email']))

        self.date_time = QLabel()
        self.date_time_stamp = datetime.datetime.now()
        #For Data Save
        self.date_time_stamp_save = self.date_time_stamp.strftime("%Y-%m-%d %H:%M")
        #For Display
        self.date_time_stamp_display = self.date_time_stamp.strftime("%A, %d %B %Y %H:%M %Z")
        self.date_time.setText("Date & Time Stamp: {0}".format(self.date_time_stamp_display))

        self.medical_information_label = QLabel("Medical Information")
        self.medical_information_ledit = QPlainTextEdit()

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
        self.stacked_layout.setCurrentIndex(2)

        #connections
        self.submit_button.clicked.connect(self.save_medical_info)

    def get_medical_information(self):
        details = {'CustomerID':self.customer_details['CustomerID'],
                    'DateTimeStamp':self.date_time_stamp_save,
                    'MedicalInfoEntry':self.medical_information_ledit.toPlainText()}
        return details

    def save_medical_info(self):
        self.medical_info_details = self.get_medical_information()
        self.connection.add_medical_information(self.medical_info_details)
        self.submit_button.hide()
        self.error_label.setText('<Strong>Customers Medical Infomration Added Successfully</Strong>')
        self.error_label.show()

    def edit_medical_information(self): 
        self.title_label = QLabel("""<html>
                                          <body>
                                               <p><span style=" font-size:16pt; font-weight:1000; color:green">Search Medical Information</span></p>
                                          </body>
                                     </html>""")

        self.customer_name_label = QLabel("Customer Name: {0} {1}".format(self.customer_details['FirstName'],
                                                                            self.customer_details['LastName']))

        self.model = self.connection.find_medical_info_by_customer_id(self.customer_details['CustomerID'])

        self.medical_info = QTableView()
        self.medical_info.setSelectionBehavior(1)
        self.medical_info.setModel(self.model)
        self.medical_info.hideColumn(1)

        self.select_medical_information_button = QPushButton('Edit Seletected Medical Information')

        self.select_medical_information_widget = QWidget()
        self.select_medical_information_layout = QVBoxLayout()
        self.select_medical_information_layout.addWidget(self.title_label)
        self.select_medical_information_layout.addWidget(self.customer_name_label)
        self.select_medical_information_layout.addWidget(self.medical_info)
        self.select_medical_information_layout.addWidget(self.select_medical_information_button)
        self.select_medical_information_widget.setLayout(self.select_medical_information_layout)
        
        self.stacked_layout.addWidget(self.select_medical_information_widget)
        self.stacked_layout.setCurrentIndex(2)

        #connections 
        self.select_medical_information_button.clicked.connect(self.edit_medical_information_information)

    def edit_medical_information_information(self):
        
        self.index = self.medical_info.selectedIndexes()

        self.title_label = QLabel("""<html>
                                          <body>
                                               <p><span style=" font-size:16pt; font-weight:1000;">Edit Medical Infomation</span></p>
                                          </body>
                                     </html>""")

        self.error_label = QLabel()
        self.error_label.hide()

        self.customer_name = QLabel()
        self.customer_name.setText("Customer Name: {0} {1}".format(self.customer_details['FirstName'],
                                                                    self.customer_details['LastName']))

        self.customer_address = QLabel()
        self.customer_address.setText("Customer Address: {0}, {1}, {2}, {3}, {4}".format(self.customer_details['House'],
                                                                                        self.customer_details['Road'],
                                                                                        self.customer_details['City'],
                                                                                        self.customer_details['County'],
                                                                                        self.customer_details['Postcode']))

        self.customer_contact = QLabel()
        self.customer_contact.setText("Contact Details: {0}, {1}, {2}".format(self.customer_details['Home'],
                                                                                self.customer_details['Mobile'],
                                                                                self.customer_details['Email']))

        self.created_on = QLabel("Medical Information Created on: {0}".format(self.medical_info.model().data(self.index[1])))

        self.date_time = QLabel()
        self.date_time_stamp = datetime.datetime.now()
        #For Data Save
        self.date_time_stamp_save = self.date_time_stamp.strftime("%Y-%m-%d %H:%M")
        #For Display
        self.date_time_stamp_display = self.date_time_stamp.strftime("%A, %d %B %Y %H:%M %Z")
        self.date_time.setText("Date & Time Stamp: {0}".format(self.date_time_stamp_display))

        self.medical_information_label = QLabel("Medical Information")
        self.medical_information_ledit = QPlainTextEdit()
        self.medical_information_ledit.setPlainText(self.medical_info.model().data(self.index[2]))

        self.submit_button = QPushButton("Update Medical Information")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.error_label)
        self.layout.addWidget(self.customer_name)
        self.layout.addWidget(self.customer_address)
        self.layout.addWidget(self.customer_contact)
        self.layout.addWidget(self.created_on)
        self.layout.addWidget(self.date_time)
        self.layout.addWidget(self.medical_information_label)
        self.layout.addWidget(self.medical_information_ledit)
        self.layout.addWidget(self.submit_button)

        self.add_medical_information_widget = QWidget()
        self.add_medical_information_widget.setLayout(self.layout)

        self.stacked_layout.addWidget(self.add_medical_information_widget)
        self.stacked_layout.setCurrentIndex(3)

        #connections
        self.submit_button.clicked.connect(self.update_medical_information)

    def update_medical_information(self):
        self.medical_information_ledit_text = self.medical_information_ledit.toPlainText() + """\n   Updated on {0}""".format(self.date_time_stamp_display)
        self.medical_info.showColumn(0)
        self.index = self.medical_info.selectedIndexes()
        self.medical_info_id = self.medical_info.model().data(self.index[0])
        self.connection.amend_medical_information(self.medical_information_ledit_text,self.medical_info_id)

        self.submit_button.hide()
        self.medical_information_ledit.setPlainText(self.medical_information_ledit_text)
        self.medical_information_ledit.setReadOnly(True)
        self.error_label.setText("<Strong>Customers Medical Infomration Updated Successfully</Strong>")
        self.error_label.show()