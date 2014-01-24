from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import re

class SearchAppointment(QWidget):

    #Appointment Found Signal to fire when Appointmnet Selected
    appointmentSelectedWidget = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.find_appointment_layout()
        #self.find_appointment_layout()

        #connections
        self.radio_button_group.buttonClicked.connect(self.change_search_type)
        self.find_appointment_button.clicked.connect(self.find_appointment)

    def find_appointment_layout(self):
        self.title_label = QLabel("""<html>
                                          <body>
                                               <p><span style=" font-size:16pt; font-weight:1000;">Search Appointments</span></p>
                                          </body>
                                     </html>""")

        self.appointment_id_label = QLabel("Appointment ID:")
        self.appointment_date_label = QLabel("Appointment Date:")
        self.appointmnet_time_label = QLabel("Appoitment Time:")
        self.customer_id_label = QLabel("Customer ID:")
        self.customer_first_name_label = QLabel("Customer First Name:")
        self.customer_last_name_label = QLabel("Customer Last Name:")
        self.customer_number_label = QLabel("Customer House No or Name:")
        self.customer_postcode_label = QLabel("Customer Postcode")
        self.appointment_treatment = QLabel("Appointment Treatment")

        self.appointment_id_ledit = QLineEdit()
        self.appointment_date_selector = QCalendarWidget()
        
        
        
        

    def change_search_type(self):
        pass

    def find_appointment(self):
        pass
