from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

from create_appointment import *
from search_appointment_widget import *

class AmendAppointment(CreateAppointment):
    """DOC STRING"""

    def __init__(self,connection):
        super().__init__(connection)

    def find_layout(self):
        self.search_appointment_layout = SearchAppointment(self.connection)
        self.stacked_appointment_layout.addWidget(self.search_appointment_layout)
        self.stacked_appointment_layout.setCurrentIndex(0)

        #connections
        self.search_appointment_layout.appointmentSelectedSignal.connect(self.create_appointment)

    def get_customer_details(self):

        self.customer_id = 5
        self.customer_details = self.connection.customer_details_from_customer_id(self.customer_id)
        
        self.customer_id = self.customer_details['CustomerID']

        self.first_name = self.customer_details['FirstName']
        self.last_name = self.customer_details['LastName']
        self.customer_name = "{0}, {1}".format(self.last_name,self.first_name)

        self.date_of_birth = self.customer_details['DateOfBirth']

        self.house = self.customer_details['House']
        self.road = self.customer_details['Road']
        self.city = self.customer_details['City']
        self.county = self.customer_details['County']
        self.postcode = self.customer_details['PostCode']
        self.customer_address = "{0} {1}, {2}, {3}, {4}".format(self.house,
                                                       self.road,
                                                       self.city,
                                                       self.county,
                                                       self.postcode)

        self.mobile = self.customer_details['MobileNum']
        self.home = self.customer_details['HomeNum']
        self.preferred = self.customer_details['Preferred']

        self.email = self.customer_details['Email']
        
    
        
        

        
