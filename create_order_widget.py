from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import datetime

from search_customer_widget import *

class CreateOrder(QWidget):
    """This is a widget which enable the end user to create an order."""

    productSelectedSignal = pyqtSignal()
    
    def __init__(self,connection):
        super().__init__()

        self.connection = connection

        self.stacked_order_layout = QStackedLayout()
        self.setLayout(self.stacked_order_layout)

        self.now = datetime.datetime.now()

        self.find_customer_layout()

        #connections
        #self.productSelectedSignal(self.product_selected)

    def find_customer_layout(self):
        self.search_customer_layout = SearchCustomer()
        self.stacked_order_layout.addWidget(self.search_customer_layout)
        self.stacked_order_layout.setCurrentIndex(0)

        #connections
        self.search_customer_layout.customerSelectedSignal.connect(self.create_order)

    def create_order(self):
        details = self.order_details_default()
        self.connection.create_order(details)
        self.order_id = self.find_order_id()
        self.create_order_layout()

    def order_details_default(self):
        details = {'DateOfOrder':self.now,
                   'CustomerID':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[0]),
                   'Ordered':"False",
                   'Delivered':"False"}
        return details

    def find_order_id(self):
        details = {'DateOfOrder':self.now,
                   'CustomerID':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[0])}
        self.order_id = self.connection.get_order_id(details)

    def create_order_layout(self):
        #TITLE FOR LAYOUT
        self.order_title_label = QLabel("""<html>
					  <body>
					       <p><span style=" font-size:16pt; font-weight:1000; color:Green">New Order</span></p>
					  </body>
				     </html>""")
        self.create_order_button = QPushButton("Create Order")
        self.create_order_button.hide()

        self.order_error_message = QLabel()
        self.order_error_message.hide()

        #CUSTOMER DETAILS LAYOUT
        self.customer_details_label = QLabel("""<html>
					  <body>
					       <p><span style=" font-size:12pt; font-weight:750;">Customer Details</span></p>
					  </body>
				     </html>""")
        
        self.customer_data = self.get_customer_details()
        self.customer_id_label = QLabel("ID: {0}".format(self.customer_data['CustomerID']))
        self.customer_name_label = QLabel("Name: {0}, {1}".format(self.customer_data['LastName'],self.customer_data['FirstName']))
        self.customer_dob_label = QLabel("Date of Birth: {0}".format(self.customer_data['DateOfBirth']))
        self.customer_address_label = QLabel("Address: {0} {1}, \n                {2}, \n                {3}, \n                {4}".format(self.customer_data['House'],
                                                                                            self.customer_data['Road'],
                                                                                            self.customer_data['City'],
                                                                                            self.customer_data['County'],
                                                                                            self.customer_data['Postcode']))
        self.customer_contact_label = QLabel("Contact Numbers: {0}, {1} - Preferred: {2}".format(self.customer_data['Mobile'],
                                                                                                 self.customer_data['Home'],
                                                                                                 self.customer_data['Prefered']))
        self.customer_email_label = QLabel("Email: {0}".format(self.customer_data['Email']))
        self.customer_email_button = QPushButton("Email Customer")

        self.customer_details_layout = QGridLayout()
        self.customer_details_layout.addWidget(self.customer_details_label,0,0,1,2)
        self.customer_details_layout.addWidget(self.customer_name_label,1,0)
        self.customer_details_layout.addWidget(self.customer_id_label,1,1)
        self.customer_details_layout.addWidget(self.customer_dob_label,2,0,1,2)
        self.customer_details_layout.addWidget(self.customer_address_label,3,0,1,2)
        self.customer_details_layout.addWidget(self.customer_contact_label,4,0,1,2)
        self.customer_details_layout.addWidget(self.customer_email_label,5,0)
        self.customer_details_layout.addWidget(self.customer_email_button,5,1)
        self.customer_details_widget = QWidget()
        self.customer_details_widget.setLayout(self.customer_details_layout)

        

        #ADD / REMOVE BUTTON LAYOUT
        self.add_product_button = QPushButton("Add Product >>")
        self.remove_product_button = QPushButton("<< Remove Product")
        self.button_layout = QVBoxLayout()
        self.button_layout.addWidget(self.add_product_button)
        self.button_layout.addWidget(self.remove_product_button)

        self.button_widget = QWidget()
        self.button_widget.setLayout(self.button_layout)

        #connections
        self.add_product_button.clicked.connect(self.add_product)

        #ALL PRODUCT LAYOUT
        self.search_product_lineedit = QLineEdit()
        self.model = self.create_product_model(("",))

        self.product_view = QTableView()
        self.product_view.setSelectionBehavior(1)
        self.product_view.setModel(self.model)
        self.product_view.hideColumn(0)
        self.product_view.hideColumn(4)

        self.product_layout = QVBoxLayout()
        self.product_layout.addWidget(self.search_product_lineedit)
        self.product_layout.addWidget(self.product_view)
        self.product_widget = QWidget()
        self.product_widget.setLayout(self.product_layout)

        #connections
        self.search_product_lineedit.textEdited.connect(self.refresh)

        #SELECTED PRODUCT LAYOUT
        self.current_products = QTableView()
        self.current_products_model = self.create_current_product_model(self.order_id)
        self.current_products.setModel(self.current_products_model)

        #ORDER SELECTION LAYOUT
        self.order_selection_layout = QHBoxLayout()
        self.order_selection_layout.addWidget(self.product_widget)
        self.order_selection_layout.addWidget(self.button_widget)
        self.order_selection_layout.addWidget(self.current_products)

        self.order_selection_widget = QWidget()
        self.order_selection_widget.setLayout(self.order_selection_layout)
        
        
        self.layout = QGridLayout()
        self.layout.addWidget(self.order_title_label,0,0,1,2)
        self.layout.addWidget(self.order_error_message,1,0,1,2)
        self.layout.addWidget(self.customer_details_widget,2,0)
        self.layout.addWidget(self.order_selection_widget,3,0,1,2)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.stacked_order_layout.addWidget(self.widget)
        self.stacked_order_layout.setCurrentIndex(1)

    def get_customer_details(self):
        details = {'CustomerID':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[0]),
                   'FirstName':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[1]),
                   'LastName':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[2]),
                   'DateOfBirth':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[3]),
                   'House':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[4]),
                   'Road':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[5]),
                   'City':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[6]),
                   'County':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[7]),
                   'Postcode':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[8]),
                   'Mobile':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[9]),
                   'Home':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[10]),
                   'Prefered':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[11]),
                   'Email':self.search_customer_layout.customer_view.model().data(self.search_customer_layout.index[12])}
        return details

    def create_product_model(self,values):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.prepare("""SELECT * FROM Product WHERE Name LIKE (?)""")
        query.addBindValue('%{0}%'.format(values[0]))
        query.exec_()
        model.setQuery(query)
        return model

    def create_current_product_model(self,value):
        model = QSqlQueryModel()
        query = QSqlQuery()
        #WHERE OrderLine.ProductID = Product.ID AND OrderLine.OrderID = (?)
        query.prepare("""SELECT Product.Name, Product.Price, Product.Code, OrderLine.Quantity
                         FROM Product, OrderLine
                         WHERE OrderLine.OrderID = (?)""")
        query.addBindValue(value)
        query.exec_()
        model.setQuery(query)
        return model 
    
    def refresh(self):
        self.search_values = (self.search_product_lineedit.text(),)
        self.new_model = self.create_product_model(self.search_values)
        self.product_view.setModel(self.new_model)
        self.product_view.hideColumn(0)

        self.current_products_model = self.create_current_product_model(self.order_id)
        self.current_products.setModel(self.current_products_model)

    def select_product(self):
        details = self.product_details()
        self.productSelectedSignal.emit()
        self.connection.add_product_to_order(details)
        self.product_view.hideColumn(4)

    def get_quantity(self):
        self.quantity_box = QInputDialog()
        self.quantity_box.setInputMode(1)
        self.quantity_box.open()

    def add_product(self):
        self.get_quantity()
        self.quantity = self.quantity_box.intValue()

        self.product_view.showColumn(0)
        self.selected_record = self.product_view.selectedIndexes()
        details = {'ProductID':self.product_view.model().data(self.selected_record[0]),
                   'OrderID':self.order_id,
                   'Quantity':self.quantity}

        self.productSelectedSignal.emit()
        self.connection.add_product_to_order(details)
        self.refresh()

        
        
    
