from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import re

class SearchAppointment(QWidget):

    #Appointment Found Signal to fire when Appointmnet Selected
    appointmentSelectedWidget = pyqtSignal()

    def __init__(self, connection ):
        super().__init__()

        self.connection = connection 

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
        self.appointment_treatment_label = QLabel("Appointment Treatment")

        self.appointment_id_ledit = QLineEdit()

        self.appointmnet_id_layout = QHBoxLayout()
        self.appointmnet_id_layout.addWidget(self.appointment_id_label)
        self.appointmnet_id_layout.addWidget(self.appointment_id_ledit)
        
        self.appointment_date_selector = QCalendarWidget()
        self.appointment_date_selector.hide()
        self.appointment_time_selector = QTimeEdit()
        self.appointment_time_selector.setDisplayFormat("HH:mm")
        self.appointment_time_selector.setEnabled(False)

        self.appointment_details_layout = QGridLayout()
        self.appointment_details_layout.addWidget(self.appointment_date_label,0,0)
        self.appointment_details_layout.addWidget(self.appointment_date_selector,0,1)
        self.appointment_details_layout.addWidget(self.appointment_time_label,1,0)
        self.appointment_details_layout.addWidget(self.appointment_time_selector,1,1)
        
        self.customer_id_ledit = QLineEdit()
        self.customer_id_ledit.setEnabled(False)

        self.customer_id_layout = QHBoxLayout()
        self.cusotmer_id_layout.addWidget(self.customer_id_label)
        self.customer_id_layout.addWidget(self.customer_id_ledit)
        
        self.customer_first_name_ledit = QLineEdit()
        self.customer_first_name_ledit.setEnabled(False)
        self.customer_last_name_ledit = QLineEdit()
        self.customer_last_name_ledit.setEnabled(False)

        self.customer_name_layout = QGridLayout()
        self.customer_name_layout.addWidget(self.customer_first_name_label,0,0)
        self.customer_name_layout.addWidget(self.customer_first_name_ledit,0,1)
        self.customer_name_layout.addWidget(self.customer_last_name_label,1,0)
        self.customer_name_layout.addWidget(self.customer_last_name_ledit,1,1)
        
        self.customer_number_ledit = QLineEdit()
        self.customer_number_ledit.setEnabled(False)
        self.customer_postcode_ledit = QLineEdit()
        self.customer_postcode_ledit.setEnabled(False)

        self.customer_address_layout = QGridLayout()
        self.customer_address_layout.addWidget(self.customer_number_label,0,0)
        self.customer_address_layout.addWidget(self.customer_number_ledit,0,1)
        self.customer_address_layout.addWidget(self.customer_postcode_label,1,0)
        self.customer_address_layout.addWidget(self.customer_postcode_ledit,1,1)
        
        self.appointment_treatmet_combobox = QComboBox()
        self.appointmnet_treatment_model = self.connection.create_treatment_combobox_model()
        self.appointment_treatment.setModel(self.appointment_treatment_model)
        self.appointment_treatment.setModelColumn(1)
        self.appointmnet_treatment.setEnabled(False)

        self.appointment_treatment_layout = QHBoxLayout()
        self.appointmnet_treatment_layout.addWidget(self.appointment_treatment_label)
        self.appointmnet_treatment_layout.addWidget(self.appointment_treatmnet_ledit)

        self.find_appointment_btn = QPushButton("Find Appointment")

        self.radio_button_box = QGroupBox()
        self.radio_button_group = QButtonGroup()

        self.appointment_id_radio = QRadioButton()
        self.appointmnet_details_radio = QRadioButton()
        self.customer_id_radio = QRadioButton()
        self.customer_name_radio = QRadioButton()
        self.customer_address_radio = QRadioButton()
        self.appointment_treatment_radio = QRadioButton()

        self.appointmnet_id_radio.setChecked(True)

        self.radio_button_group.addButton(self.appointment_id_radio)
        self.radio_button_group.setId(self.appointment_id_radio,0)
        self.radio_button_group.addButton(self.appointmnet_details_radio)
        self.radio_button_group.setId(self.appointmnet_details_radio,1)
        self.radio_button_group.addButton(self.customer_id_radio)
        self.radio_button_group.setId(self.customer_id_radio,2)
        self.radio_button_group.addButton(self.customer_name_radio)
        self.radio_button_group.setId(self.customer_name_radio,3)
        self.radio_button_group.addButton(self.customer_address_radio)
        self.radio_button_group.setId(self.customer_address_radio,4)
        self.radio_button_group.addButton(self.appointment_treatment_radio)
        self.radio_button_group.setId(self.appointment_treatment_radio,5)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.appointment_id_radio,0,0)
        self.grid_layout.addWidget(self.appointment_details_radio,1,0)
        self.grid_layout.addWidget(self.customer_id_radio,2,0)
        self.grid_layout.addWidget(self.customer_name_radio,3,0)
        self.grid_layout.addWidget(self.customer_address_radio,4,0)
        self.grid_layout.addWidget(self.appointment_treatment_radio,5,0)
        self.grid_layout.addLayout(self.appointmnet_id_layout,0,1)
        self.grid_layout.addLayout(self.appointment_details_layout,1,1)
        self.grid_layout.addLayout(self.customer_id_layout,2,1)
        self.grid_layout.addLayout(self.customer_name_layout,3,1)
        self.grid_layout.addLayout(self.customer_address_layout,4,1)
        self.grid_layout.addLayout(self.appointment_treatment_layout,5,1)
        self.grid_layout.addWidget(self.find_appointment_btn,6,1)

        self.radio_button_box.setLayout(self.grid_layout)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.radio_button_box)

        self.find_appointment_widget = QWidget()
        self.find_appointmnet_widget.setLayout(self.layout)
        self.stacked_layout.addWidget(self.find_appointmnet_widget)

        self.stacked_layout.setCurrentIndex(0)
        
    def change_search_type(self):
        pass

    def find_appointment(self):
        pass
