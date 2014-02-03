from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

from add_treatment_widget import *
from search_treatment_widget import *

class AmendTreatment(QWidget):

    def __init__(self,connection):

        super().__init__()

        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)

        self.connection = connection
        
        self.search_treatment_widget = SearchTreatment(self.connection)
        self.stacked_layout.addWidget(self.search_treatment_widget)
        self.stacked_layout.setCurrentIndex(0)

        #connections
        self.search_treatment_widget.treatmentSelectedSignal.connect(self.amend_treatment_details)

    def amend_treatment_details(self):
        self.amend_treatment_widget = AddTreatment()

        self.amend_treatment_widget.title_label.setText("""<html>
                                          <body>
                                               <p><span style=" font-size:16pt; font-weight:1000;">Amend Treatment</span></p>
                                          </body>
                                     </html>""")
        self.amend_treatment_widget.save_pushbutton.setText("Save Amended Details")
        self.amend_treatment_widget.reset_pushbutton.hide()
        
        self.stacked_layout.addWidget(self.amend_treatment_widget)
        self.stacked_layout.setCurrentIndex(1)
