from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import webbrowser

#Confirmation Email Imports
from send_email import *

from search_customer_widget import *
from SQL import *

class CreateAppointment(QWidget):
    """This is what will be used to create an appointment"""

    def __init__(self, connection):
        super().__init__()

        self.connection = connection

        self.stacked_appointment_layout = QStackedLayout()
        self.setLayout(self.stacked_appointment_layout)
        self.find_layout()

    def find_layout(self):
        self.search_customer_layout = SearchCustomer()
        self.stacked_appointment_layout.addWidget(self.search_customer_layout)
        self.stacked_appointment_layout.setCurrentIndex(0)
        
        #connections (signal)
        self.search_customer_layout.customerSelectedSignal.connect(self.create_appointment)

    def create_appointment_layout(self):
        
        #TITLE FOR LAYOUT
        self.title_label = QLabel("""<html>
					  <body>
					       <p><span style=" font-size:16pt; font-weight:1000; color:Green">New Appointment</span></p>
					  </body>
				     </html>""")
        self.book_appointment_button = QPushButton("Book Appointment")
        self.book_appointment_button.hide()

        self.error_message = QLabel()
        self.error_message.hide()

        self.get_customer_details()
        
        #CUSTOMER DETAILS LAYOUT
        self.customer_details_label = QLabel("""<html>
					  <body>
					       <p><span style=" font-size:12pt; font-weight:750;">Customer Details</span></p>
					  </body>
				     </html>""")
        self.customer_id_label = QLabel("ID: {0}".format(self.customer_id))
        self.customer_name_label = QLabel("Name: {0}".format(self.customer_name))
        self.customer_dob_label = QLabel("Date of Birth: {0}".format(self.date_of_birth))
        self.customer_address_label = QLabel("Address: {0}".format(self.customer_address))
        self.customer_contact_label = QLabel("Contact Numbers: {0}, {1} - Preferred: {2}".format(self.mobile,self.home,self.preferred))
        self.customer_email_label = QLabel("Email: {0}".format(self.email))
        self.customer_email_button = QPushButton("Email Customer")

        self.customer_details_layout = QGridLayout()
        self.customer_details_layout.addWidget(self.customer_details_label,0,0,1,2)
        self.customer_details_layout.addWidget(self.customer_name_label,1,0)
        self.customer_details_layout.addWidget(self.customer_id_label,1,1)
        self.customer_details_layout.addWidget(self.customer_dob_label,2,0,1,2)
        self.customer_details_layout.addWidget(self.customer_address_label,3,0,1,2)
        self.customer_details_layout.addWidget(self.customer_contact_label,4,0,1,2)
        self.customer_details_layout.addWidget(self.customer_email_label,5,0)
        self.customer_details_layout.addWidget(self.customer_email_button,5,1)

        self.customer_details_widget = QWidget()
        self.customer_details_widget.setLayout(self.customer_details_layout)
        
        
        #TREATMENT DETAILS LAYOUT
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
        self.treatment_text = QLabel()
        self.select_treatment_button = QPushButton("Select")
        self.select_another_button = QPushButton("Select Another")
        self.select_another_button.hide()
        self.treatment_text.hide()

        self.treatment_selection_layout = QVBoxLayout()
        self.treatment_selection_layout.addWidget(self.treatment_combobox)
        self.treatment_selection_layout.addWidget(self.treatment_text)
        self.treatment_selection_widget = QWidget()
        self.treatment_selection_widget.setLayout(self.treatment_selection_layout)

        self.treatment_cost_label = QLabel("Cost: ")
        self.treatment_cost_details = QLabel()
        self.treatment_duration_label = QLabel("Duration: ")
        self.treatment_duration_details = QLabel()
        self.treatment_cost_label.hide()
        self.treatment_cost_details.hide()
        self.treatment_duration_label.hide()
        self.treatment_duration_details.hide()

        self.treatment_details_layout = QGridLayout()
        self.treatment_details_layout.addWidget(self.treatment_details_label,0,0,1,2)
        self.treatment_details_layout.addWidget(self.treatment_label,1,0)
        self.treatment_details_layout.addWidget(self.treatment_selection_widget,1,1)
        self.treatment_details_layout.addWidget(self.select_treatment_button,2,0,1,2)
        self.treatment_details_layout.addWidget(self.treatment_cost_label,3,0)
        self.treatment_details_layout.addWidget(self.treatment_cost_details,3,1)
        self.treatment_details_layout.addWidget(self.treatment_duration_label,4,0)
        self.treatment_details_layout.addWidget(self.treatment_duration_details,4,1)
        self.treatment_details_layout.addWidget(self.select_another_button,5,0,1,2)

        self.treatment_details_widget = QWidget()
        self.treatment_details_widget.setLayout(self.treatment_details_layout)
        
        #TREATMENT BOOKING DETAILS
        self.treatment_booking_label = QLabel("""<html>
					  <body>
					       <p><span style=" font-size:12pt; font-weight:750;">Date & Time of Appointment</span></p>
					  </body>
				     </html>""")

        self.date_selector = QCalendarWidget()
        self.time_selector = QTimeEdit()
        self.time_selector.setDisplayFormat("HH:mm")

        self.treatment_booking_layout = QVBoxLayout()
        self.treatment_booking_layout.addWidget(self.treatment_booking_label)
        self.treatment_booking_layout.addWidget(self.date_selector)
        self.treatment_booking_layout.addWidget(self.time_selector)
        self.treatment_booking_widget = QWidget()
        self.treatment_booking_widget.setLayout(self.treatment_booking_layout)
        self.treatment_booking_widget.hide()

        #OVERALL LAYOUT
        self.layout = QGridLayout()
        self.layout.addWidget(self.title_label,0,0,1,2)
        self.layout.addWidget(self.error_message,1,0,1,2)
        self.layout.addWidget(self.customer_details_widget,2,0)
        self.layout.addWidget(self.treatment_details_widget,2,1)
        self.layout.addWidget(self.treatment_booking_widget,3,0,1,2)
        self.layout.addWidget(self.book_appointment_button,4,0,1,2)
        
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.stacked_appointment_layout.addWidget(self.widget)

        #connections
        self.select_treatment_button.clicked.connect(self.enable_creation)
        self.customer_email_button.clicked.connect(self.email_customer)
        self.book_appointment_button.clicked.connect(self.validate_treatment_datetime)
        self.select_another_button.clicked.connect(self.disable_datetime)
        
    def validate_treatment_datetime(self):
        self.data_valid = None
        self.details = self.appointment_details()
        self.validate_treatment_datetime = QSqlQuery()
        self.validate_treatment_datetime.prepare("""SELECT TreatmentID
                                           FROM Appointment
                                           WHERE AppointmentTime = (?) AND AppointmentDate = (?)""")
        self.validate_treatment_datetime.addBindValue(self.details['Time'])
        self.validate_treatment_datetime.addBindValue(self.details['Date'])
        self.validate_treatment_datetime.exec_()
        self.validate_list = []
        while self.validate_treatment_datetime.next():
            self.validate_list.append(self.validate_treatment_datetime.value(0))
        if len(self.validate_list) == 0:
            pass 
        else:
            self.data_valid = False
        if self.data_valid == False:
            self.error_message.setText("Appointment time has previously been taken.")
            self.error_message.show()
        else:
            self.book_appointment()

    def get_treatment_duration_SQL(self,treatmentID):
        self.get_treatment_duration_SQL = QSqlQuery()
        self.get_treatment_duration_SQL.prepare("""SELECT Duration
                                           FROM Treatment
                                           WHERE TreatmentID = (?)""")
        self.get_treatment_duration_SQL.addBindValue(treatmentID)
        self.get_treatment_duration_SQL.exec_()
        while self.get_treatment_duration_SQL.next():
            self.treatment_duration = self.get_treatment_duration_SQL.value(0)
        return self.treatment_duration

    def create_appointment(self):
        self.create_appointment_layout()
        self.stacked_appointment_layout.setCurrentIndex(1)

    def enable_creation(self):
        self.select_treatment_button.hide()
        self.select_another_button.show()
        self.treatment_combobox.hide()
        self.treatment_text.setText(self.model.index(self.treatment_combobox.currentIndex(),1).data())
        self.treatment_text.show()
        self.treatment_duration_label.show()
        self.treatment_duration_details.setText(self.model.index(self.treatment_combobox.currentIndex(),3).data())
        self.treatment_duration_details.show()
        self.treatment_cost_label.show()
        self.treatment_cost_text = "£ {0}".format(self.model.index(self.treatment_combobox.currentIndex(),2).data())
        self.treatment_cost_details.setText(self.treatment_cost_text)
        self.treatment_cost_details.show()
        self.treatment_booking_widget.show()
        self.book_appointment_button.show()

    def disable_datetime(self):
        self.select_treatment_button.show()
        self.select_another_button.hide()
        self.treatment_combobox.show()
        self.treatment_text.hide()
        self.treatment_duration_label.hide()
        self.treatment_duration_details.hide()
        self.treatment_cost_label.hide()
        self.treatment_cost_details.hide()
        self.treatment_booking_widget.hide()
        self.book_appointment_button.hide()

    def create_treatment_model(self):
        self.model = QSqlRelationalTableModel()
        self.model.setTable("Treatment")
        self.model.select()

    def get_customer_details(self):
        self.customer_id = self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[0])

        self.first_name = self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[1])
        self.last_name = self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[2])
        self.customer_name = "{0}, {1}".format(self.last_name,self.first_name)

        self.date_of_birth = self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[3])

        self.house = self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[4])
        self.road = self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[5])
        self.city = self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[6])
        self.county = self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[7])
        self.postcode = self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[8])
        self.customer_address = "{0} {1}, {2}, {3}, {4}".format(self.house,
                                                       self.road,
                                                       self.city,
                                                       self.county,
                                                       self.postcode)

        self.mobile = self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[9])
        self.home = self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[10])
        self.preferred = self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[11])

        self.email = self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[12])
        
    def email_customer(self):
        webbrowser.open("mailto:{0}".format(self.email))

    def book_appointment(self):
        self.booked_appointment()
        self.save_appointment()
        if self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[12]) != "":
            self.app_id = self.get_appointment_id()
            self.email_booking()

    def save_appointment(self):
        self.details = self.appointment_details()
        self.save_to_database = QSqlQuery()
        self.save_to_database.prepare("""INSERT INTO Appointment(AppointmentTime,AppointmentDate,CustomerID,TreatmentID)
                                         VALUES (?,?,?,?)""")
        self.save_to_database.addBindValue(self.details['Time'])
        self.save_to_database.addBindValue(self.details['Date'])
        self.save_to_database.addBindValue(self.details['CustomerID'])
        self.save_to_database.addBindValue(self.details['TreatmentID'])
        self.save_to_database.exec_()     

    def get_appointment_id(self):
        self.details = self.appointment_details()
        self.get_appointment_id = QSqlQuery()
        self.get_appointment_id.prepare("""SELECT AppointmentID
                                           FROM Appointment
                                           WHERE AppointmentTime = (?) AND AppointmentDate = (?) AND CustomerID = (?) AND TreatmentID = (?)""")
        self.get_appointment_id.addBindValue(self.details['Time'])
        self.get_appointment_id.addBindValue(self.details['Date'])
        self.get_appointment_id.addBindValue(self.details['CustomerID'])
        self.get_appointment_id.addBindValue(self.details['TreatmentID'])
        self.get_appointment_id.exec_()
        
        while self.get_appointment_id.next():
            app = self.get_appointment_id.value(0)
        return app

    def appointment_details(self):
        details = {'CustomerID':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[0]),
                   'TreatmentID':self.model.index(self.treatment_combobox.currentIndex(),0).data(),
                   'Date':self.date_selector.selectedDate().toString(Qt.ISODate),
                   'Time':self.time_selector.time().toString(Qt.ISODate)}
        return details

    def booked_appointment(self):
        self.booked_appointment_layout = QLabel("""<html>
					                 <body>
					                       <p><span style=" font-size:16pt; font-weight:1000; color:Green">Appointment Booked</span></p>
					                 </body>
				                   </html>""")

        if self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[12]) != "":
            self.email_text = " and email sent to the client"
        else:
            self.email_text = ""
            
        self.booked_confirmation_label = QLabel("This appointment has been booked{0}.".format(self.email_text))

        self.booked_customer_name_label = QLabel("Customer Name: ")
        self.booked_customer_name_detail = QLabel()
        self.booked_customer_name = ("{0} {1}".format(self.first_name,self.last_name))
        self.booked_customer_name_detail.setText(self.booked_customer_name)
        self.booked_customer_address_label = QLabel("Customer Address: ")
        self.booked_customer_address_detail = QLabel()
        self.booked_customer_address = "{0}, {1} \n {2} \n {3} \n {4}".format(self.house,
                                                       self.road,
                                                       self.city,
                                                       self.county,
                                                       self.postcode)
        self.booked_customer_address_detail.setText(self.booked_customer_address)

        self.booked_appointment_name_label = QLabel("Treatment: ")
        self.booked_appointment_name_detail = QLabel()
        self.booked_appointment_name_detail.setText(self.model.index(self.treatment_combobox.currentIndex(),1).data())
        self.booked_appointment_cost_label = QLabel("Treatment Cost: ")
        self.booked_appointment_cost_detail = QLabel()
        self.booked_appointment_cost_detail.setText(self.treatment_cost_text)

        self.booked_appointment_date_label = QLabel("Treatment Date: ")
        self.booked_appointment_date_detail = QLabel(self.date_selector.selectedDate().toString(Qt.TextDate))
        self.booked_appointment_time_label = QLabel("Treatment Time: ")
        self.booked_appointment_time_detail = QLabel(self.time_selector.time().toString(Qt.TextDate))

        self.booked_layout = QGridLayout()
        self.booked_layout.addWidget(self.booked_appointment_layout,0,0,1,2)
        self.booked_layout.addWidget(self.booked_confirmation_label,1,0,1,2)
        self.booked_layout.addWidget(self.booked_customer_name_label,2,0)
        self.booked_layout.addWidget(self.booked_customer_name_detail,2,1)
        self.booked_layout.addWidget(self.booked_customer_address_label,3,0)
        self.booked_layout.addWidget(self.booked_customer_address_detail,3,1)
        self.booked_layout.addWidget(self.booked_appointment_name_label,4,0)
        self.booked_layout.addWidget(self.booked_appointment_name_detail,4,1)
        self.booked_layout.addWidget(self.booked_appointment_cost_label,5,0)
        self.booked_layout.addWidget(self.booked_appointment_cost_detail,5,1)
        self.booked_layout.addWidget(self.booked_appointment_date_label,6,0)
        self.booked_layout.addWidget(self.booked_appointment_date_detail,6,1)
        self.booked_layout.addWidget(self.booked_appointment_time_label,7,0)
        self.booked_layout.addWidget(self.booked_appointment_time_detail,7,1)
        self.booked_widget = QWidget()
        self.booked_widget.setLayout(self.booked_layout)

        self.stacked_appointment_layout.addWidget(self.booked_widget)
        self.stacked_appointment_layout.setCurrentIndex(2)

    def email_booking(self):
        self.to = "{0}, ".format(self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[12]))
        self.subject = "You booking for {0}".format(self.model.index(self.treatment_combobox.currentIndex(),1).data())
        self.body = "Hi {2}, \n \n Your {3} appointment with Gentle Effects is booked for {4} at {5}. I look forward to seeing you then. \n \n Please have these handy when calling - Personal ID: {0}, Appointment ID: {1} \n  \n Kind Regards, \n Paula Lawrence \n Aestetic Nurse Practioner \n \n".format(self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[0]),
                                                                                                                                                                                                                                                                                                     self.app_id,
                                                                                                                                                                                                                                                                                                     self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[1]),
                                                                                                                                                                                                                                                                                                     self.model.index(self.treatment_combobox.currentIndex(),1).data(),
                                                                                                                                                                                                                                                                                                     self.date_selector.selectedDate().toString(Qt.TextDate),
                                                                                                                                                                                                                                                                                                     self.time_selector.time().toString(Qt.TextDate))
        send_email(self.to,self.subject,self.body)





        
