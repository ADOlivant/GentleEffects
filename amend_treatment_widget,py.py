from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

from add_treatment_widget import *
from search_treatment_widget import *

class AmendProduct(QWidget):

    def __init__(self,connection)

        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)

        self.connection = connection
        
        self.search_treatment_widget = SearchTreatment(self.connection)
        self.stacked_layout.addWidget(self.search_treatment_widget)
        self.stacked_layout.setCurrentIndex(0)

    def amend_treatment_details(self):
        self.amend_product_widget = SearchTreatment()

        
