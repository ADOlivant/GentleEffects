from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

from add_product_widget import *
from search_product_widget import *

class AmendProduct(QWidget):

    def __init__(self,connection):
        super().__init__()

        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)

        self.search_product_widget = SearchProduct(connection)
        self.stacked_layout.addWidget(self.search_product_widget)
        self.stacked_layout.setCurrentIndex(0)

        #connections
        self.search_product_widget.productSelectedSignal.connect(self.amend_product_details)

    def amend_product_details(self):
        self.amend_product_details = AddProduct()
        self.product_details = self.search_product_widget.selected_product_details()
        self.amend_product_details.save_pushbutton.setText("Amend Details")
        self.amend_product_details.title_label.setText("""<html>
                                          <body>
                                               <p><span style=" font-size:16pt; font-weight:1000;">Amend Product</span></p>
                                          </body>
                                     </html>""")
        self.amend_product_details.name_lineedit.setText(self.product_details[1])

        self.stacked_layout.addWidget(self.amend_product_details)
        self.stacked_layout.setCurrentIndex(1)
    

