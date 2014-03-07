from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class OrderReport(QWidget):
        """Doc String""" 

        def __init__(self,connection):
                super().__init__()

                self.sql = connection

                self.title_label = QLabel("""<html>
                                          <body>
                                                   <p><span style=" font-size:16pt; font-weight:1000;">Unordered Products from Outstanding Orders</span></p>
                                          </body>
                                         </html>""")

                self.products_view = QTableView()

                self.products_view_model = self.sql.unordered_products_report_model()

                self.products_view.setModel(self.products_view_model)

                self.layout = QVBoxLayout()
                self.layout.addWidget(self.title_label)
                self.layout.addWidget(self.products_view)

                self.setLayout(self.layout)

