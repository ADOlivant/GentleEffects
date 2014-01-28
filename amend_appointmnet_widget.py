from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

from create_appointment import *

class AmendAppointmnet(QWidget):
    """DOC STRING"""

    def __init__(self,connection):
        super().__init__()

        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)

        self.connection = connection

        self.amend_appointmnet_widget = CreateAppointment()
        self.amend_appointmnet_widget.create_appointment()

        self.stacked_layout.addWidget(self.amend_appointmnet_widget)
        self.stacked_layout.setCurrentIndex(0)
        
        

        
