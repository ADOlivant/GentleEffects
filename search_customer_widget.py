from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import re

from search_customer_table_models import *

class SearchCustomer(QWidget):
        """Searching Customer data from SQL Database with PyQt4"""

        #Customer Found Signal to fire when Customer Selected
        customerSelectedSignal = pyqtSignal()

        def __init__(self):
                super().__init__()

                self.stacked_layout = QStackedLayout()
                self.setLayout(self.stacked_layout)
                self.find_customer_layout()

                #connections
                self.radio_button_group.buttonClicked.connect(self.change_search_type)
                self.find_customer_button.clicked.connect(self.find_customer)

        def find_customer_layout(self):

                self.title_label = QLabel("""<html>
                                          <body>
                                               <p><span style=" font-size:16pt; font-weight:1000;">Search Customer</span></p>
                                          </body>
                                     </html>""")

                self.customer_id_label = QLabel("Customer ID:")
                self.customer_fName_label = QLabel("First Name:")
                self.customer_lName_label = QLabel("Last Name:")
                self.customer_number_label = QLabel("House No or Name:")
                self.customer_postcode_label = QLabel("Postcode")

                self.customer_id_ledit = QLineEdit()
                self.customer_fName_ledit = QLineEdit()
                self.customer_fName_ledit.setEnabled(False)
                self.customer_lName_ledit = QLineEdit()
                self.customer_lName_ledit.setEnabled(False)
                self.customer_number_ledit = QLineEdit()
                self.customer_number_ledit.setEnabled(False)
                self.customer_postcode_ledit = QLineEdit()
                self.customer_postcode_ledit.setEnabled(False)

                self.find_customer_button = QPushButton("Find Customer")

                self.radio_button_box = QGroupBox()
                self.radio_button_group = QButtonGroup()

                self.id_radio = QRadioButton()
                self.postcode_radio = QRadioButton()
                self.name_radio = QRadioButton()

                self.id_radio.setChecked(True)

                self.radio_button_group.addButton(self.id_radio)
                self.radio_button_group.setId(self.id_radio,0)
                self.radio_button_group.addButton(self.name_radio)
                self.radio_button_group.setId(self.name_radio,1)
                self.radio_button_group.addButton(self.postcode_radio)
                self.radio_button_group.setId(self.postcode_radio,2)

                self.customer_id_layout = QGridLayout()
                self.customer_id_layout.addWidget(self.customer_id_label,0,0)
                self.customer_id_layout.addWidget(self.customer_id_ledit,0,1)

                self.customer_name_layout = QGridLayout()
                self.customer_name_layout.addWidget(self.customer_fName_label,0,0)
                self.customer_name_layout.addWidget(self.customer_fName_ledit,0,1)
                self.customer_name_layout.addWidget(self.customer_lName_label,1,0)
                self.customer_name_layout.addWidget(self.customer_lName_ledit,1,1)

                self.customer_postcode_layout = QGridLayout()
                self.customer_postcode_layout.addWidget(self.customer_number_label,0,0)
                self.customer_postcode_layout.addWidget(self.customer_number_ledit,0,1)
                self.customer_postcode_layout.addWidget(self.customer_postcode_label,1,0)
                self.customer_postcode_layout.addWidget(self.customer_postcode_ledit,1,1)

                self.grid_layout = QGridLayout()
                self.grid_layout.addWidget(self.id_radio,0,0)
                self.grid_layout.addWidget(self.name_radio,1,0)
                self.grid_layout.addWidget(self.postcode_radio,2,0)
                self.grid_layout.addLayout(self.customer_id_layout,0,1)
                self.grid_layout.addLayout(self.customer_name_layout,1,1)
                self.grid_layout.addLayout(self.customer_postcode_layout,2,1)
                self.grid_layout.addWidget(self.find_customer_button,3,1)

                self.radio_button_box.setLayout(self.grid_layout)

                self.layout = QVBoxLayout()
                self.layout.addWidget(self.title_label)
                self.layout.addWidget(self.radio_button_box)

                self.find_customer_widget = QWidget()
                self.find_customer_widget.setLayout(self.layout)
                self.stacked_layout.addWidget(self.find_customer_widget)

        def select_customer_layout(self):
                self.customer_view = QTableView()
                self.customer_view.setSelectionBehavior(1)
                self.customer_view.setModel(self.model)

                self.customer_view_layout = QVBoxLayout()
                self.customer_view_layout.addWidget(self.customer_view)

                self.select_customer_button = QPushButton("Select Customer")
                self.customer_view_layout.addWidget(self.select_customer_button)

                self.select_customer_widget = QWidget()
                self.select_customer_widget.setLayout(self.customer_view_layout)
                self.stacked_layout.addWidget(self.select_customer_widget)
                
                #connections
                self.select_customer_button.clicked.connect(self.selected_customer_details)

        def change_search_type(self):
                if self.radio_button_group.checkedId() == 0:
                        self.customer_id_ledit.setEnabled(True)
                        self.customer_fName_ledit.setEnabled(False)
                        self.customer_lName_ledit.setEnabled(False)
                        self.customer_number_ledit.setEnabled(False)
                        self.customer_postcode_ledit.setEnabled(False)
                elif self.radio_button_group.checkedId() == 1:
                        self.customer_id_ledit.setEnabled(False)
                        self.customer_fName_ledit.setEnabled(True)
                        self.customer_lName_ledit.setEnabled(True)
                        self.customer_number_ledit.setEnabled(False)
                        self.customer_postcode_ledit.setEnabled(False)
                elif self.radio_button_group.checkedId() == 2:
                        self.customer_id_ledit.setEnabled(False)
                        self.customer_fName_ledit.setEnabled(False)
                        self.customer_lName_ledit.setEnabled(False)
                        self.customer_number_ledit.setEnabled(True)
                        self.customer_postcode_ledit.setEnabled(True)

        def find_customer(self):
                if self.radio_button_group.checkedId() == 0:
                        self.search_values = (self.customer_id_ledit.text(),)
                        self.model = find_customer_by_id(self,self.search_values)
                elif self.radio_button_group.checkedId() == 1:
                        self.search_values = (self.customer_fName_ledit.text(),self.customer_lName_ledit.text())
                        self.model = find_customer_by_name(self,self.search_values)
                elif self.radio_button_group.checkedId() == 2:
                        self.search_values = (self.customer_number_ledit.text(),self.customer_postcode_ledit.text())
                        self.model = find_customer_by_postcode(self,self.search_values)
                self.select_customer_layout()
                self.stacked_layout.setCurrentIndex(1)

        def selected_customer_details(self):
                self.index = self.customer_view.selectedIndexes()
                self.customer_id = self.customer_view.model().data(self.index[0])
                self.stacked_layout.setCurrentIndex(0)
                self.customerSelectedSignal.emit()
                return self.customer_id
