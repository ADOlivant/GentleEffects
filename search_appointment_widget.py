from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import re

class SearchAppointment(QWidget):

    #Appointment Found Signal to fire when Appointmnet Selected
    appointmentSelectedSignal = pyqtSignal()

    def __init__(self, connection ):
        super().__init__()

        self.connection = connection 

        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.find_appointment_layout()
        #self.find_appointment_layout()

        #connections
        self.radio_button_group.buttonClicked.connect(self.change_search_type)
        self.find_appointment_btn.clicked.connect(self.find_appointment)

    def find_appointment_layout(self):
        self.title_label = QLabel("""<html>
                                          <body>
                                               <p><span style=" font-size:16pt; font-weight:1000;">Search Appointments</span></p>
                                          </body>
                                     </html>""")

        self.appointment_id_label = QLabel("Appointment ID:")
        self.appointment_date_label = QLabel("Appointment Date:")
        self.appointment_time_label = QLabel("Appoitment Time:")
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
        self.appointment_date_selector.setEnabled(False)
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
        self.customer_id_layout.addWidget(self.customer_id_label)
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
        
        self.appointment_treatment_combobox = QComboBox()
        self.appointment_treatment_model = self.connection.create_treatment_combobox_model()
        self.appointment_treatment_combobox.setModel(self.appointment_treatment_model)
        self.appointment_treatment_combobox.setModelColumn(1)
        self.appointment_treatment_combobox.setEnabled(False)

        self.appointment_treatment_layout = QHBoxLayout()
        self.appointment_treatment_layout.addWidget(self.appointment_treatment_label)
        self.appointment_treatment_layout.addWidget(self.appointment_treatment_combobox)

        self.find_appointment_btn = QPushButton("Find Appointment")

        self.radio_button_box = QGroupBox()
        self.radio_button_group = QButtonGroup()

        self.appointment_id_radio = QRadioButton()
        self.appointment_details_radio = QRadioButton()
        self.customer_id_radio = QRadioButton()
        self.customer_name_radio = QRadioButton()
        self.customer_address_radio = QRadioButton()
        self.appointment_treatment_radio = QRadioButton()

        self.appointment_id_radio.setChecked(True)

        self.radio_button_group.addButton(self.appointment_id_radio)
        self.radio_button_group.setId(self.appointment_id_radio,0)
        self.radio_button_group.addButton(self.appointment_details_radio)
        self.radio_button_group.setId(self.appointment_details_radio,1)
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
        self.find_appointment_widget.setLayout(self.layout)
        self.stacked_layout.addWidget(self.find_appointment_widget)

        self.stacked_layout.setCurrentIndex(0)
        
    def change_search_type(self):
        if self.radio_button_group.checkedId() == 0:
            self.appointment_id_ledit.setEnabled(True)
            self.appointment_date_selector.setEnabled(False)
            self.appointment_time_selector.setEnabled(False)
            self.customer_id_ledit.setEnabled(False)
            self.customer_first_name_ledit.setEnabled(False)
            self.customer_last_name_ledit.setEnabled(False)
            self.customer_number_ledit.setEnabled(False)
            self.customer_postcode_ledit.setEnabled(False)
            self.appointment_treatment_combobox.setEnabled(False)
        elif self.radio_button_group.checkedId() == 1:
            self.appointment_id_ledit.setEnabled(False)
            self.appointment_date_selector.setEnabled(True)
            self.appointment_time_selector.setEnabled(True)
            self.customer_id_ledit.setEnabled(False)
            self.customer_first_name_ledit.setEnabled(False)
            self.customer_last_name_ledit.setEnabled(False)
            self.customer_number_ledit.setEnabled(False)
            self.customer_postcode_ledit.setEnabled(False)
            self.appointment_treatment_combobox.setEnabled(False)
        elif self.radio_button_group.checkedId() == 2:
            self.appointment_id_ledit.setEnabled(False)
            self.appointment_date_selector.setEnabled(False)
            self.appointment_time_selector.setEnabled(False)
            self.customer_id_ledit.setEnabled(True)
            self.customer_first_name_ledit.setEnabled(False)
            self.customer_last_name_ledit.setEnabled(False)
            self.customer_number_ledit.setEnabled(False)
            self.customer_postcode_ledit.setEnabled(False)
            self.appointment_treatment_combobox.setEnabled(False)
        elif self.radio_button_group.checkedId() == 3:
            self.appointment_id_ledit.setEnabled(False)
            self.appointment_date_selector.setEnabled(False)
            self.appointment_time_selector.setEnabled(False)
            self.customer_id_ledit.setEnabled(False)
            self.customer_first_name_ledit.setEnabled(True)
            self.customer_last_name_ledit.setEnabled(True)
            self.customer_number_ledit.setEnabled(False)
            self.customer_postcode_ledit.setEnabled(False)
            self.appointment_treatment_combobox.setEnabled(False)
        elif self.radio_button_group.checkedId() == 4:
            self.appointment_id_ledit.setEnabled(False)
            self.appointment_date_selector.setEnabled(False)
            self.appointment_time_selector.setEnabled(False)
            self.customer_id_ledit.setEnabled(False)
            self.customer_first_name_ledit.setEnabled(False)
            self.customer_last_name_ledit.setEnabled(False)
            self.customer_number_ledit.setEnabled(True)
            self.customer_postcode_ledit.setEnabled(True)
            self.appointment_treatment_combobox.setEnabled(False)
        elif self.radio_button_group.checkedId() == 5:
            self.appointment_id_ledit.setEnabled(False)
            self.appointment_date_selector.setEnabled(False)
            self.appointment_time_selector.setEnabled(False)
            self.customer_id_ledit.setEnabled(False)
            self.customer_first_name_ledit.setEnabled(False)
            self.customer_last_name_ledit.setEnabled(False)
            self.customer_number_ledit.setEnabled(False)
            self.customer_postcode_ledit.setEnabled(False)
            self.appointment_treatment_combobox.setEnabled(True)

    def find_appointment(self):
        if self.radio_button_group.checkedId() == 0:
            self.search_values = (self.appointment_id_ledit.text(),)
            self.model = self.connection.find_appointment_by_id(self.search_values)
        elif self.radio_button_group.checkedId() == 1:
            self.search_values = None
            self.model = self.connection.find_appointment_by_details(self.search_values)
        elif self.radio_button_group.checkedId() == 2:
            self.search_values = (self.customer_id_ledit.text(),)
            self.model = self.connection.find_appointment_by_customer_id(self.search_values)
        elif self.radio_button_group.checkedId() == 3:
            self.search_values = (self.customer_first_name_ledit.text(),self.customer_last_name_ledit.text(),)
            self.model = self.connection.find_appointment_by_customer_name(self.search_values)
        elif self.radio_button_group.checkedId() == 4:
            self.search_values = (self.customer_number_ledit.text(),self.customer_postcode_ledit.text(),)
            self.model = self.connection.find_appointment_by_customer_address(self.search_values)
        elif self.radio_button_group.checkedId() == 5:
            self.search_values = (self.appointment_treatment_model.index(self.appointment_treatment_combobox.currentIndex(),0).data(),)
            self.model = self.connection.find_appointment_by_treatment(self.search_values)
        self.select_appointment_layout_view()
        self.stacked_layout.setCurrentIndex(1)

    def select_appointment_layout_view(self):
        self.title_label = QLabel("""<html>
                                          <body>
                                               <p><span style=" font-size:16pt; font-weight:1000;">Select Appointment</span></p>
                                          </body>
                                     </html>""")
        self.select_appointment_btn = QPushButton("Select Appointment")
        self.appointment_view = QTableView()
        self.appointment_view.setSelectionBehavior(1)
        self.appointment_view.setModel(self.model)

        self.appointment_view_layout = QVBoxLayout()
        self.appointment_view_layout.addWidget(self.title_label)
        self.appointment_view_layout.addWidget(self.appointment_view)
        self.appointment_view_layout.addWidget(self.select_appointment_btn)

        self.appointment_view_widget = QWidget()
        self.appointment_view_widget.setLayout(self.appointment_view_layout)

        self.stacked_layout.addWidget(self.appointment_view_widget)

        #connections
        self.select_appointment_btn.clicked.connect(self.select_appointment)

    def select_appointment(self):
        self.appointmentSelectedSignal.emit()
