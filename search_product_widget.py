from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class SearchProduct(QWidget):
    """This will be used to search for products and then to ammend or delete"""

    #Product Found Signal to fire when Product selected.
    productSelectedSignal = pyqtSignal()
    
    def __init__(self):
        super().__init__()

        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)

        self.find_product_layout()

    def find_product_layout(self):
        self.title_label = QLabel("""<html>
                                          <body>
                                               <p><span style=" font-size:16pt; font-weight:1000;">Search Products</span></p>
                                          </body>
                                     </html>""")
        self.product_id_lbl = QLabel("Product ID:")
        self.product_name_lbl = QLabel("Product Name:")
        self.product_price_lbl = QLabel("Product Price:")

        self.product_id_ledit = QLineEdit()
        self.product_name_ledit = QLineEdit()
        self.product_name_ledit.setEnabled(False)
        self.product_price_ledit = QDoubleSpinBox()
        self.product_price_ledit.setPrefix("£")
        self.product_price_ledit.setSingleStep(0.5)
        self.product_price_ledit.setMaximum(999.99)
        self.product_price_ledit.setEnabled(False)

        self.find_product_btn = QPushButton("Find Product")

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

        self.product_id_layout = QHBoxLayout()
        self.product_id_layout.addWidget(self.product_id_lbl)
        self.product_id_layout.addWidget(self.product_id_ledit)

        self.product_name_layout = QHBoxLayout()
        self.product_name_layout.addWidget(self.product_name_lbl)
        self.product_name_layout.addWidget(self.product_name_ledit)

        self.product_price_layout = QHBoxLayout()
        self.product_price_layout.addWidget(self.product_price_lbl)
        self.product_price_layout.addWidget(self.product_price_ledit)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.id_radio,0,0)
        self.grid_layout.addWidget(self.name_radio,1,0)
        self.grid_layout.addWidget(self.price_radio,2,0)
        self.grid_layout.addLayout(self.product_id_layout,0,1)
        self.grid_layout.addLayout(self.product_name_layout,1,1)
        self.grid_layout.addLayout(self.product_price_layout,2,1)
        self.grid_layout.addWidget(self.find_product_btn,3,1)

        self.radio_button_box.setLayout(self.grid_layout)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.radio_button_box)

        self.find_product_widget = QWidget()
        self.find_product_widget.setLayout(self.layout)
        self.stacked_layout.addWidget(self.find_product_widget)

        self.stacked_layout.setCurrentIndex(0)
        

        
