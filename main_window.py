from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import os
import re

from add_treatment_widget import *
from add_customer_widget import *
from add_product_widget import *
from add_supplier_widget import *

class MainWindow(QMainWindow):
    """The Main Window used with the System"""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gentle Effects Customer Management System")

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("GentleEffects.db")
        self.db.open()

        self.pragma_on = QSqlQuery()
        self.pragma_on.prepare("""PRAGMA foreign_keys = ON""")
        self.pragma_on.exec_()

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
        self.ammend_product = QAction("Ammend Product Details",self)
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
        self.customer_menu.addAction(self.edit_customer)
        self.customer_menu.addAction(self.edit_medical)
        self.customer_menu.addAction(self.add_allergy)
        self.customer_menu.addAction(self.edit_allergy)
        self.customer_menu.addAction(self.delete)
        self.treatment_menu.addAction(self.add_treatmnet)
        self.treatment_menu.addAction(self.edit_treatment)
        self.appointment_menu.addAction(self.new_appointment)
        self.appointment_menu.addAction(self.edit_appointment)
        self.appointment_menu.addAction(self.cancel_appointmnet)
        self.supplier_menu.addAction(self.new_supplier)
        self.supplier_menu.addAction(self.amend_supplier)
        self.supplier_menu.addAction(self.delete_supplier)
        self.product_menu.addAction(self.new_product)
        self.product_menu.addAction(self.ammend_product)
        self.product_menu.addAction(self.delete_product)
        self.order_menu.addAction(self.new_order)
        self.order_menu.addAction(self.amend_order)
        self.order_menu.addAction(self.cancel_order)
        self.admin_menu.addAction(self.create_reports)
        self.admin_menu.addAction(self.backup)
        self.admin_menu.addAction(self.database)
        self.admin_menu.addAction(self.add_user)
        self.admin_menu.addAction(self.edit_user)

        self.setMenuBar(self.menu_bar)

        #connections
        self.new_customer.triggered.connect(self.add_new_customer)
        self.add_treatmnet.triggered.connect(self.add_new_treatment)
        self.reset_central_widget.triggered.connect(self.reset)
        self.new_product.triggered.connect(self.add_new_product)
        self.new_supplier.triggered.connect(self.add_new_supplier)
        
    def add_new_customer(self):
        CustomerWidget = AddCustomer()
        self.setCentralWidget(CustomerWidget)

    def add_new_treatment(self): 
        TreatmentWidget = AddTreatment()
        self.setCentralWidget(TreatmentWidget)

    def add_new_supplier(self):
        SupplierWidget = AddSupplier()
        self.setCentralWidget(SupplierWidget)

    def add_new_product(self):
        ProductWidget = AddProduct()
        self.setCentralWidget(ProductWidget)

    def reset(self):
        self.setCentralWidget(None)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
