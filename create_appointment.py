from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class CreateAppointment(QWidget):
    """This is what will be used to create an appointment"""

    def __init__(self):
        super().__init__()

        self.customerID = int(1)
        self.get_customer_details(self.customerID)
        
        self.title_label = QLabel("""<html>
					  <body>
					       <p><span style=" font-size:16pt; font-weight:1000;">Create Treatment</span></p>
					  </body>
				     </html>""")

        self.date_selector = QCalendarWidget()

        self.time_selector = QTimeEdit()
        self.time_selector.setDisplayFormat("HH:mm")
        self.treatment_label = QLabel("Treatment: ")
        self.create_treatment_model()
        self.treatment_combobox = QComboBox()
        self.treatment_combobox.setModel(self.model)
        self.treatment_combobox.setModelColumn(1)

        self.duration_label = QLabel("Duration of Treatment: ")
        self.duration_time = QLabel()

        self.duration = self.model.index(self.treatment_combobox.currentIndex(),3).data()
        self.duration_time.setText(self.duration)

        self.layout = QGridLayout()
        self.layout.addWidget(self.title_label,0,0,1,3)
        self.layout.addWidget(self.date_selector,1,0)
        self.layout.addWidget(self.time_selector,2,0)
        self.layout.addWidget(self.treatment_label,1,1)
        self.layout.addWidget(self.treatment_combobox,1,2)
        self.layout.addWidget(self.duration_label,2,1)
        self.layout.addWidget(self.duration_time,2,2)

        self.setLayout(self.layout)

    def create_treatment_model(self):
        self.model = QSqlRelationalTableModel()
        self.model.setTable("Treatment")
        self.model.select()

    def get_customer_details(self,CustomerID):
        self.query = QSqlQuery()
        self.query.prepare("""SELECT FirstName, LastName
                              FROM Customer
                              WHERE CustomerID = ?""")
        self.query.addBindValue(CustomerID)
        self.query.exec_()
        #Attribute Error - QSqlQuery object has no attribute select - check PyQt Docs.
        self.customer_details = self.query.select()
        print(self.customer_details)
        return self.customer_details 
        
        
