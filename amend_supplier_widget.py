from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

from add_supplier_widget import *

class AmendSupplier(QWidget):
    """This will be used to search for suppliers and then to ammend or delete"""

    def __init__(self,connection):
        super().__init__()

        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)

        self.connection = connection

        self.amend_supplier_widget = AddSupplier()

        self.amend_supplier_widget.title_label.setText("""<html>
					  <body>
					       <p><span style=" font-size:16pt; font-weight:1000;">Amend Supplier</span></p>
					  </body>
				     </html>""")

        self.create_comobobox_model()
        self.amend_supplier_widget.combo_box.setModel(self.model)
        self.amend_supplier_widget.combo_box.setModelColumn(1)
        self.amend_supplier_widget.combo_box.show()

        self.amend_supplier_widget.reset_button.hide()
        self.amend_supplier_widget.save_button.setText("Save updated details")

        self.stacked_layout.addWidget(self.amend_supplier_widget)
        self.stacked_layout.setCurrentIndex(0)

        self.populate_lineedits()

        #connections
        self.amend_supplier_widget.combo_box.currentIndexChanged.connect(self.populate_lineedits)

    def create_comobobox_model(self):
        self.model = QSqlRelationalTableModel()
        self.model.setTable("Supplier")
        self.model.select()

    def model_details(self):
        details = {'Name':self.model.index(self.amend_supplier_widget.combo_box.currentIndex(),1).data(),
                    'House':self.model.index(self.amend_supplier_widget.combo_box.currentIndex(),2).data(),
                    'Road':self.model.index(self.amend_supplier_widget.combo_box.currentIndex(),3).data(),
                    'City':self.model.index(self.amend_supplier_widget.combo_box.currentIndex(),4).data(),
                    'County':self.model.index(self.amend_supplier_widget.combo_box.currentIndex(),5).data(),
                    'PostCode':self.model.index(self.amend_supplier_widget.combo_box.currentIndex(),6).data(),
                    'ContactNum':self.model.index(self.amend_supplier_widget.combo_box.currentIndex(),7).data(),
                    'Email':self.model.index(self.amend_supplier_widget.combo_box.currentIndex(),8).data(),
                    'Website':self.model.index(self.amend_supplier_widget.combo_box.currentIndex(),9).data()}
        return details

    def populate_lineedits(self):
        supplier_details = self.model_details()
        print(supplier_details)
        self.amend_supplier_widget.name_lineedit.setText(supplier_details['Name'])
        self.amend_supplier_widget.number_lineedit.setText(supplier_details['House'])
        self.amend_supplier_widget.road_lineedit.setText(supplier_details['Road'])
        self.amend_supplier_widget.city_lineedit.setText(supplier_details['City'])
        self.amend_supplier_widget.county_lineedit.setText(supplier_details['County'])
        self.amend_supplier_widget.postcode_lineedit.setText(supplier_details['PostCode'])
        self.amend_supplier_widget.contact_lineedit.setText(supplier_details['ContactNum'])
        self.amend_supplier_widget.email_lineedit.setText(supplier_details['Email'])
        self.amend_supplier_widget.website_lineedit.setText(supplier_details['Website'])
        self.amend_supplier_widget.website_lineedit.setText(supplier_details['Website'])
