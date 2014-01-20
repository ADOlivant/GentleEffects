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

        self.connection = connection
        
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
        self.amend_product_details.name_lineedit.setText(self.product_details['Name'])
        self.amend_product_details.price_dblspinbox.setValue(self.product_details['Price'])
        self.amend_product_details.code_lineedit.setText(self.product_details['Code'])
        self.amend_product_details.supplier_combobox.hide()
        #self.connection.get_supplier_name_from_id(details['SupplierID'])
        self.amend_product_details.supplier_lineedit.setText(self.connection.get_supplier_name_from_id(details['SupplierID']))
        self.amend_product_details.supplier_lineedit.show()
        self.amend_product_details.supplier_change_btn.show()

        #connections
        self.amend_product_details.supplier_change_btn.clicked.connect(self.enable_supplier_combo)

        self.stacked_layout.addWidget(self.amend_product_details)
        self.stacked_layout.setCurrentIndex(1)

    def enable_supplier_combo(self):
        self.amend_product_details.supplier_change_btn.hide()
        self.amend_product_details.supplier_lineedit.hide()
        self.amend_product_details.supplier_combobox.show()
    

