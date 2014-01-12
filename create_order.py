from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

from search_customer_widget import *

class CreateOrder(QWidget):
    """This is a widget which enable the end user to create an order."""

    def __init__(self):
        super().__init__()

        self.stacked_order_layout = QStackedLayout()
        self.setLayout(self.stacked_order_layout)

        self.find_customer_layout()

    def find_customer_layout(self):
        self.search_customer_layout = SearchCustomer()
        self.stacked_order_layout.addWidget(self.search_customer_layout)
        self.stacked_order_layout.setCurrentIndex(0)

        #Connections - Signal
        self.search_customer_layout.customerSelectedSignal.connect(self.create_order)

    def create_order(self):
        pass

    def create_order_layout(self):
        pass 
