from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import re

class AddCustomer(QWidget):
        """Adding Customer data to SQL Database with PyQt4"""

        #Customer Signal to fire when Details are Added.
        customerAddedSignal = pyqtSignal()

        def __init__(self):
                super().__init__()

                self.title_label = QLabel("""<html>
                                          <body>
                                                   <p><span style=" font-size:16pt; font-weight:1000;">New Customer</span></p>
                                          </body>
                                         </html>""")

                self.fName_label = QLabel("First Name(s)")
                self.lName_label = QLabel("Last Name(s)")
                self.dateofbirth_label = QLabel("Date of Birth")
                self.number_label = QLabel("House Name / Number")
                self.road_label = QLabel("Road")
                self.city_label = QLabel("Town / City")
                self.county_label = QLabel("County")
                self.postcode_label = QLabel("Postcode")
                self.mobile_label = QLabel("Mobile Number")
                self.home_label = QLabel("Home Number")
                self.email_label = QLabel("Email")
                
                #Preferred Contact
                self.preferred_groupbox = QGroupBox("Preferred Contact")
                self.mobile_radio = QRadioButton("Mobile")
                self.home_radio = QRadioButton("Home")
                self.preferred_layout = QVBoxLayout()
                self.preferred_layout.addWidget(self.mobile_radio)
                self.preferred_layout.addWidget(self.home_radio)
                self.preferred_groupbox.setLayout(self.preferred_layout)

                self.fName_lineedit = QLineEdit()
                self.lName_lineedit = QLineEdit()
                self.number_lineedit = QLineEdit()
                self.road_lineedit = QLineEdit()
                self.city_lineedit = QLineEdit()
                self.county_lineedit = QLineEdit()
                self.postcode_lineedit = QLineEdit()
                self.mobile_lineedit = QLineEdit()
                self.home_lineedit = QLineEdit()
                self.email_lineedit = QLineEdit()

                self.date_lineedit = QDateEdit()

                self.save_button = QPushButton("Save New Customer")
                self.reset_button = QPushButton("Reset")

                self.error_label = QLabel("Errors to Appear Here")

                self.name_layout = QGridLayout()
                self.name_layout.addWidget(self.fName_label,0,0)
                self.name_layout.addWidget(self.fName_lineedit,0,1)
                self.name_layout.addWidget(self.lName_label,1,0)
                self.name_layout.addWidget(self.lName_lineedit,1,1)
                self.name_layout.addWidget(self.dateofbirth_label,2,0)
                self.name_layout.addWidget(self.date_lineedit,2,1)
                self.name_widget = QWidget()
                self.name_widget.setLayout(self.name_layout)

                self.address_layout = QGridLayout()
                self.address_layout.addWidget(self.number_label,0,0)
                self.address_layout.addWidget(self.number_lineedit,0,1)
                self.address_layout.addWidget(self.road_label,1,0)
                self.address_layout.addWidget(self.road_lineedit,1,1)
                self.address_layout.addWidget(self.city_label,2,0)
                self.address_layout.addWidget(self.city_lineedit,2,1)
                self.address_layout.addWidget(self.county_label,3,0)
                self.address_layout.addWidget(self.county_lineedit,3,1)
                self.address_layout.addWidget(self.postcode_label,4,0)
                self.address_layout.addWidget(self.postcode_lineedit,4,1)
                self.address_widget = QWidget()
                self.address_widget.setLayout(self.address_layout)

                self.personaldetails_layout = QVBoxLayout()
                self.personaldetails_layout.addWidget(self.name_widget)
                self.personaldetails_layout.addWidget(self.address_widget)
                self.personaldetails_widget = QWidget()
                self.personaldetails_widget.setLayout(self.personaldetails_layout)

                self.contactnumbers_layout = QGridLayout()
                self.contactnumbers_layout.addWidget(self.mobile_label,0,0)
                self.contactnumbers_layout.addWidget(self.mobile_lineedit,0,1)
                self.contactnumbers_layout.addWidget(self.home_label,1,0)
                self.contactnumbers_layout.addWidget(self.home_lineedit,1,1)
                self.contactnumbers_widget = QWidget()
                self.contactnumbers_widget.setLayout(self.contactnumbers_layout)

                self.email_layout = QHBoxLayout()
                self.email_layout.addWidget(self.email_label)
                self.email_layout.addWidget(self.email_lineedit)
                self.email_widget = QWidget()
                self.email_widget.setLayout(self.email_layout)

                self.contact_layout = QVBoxLayout()
                self.contact_layout.addWidget(self.contactnumbers_widget)
                self.contact_layout.addWidget(self.preferred_groupbox)
                self.contact_layout.addWidget(self.email_widget)
                self.contact_widget = QWidget()
                self.contact_widget.setLayout(self.contact_layout)

                self.button_layout = QHBoxLayout()
                self.button_layout.addWidget(self.save_button)
                self.button_layout.addWidget(self.reset_button)
                self.button_widget = QWidget()
                self.button_widget.setLayout(self.button_layout)

                self.data_layout = QGridLayout()
                self.data_layout.addWidget(self.personaldetails_widget,0,0)
                self.data_layout.addWidget(self.contact_widget,0,1)
                self.data_widget = QWidget()
                self.data_widget.setLayout(self.data_layout)

                self.main_layout = QVBoxLayout()
                self.main_layout.addWidget(self.title_label)
                self.main_layout.addWidget(self.error_label)
                self.main_layout.addWidget(self.data_widget)
                self.main_layout.addWidget(self.button_widget)
                #self.main_widget = QWidget()
                self.setLayout(self.main_layout)

                self.error_label.hide()

                #connections
                self.reset_button.clicked.connect(self.reset_data)
                self.save_button.clicked.connect(self.validate_data)

        def validate_data(self):
                self.error_text = ""
                if len(self.fName_lineedit.text()) == 0:
                        self.error_text += "\n Please ensure that the First Name field is not empty."
                if len(self.lName_lineedit.text()) == 0:
                        self.error_text += "\n Please ensure that the Last Name field is not empty."
                self.error_label.setText(self.error_text)
                if self.error_text == "":
                        self.save_data()
                else:
                        self.error_label.show()


        def save_data(self):
                self.customerAddedSignal.emit()
                self.save_button.setEnabled(False)
                self.error_label.setText("Customer Added Succesfully")
                self.error_label.show()

        def reset_data(self):
                self.fName_lineedit.clear()
                self.lName_lineedit.clear()
                self.date_lineedit.clear()
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
                prefered = False
                if self.mobile_radio.isChecked():
                        self.preferred = "Mobile"
                        prefered = True
                if self.home_radio.isChecked():
                        self.preferred = "Home"
                        prefered = True
                if not prefered:
                        self.preferred = "Neither"
                details = {'FirstName':self.fName_lineedit.text(),
                           'LastName':self.lName_lineedit.text(),
                           'DateOfBirth':self.date_lineedit.date().toString(Qt.ISODate),
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
