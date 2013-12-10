from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import os
import re

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

        #Create Menubar
        self.menu_bar = QMenuBar()
        self.customer_menu = self.menu_bar.addMenu("Customers")
        self.treatment_menu = self.menu_bar.addMenu("Treatments")
        self.appointment_menu = self.menu_bar.addMenu("Appointments")
        self.product_menu = self.menu_bar.addMenu("Products")
        self.order_menu = self.menu_bar.addMenu("Orders")
        self.admin_menu = self.menu_bar.addMenu("Administration")
        #Add Actions to the Menu Bar
        self.customer_menu.addAction(self.new_customer)

        self.setMenuBar(self.menu_bar)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()

    
    
    
