from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import os
import re

from SQL import *
from add_treatment_widget import *
from add_customer_widget import *
from add_product_widget import *
from amend_product_widget import *
from add_supplier_widget import *
from amend_supplier_widget import *
from search_appointment_widget import *
from search_customer_widget import *
from search_product_widget import *
from create_appointment import *
from amend_appointment_widget import *
from create_order import *
from welcome_widget import *

class MainWindow(QMainWindow):
    """The Main Window used with the System"""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gentle Effects Customer Management System")

        self.status_bar = QStatusBar()
        self.status_label = QLabel()
        self.status_bar.addWidget(self.status_label)

        self.path = "GentleEffects.db"
        self.connection = SQL(self.path)
        self.connection.open_database()
        
        self.status_label.setText("Connected to {0}".format(self.connection.db.databaseName()))
        self.setStatusBar(self.status_bar)

        self.title_label = QLabel("""<html>
                                          <body>
                                                   <p><span style=" font-size:16pt; font-weight:1000; color:green">Welcome to Gentle Effect's Customer Management System</span></p>
                                          </body>
                                         </html>""")

        #Actions for use within menus / toolbars
        #Customer Details Management
        self.new_customer = QAction("Add New Customer",self)
        self.edit_customer = QAction("Edit Exisiting Customer",self)
        self.edit_medical = QAction("Edit Medical Information",self)
        self.add_allergy = QAction("Add Allergy to DB",self)
        self.edit_allergy = QAction("Edit Allergy",self)
        self.delete = QAction("7 Year bulk delete",self)
        #Treatment Managemnet
        self.add_treatmnet = QAction("Add New Treatment",self)
        self.edit_treatment = QAction("Edit Exisiting Treatment",self)
        #Appointment Management
        self.new_appointment = QAction("Create Appointment",self)
        self.edit_appointment = QAction("Amend Appointment",self)
        self.cancel_appointmnet = QAction("Cancel Appointment",self)
        #Supplier Managment
        self.new_supplier = QAction("Add New Supplier",self)
        self.amend_supplier = QAction("Amend Supplier",self)
        self.delete_supplier = QAction("Remove Supplier",self)
        #Product Management
        self.new_product = QAction("Add New Product",self)
        self.ammend_product = QAction("Amend Product Details",self)
        self.delete_product = QAction("Delete Existing Product",self)
        #Order Management
        self.new_order = QAction("Add New Order",self)
        self.amend_order = QAction("Amend Order",self)
        self.cancel_order = QAction("Cancel Order",self)
        #Administration
        self.create_reports = QAction("Create Reports",self)
        self.backup = QAction("Backup Database",self)
        self.database = QAction("Set Database File Path",self)
        self.add_user = QAction("Add System User",self)
        self.edit_user = QAction("Edit User",self)
        #Extra
        self.reset_central_widget = QAction("Reset Screen",self)

        #Create Menubar
        self.menu_bar = QMenuBar()
        self.customer_menu = self.menu_bar.addMenu("Customers")
        self.treatment_menu = self.menu_bar.addMenu("Treatments")
        self.appointment_menu = self.menu_bar.addMenu("Appointments")
        self.supplier_menu = self.menu_bar.addMenu("Suppliers")
        self.product_menu = self.menu_bar.addMenu("Products")
        self.order_menu = self.menu_bar.addMenu("Orders")
        self.admin_menu = self.menu_bar.addMenu("Administration")
        self.menu_bar.addAction(self.reset_central_widget)
        #Add Actions to the Menu Bar
        self.customer_menu.addAction(self.new_customer)
        self.customer_menu.addSeparator()
        #self.customer_menu.addAction(self.edit_customer)
        #self.customer_menu.addAction(self.edit_medical)
        self.customer_menu.addSeparator()
        #self.customer_menu.addAction(self.add_allergy)
        #self.customer_menu.addAction(self.edit_allergy)
        self.customer_menu.addSeparator()
        #self.customer_menu.addAction(self.delete)
        self.treatment_menu.addAction(self.add_treatmnet)
        self.treatment_menu.addAction(self.edit_treatment)
        self.appointment_menu.addAction(self.new_appointment)
        self.appointment_menu.addAction(self.edit_appointment)
        #self.appointment_menu.addAction(self.cancel_appointmnet)
        self.supplier_menu.addAction(self.new_supplier)
        self.supplier_menu.addAction(self.amend_supplier)
        #self.supplier_menu.addAction(self.delete_supplier)
        self.product_menu.addAction(self.new_product)
        self.product_menu.addAction(self.ammend_product)
        #self.product_menu.addAction(self.delete_product)
        self.order_menu.addAction(self.new_order)
        #self.order_menu.addAction(self.amend_order)
        #self.order_menu.addAction(self.cancel_order)
        #self.admin_menu.addAction(self.create_reports)
        self.admin_menu.addSeparator()
        #self.admin_menu.addAction(self.backup)
        #self.admin_menu.addAction(self.database)
        self.admin_menu.addSeparator()
        #self.admin_menu.addAction(self.add_user)
        #self.admin_menu.addAction(self.edit_user)

        self.setMenuBar(self.menu_bar)

        self.reset_screen()

        #connections
        self.new_customer.triggered.connect(self.view_add_new_customer)
        self.add_treatmnet.triggered.connect(self.add_new_treatment)
        self.new_appointment.triggered.connect(self.create_appointment)
        self.reset_central_widget.triggered.connect(self.reset_screen)
        self.new_product.triggered.connect(self.view_add_new_product)
        self.new_supplier.triggered.connect(self.view_add_new_supplier)
        self.new_order.triggered.connect(self.create_order)
        self.add_user.triggered.connect(self.test_area)
        self.ammend_product.triggered.connect(self.ammend_product_details)
        self.amend_supplier.triggered.connect(self.amend_supplier_details)
        self.edit_appointment.triggered.connect(self.edit_appointment_details)

    def ammend_product_details(self):
        self.ammend_product_widget = AmendProduct(self.connection)
        self.setCentralWidget(self.ammend_product_widget)
        
    def view_add_new_customer(self):
        self.add_customer_widget = AddCustomer()
        self.setCentralWidget(self.add_customer_widget)
        #Connections - Signal
        self.add_customer_widget.customerAddedSignal.connect(self.process_save_customer)

    def process_save_customer(self):
        details = self.add_customer_widget.customer_details()
        self.connection.add_new_customer(details)

    def add_new_treatment(self): 
        TreatmentWidget = AddTreatment()
        self.setCentralWidget(TreatmentWidget)

    def create_appointment(self):
        create_appointment = CreateAppointment(self.connection)
        self.setCentralWidget(create_appointment)

    def edit_appointment_details(self):
        edit_appointment = AmendAppointment(self.connection)
        self.setCentralWidget(edit_appointment)

    def view_add_new_supplier(self):
        self.add_supplier_widget = AddSupplier()
        self.setCentralWidget(self.add_supplier_widget)
        #Connections - Signal
        self.add_supplier_widget.supplierAddedSignal.connect(self.process_save_supplier)

    def process_save_supplier(self):
        details = self.add_supplier_widget.product_details()
        self.connection.add_new_supplier(details)

    def amend_supplier_details(self):
        amend_supplier_widget = AmendSupplier(self.connection)
        self.setCentralWidget(amend_supplier_widget)

    def view_add_new_product(self):
        self.add_product_widget = AddProduct()
        self.setCentralWidget(self.add_product_widget)
        #Connections - Signal
        self.add_product_widget.productAddedSignal.connect(self.process_save_product)

    def process_save_product(self):
        details = self.add_product_widget.product_details()
        self.connection.add_new_product(details)

    def create_order(self):
        OrderWidget = CreateOrder(self.connection)
        self.setCentralWidget(OrderWidget)

    def reset_screen(self):
        welcome = WelcomeWidget()
        self.setCentralWidget(welcome)

    def test_area(self):
        calendar = CreateAppointment()
        self.setCentralWidget(calendar)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
