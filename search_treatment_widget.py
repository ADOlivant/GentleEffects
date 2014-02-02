from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class SearchTreatment(QWidget):
    """This will be used to search for treatments and then to ammend or delete"""

    #Product Found Signal to fire when Product selected.
    teratmentSelectedSignal = pyqtSignal()
    
    def __init__(self,connection):
        super().__init__()

        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)

        self.connection = connection

        self.find_treatment_layout()

        #connections
        self.radio_button_group.buttonClicked.connect(self.change_search_type)
        self.find_treatment_button.clicked.connect(self.find_treatment)

    def find_treatment_layout(self):
        self.title_label = QLabel("""<html>
                                          <body>
                                               <p><span style=" font-size:16pt; font-weight:1000;">Search Treatments</span></p>
                                          </body>
                                     </html>""")
        self.treatment_id_lbl = QLabel("Treatment ID:")
        self.treatment_name_lbl = QLabel("Treatment Name:")
        self.treatment_price_lbl = QLabel("Treatment Price:")

        self.treatment_id_ledit = QLineEdit()
        self.treatment_name_ledit = QLineEdit()
        self.treatment_name_ledit.setEnabled(False)
        self.treatment_price_ledit = QDoubleSpinBox()
        self.treatment_price_ledit.setPrefix("£")
        self.treatment_price_ledit.setSingleStep(0.5)
        self.treatment_price_ledit.setMaximum(999.99)
        self.treatment_price_ledit.setEnabled(False)

        self.find_treatment_button = QPushButton("Find Treatment")

        self.radio_button_box = QGroupBox()
        self.radio_button_group = QButtonGroup()

        self.id_radio = QRadioButton()
        self.name_radio = QRadioButton()
        self.price_radio = QRadioButton()

        self.id_radio.setChecked(True)

        self.radio_button_group.addButton(self.id_radio)
        self.radio_button_group.setId(self.id_radio,0)
        self.radio_button_group.addButton(self.name_radio)
        self.radio_button_group.setId(self.name_radio,1)
        self.radio_button_group.addButton(self.price_radio)
        self.radio_button_group.setId(self.price_radio,2)

        self.treatment_id_layout = QHBoxLayout()
        self.treatment_id_layout.addWidget(self.treatment_id_lbl)
        self.treatment_id_layout.addWidget(self.treatment_id_ledit)

        self.treatment_name_layout = QHBoxLayout()
        self.treatment_name_layout.addWidget(self.treatment_name_lbl)
        self.treatment_name_layout.addWidget(self.treatment_name_ledit)

        self.treatment_price_layout = QHBoxLayout()
        self.treatment_price_layout.addWidget(self.treatment_price_lbl)
        self.treatment_price_layout.addWidget(self.treatment_price_ledit)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.id_radio,0,0)
        self.grid_layout.addWidget(self.name_radio,1,0)
        self.grid_layout.addWidget(self.price_radio,2,0)
        self.grid_layout.addLayout(self.treatment_id_layout,0,1)
        self.grid_layout.addLayout(self.treatment_name_layout,1,1)
        self.grid_layout.addLayout(self.treatment_price_layout,2,1)
        self.grid_layout.addWidget(self.find_treatment_button,3,1)

        self.radio_button_box.setLayout(self.grid_layout)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.radio_button_box)

        self.find_treatment_widget = QWidget()
        self.find_treatment_widget.setLayout(self.layout)
        self.stacked_layout.addWidget(self.find_treatment_widget)

        self.stacked_layout.setCurrentIndex(0)

    def change_search_type(self):
        if self.radio_button_group.checkedId() == 0:
            self.treatment_id_ledit.setEnabled(True)
            self.treatment_name_ledit.setEnabled(False)
            self.treatment_price_ledit.setEnabled(False)
        elif self.radio_button_group.checkedId() == 1:
            self.treatment_id_ledit.setEnabled(False)
            self.treatment_name_ledit.setEnabled(True)
            self.treatment_price_ledit.setEnabled(False)
        elif self.radio_button_group.checkedId() == 2:
            self.treatment_id_ledit.setEnabled(False)
            self.treatment_name_ledit.setEnabled(False)
            self.treatment_price_ledit.setEnabled(True)

    def find_treatment(self):
        print("Hello")

    def select_treatment_layout_view(self):
         self.title_label = QLabel("""<html>
                                          <body>
                                               <p><span style=" font-size:16pt; font-weight:1000;">Select Treatment</span></p>
                                          </body>
                                     </html>""")
         self.select_treatment_btn = QPushButton("Select Treatment")
         self.treatment_view = QTableView()
         self.treatment_view.setSelectionBehavior(1)
         self.treatment_view.setModel(self.model)

         self.treatment_view_layout = QVBoxLayout()
         self.treatment_view_layout.addWidget(self.title_label)
         self.treatment_view_layout.addWidget(self.treatment_view)
         self.treatment_view_layout.addWidget(self.select_treatment_btn)

         self.treatment_view_widget = QWidget()
         self.treatment_view_widget.setLayout(self.treatment_view_layout)

         self.stacked_layout.addWidget(self.treatment_view_widget)

         #connection
         self.select_treatment_btn.clicked.connect(self.selected_treatment)

    def selected_treatment(self):
        self.index = self.treatment_view.selectedIndexes()
        self.treatment_id = self.treatment_view.model().data(self.index[0])
        self.treatmentSelectedSignal.emit()

    def selected_treatment_details(self):
        details = {'ID':self.treatment_view.model().data(self.index[0]),
                   'Name':self.treatment_view.model().data(self.index[1]),
                   'Price':self.treatment_view.model().data(self.index[2]),
                   'Code':self.treatment_view.model().data(self.index[3]),
                   'SupplierID':self.treatment_view.model().data(self.index[4])}
        return details