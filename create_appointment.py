from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import webbrowser

from search_customer_widget import *

class CreateAppointment(QWidget):
    """This is what will be used to create an appointment"""

    def __init__(self):
        super().__init__()

        self.stacked_appointment_layout = QStackedLayout()
        self.setLayout(self.stacked_appointment_layout)
        self.find_customer_layout()
        self.create_appointment_layout()

    def find_customer_layout(self):
        self.search_customer_layout = SearchCustomer()
        self.stacked_appointment_layout.addWidget(self.search_customer_layout)
        #connections (signal)
        self.search_customer_layout.customerSelectedSignal.connect(self.create_appointment)

    def create_appointment_layout(self):
        
        self.title_label = QLabel("""<html>
					  <body>
					       <p><span style=" font-size:16pt; font-weight:1000;">Create Treatment</span></p>
					  </body>
				     </html>""")

        self.get_customer_details(2)
        
        self.customer_details_label = QLabel("""<html>
					  <body>
					       <p><span style=" font-size:12pt; font-weight:750;">Customer Details</span></p>
					  </body>
				     </html>""")
        self.customer_id_label = QLabel("ID: {0}".format(self.customer_id))
        self.customer_name_label = QLabel("Name: {0}".format(self.customer_name))
        self.customer_dob_label = QLabel("Date of Birth: {0}".format(self.date_of_birth))
        self.customer_address_label = QLabel("Address: {0}".format(self.customer_address))
        self.customer_mobile_label = QLabel("Contact Numbers: {0}, {1} - Preferred: {2}".format(self.mobile,self.home,self.preferred))
        self.email_label = QLabel("Email: ")
        self.email_button = QPushButton("Email Customer")
        self.email_layout = QHBoxLayout()
        self.email_layout.addWidget(self.email_label)
        self.email_layout.addWidget(self.email_button)
        self.customer_email_widget = QWidget()
        self.customer_email_widget.setLayout(self.email_layout)
        self.customer_different_button = QPushButton("Change Customer")

        self.treatment_details_label = QLabel("""<html>
					  <body>
					       <p><span style=" font-size:12pt; font-weight:750;">Treatment Details</span></p>
					  </body>
				     </html>""")
        self.treatment_label = QLabel("Treatment: ")
        self.create_treatment_model()
        self.treatment_combobox = QComboBox()
        self.treatment_combobox.setModel(self.model)
        self.treatment_combobox.setModelColumn(1)
        self.select_treatment_button = QPushButton("Select")
        
        self.date_selector = QCalendarWidget()
        self.date_selector.setEnabled(False)

        self.time_selector = QTimeEdit()
        self.time_selector.setDisplayFormat("HH:mm")
        self.time_selector.setEnabled(False)

        self.duration_label = QLabel("Duration of Treatment: ")
        self.duration_time = QLabel()

        self.duration = self.model.index(self.treatment_combobox.currentIndex(),3).data()
        self.duration_time.setText(self.customer_name)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.customer_details_label)
        self.layout.addWidget(self.customer_id_label)
        self.layout.addWidget(self.customer_name_label)
        self.layout.addWidget(self.customer_address_label)
        self.layout.addWidget(self.customer_mobile_label)
        self.layout.addWidget(self.customer_email_widget)
        self.layout.addWidget(self.customer_different_button)

        self.layout.addWidget(self.treatment_details_label)
        self.layout.addWidget(self.treatment_label)
        self.layout.addWidget(self.treatment_combobox)
        self.layout.addWidget(self.select_treatment_button)

        self.layout.addWidget(self.date_selector)
        self.layout.addWidget(self.time_selector)

        self.layout.addWidget(self.duration_label)
        self.layout.addWidget(self.duration_time)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.stacked_appointment_layout.addWidget(self.widget)
        
    def create_appointment(self):
        self.stacked_appointment_layout.setCurrentIndex(1)

        #connections
        self.customer_different_button.clicked.connect(self.search_customer)
        self.select_treatment_button.clicked.connect(self.enable_creation)
        self.email_button.clicked.connect(self.email_customer)

    def enable_creation(self):
        self.select_treatment_button.setEnabled(False)
        self.treatment_combobox.setEnabled(False)
        self.date_selector.setEnabled(True)
        self.time_selector.setEnabled(True)

    def create_treatment_model(self):
        self.model = QSqlRelationalTableModel()
        self.model.setTable("Treatment")
        self.model.select()

    def get_customer_details(self,CustomerID):
        self.query = QSqlQuery()
        self.query.prepare("""SELECT *
                              FROM Customer
                              WHERE CustomerID = ?""")
        self.query.addBindValue(CustomerID)
        self.query.exec_()
        while self.query.next():
            self.customer_id = self.query.value(0)

            self.first_name = self.query.value(1)
            self.last_name = self.query.value(2)
            self.customer_name = "{0}, {1}".format(self.last_name,self.first_name)

            self.date_of_birth = self.query.value(3)

            self.house = self.query.value(4)
            self.road = self.query.value(5)
            self.city = self.query.value(6)
            self.county = self.query.value(7)
            self.postcode = self.query.value(8)
            self.customer_address = "{0} {1}, {2}, {3}, {4}".format(self.house,
                                                           self.road,
                                                           self.city,
                                                           self.county,
                                                           self.postcode)

            self.mobile = self.query.value(9)
            self.home = self.query.value(10)
            self.preferred = self.query.value(11)

            self.email = self.query.value(12)
        
    def email_customer(self):
        webbrowser.open("mailto:{0}".format(self.email))
        
