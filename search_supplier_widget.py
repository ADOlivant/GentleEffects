from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class SearchSupplier(QWidget):
    """This will be used to search for suppliers and then to ammend or delete"""

    #Supplier Found Signal to fire when Supplier Seleceted
    supplierSelectedSignal = pyqtSignal()

    def __init__(self,connection):
        super().__init__()

        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)

        self.connection = connection

        #self.find_supplier_layout()

        #connetions

    def find_supplier_layout():
        self.title_label = QLabel("""<html>
                                          <body>
                                               <p><span style=" font-size:16pt; font-weight:1000;">Search Supplier</span></p>
                                          </body>
                                     </html>""")
        self.supplier_id_lbl = QLabel("Supplier ID:")
        self.supplier_name_lbl = QLabel("Supplier Name:")
        self.number_lbl = QLabel("House No. / Name:")
        self.postcode_lbl = QLabel("
