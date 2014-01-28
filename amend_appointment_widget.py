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
        
    
        
        

        
