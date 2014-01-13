from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class SQL:
    def __init__(self,path):
        self.path = path
        self.db = None

    def open_database(self):
        if self.db:
            self.close_database()

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)
        open_db = self.db.open()

        self.pragma_on = QSqlQuery()
        self.pragma_on.prepare("""PRAGMA foreign_keys = ON""")
        self.pragma_on.exec_()

        return open_db

    def close_database(self):
        pass

    #ADD CUSTOMER
    def add_new_customer(self,details):   
         query = QSqlQuery()
         query.prepare("""INSERT INTO Customer(FirstName,LastName,DateOfBirth,
	                    		   House,Road,City,County,PostCode,
	                    		   MobileNum,HomeNum,Preferred,Email)
	                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""")
	 query.addBindValue(details['FirstName'])
	 query.addBindValue(details['LastName'])
	 query.addBindValue(details['DateOfBirth'])
	 query.addBindValue(details['House'])
	 query.addBindValue(details['Road'])
	 query.addBindValue(details['City'])
	 query.addBindValue(details['County'])
	 query.addBindValue(details['PostCode'])
	 query.addBindValue(details['MobileNum'])
	 query.addBindValue(details['HomeNum'])
         query.addBindValue(details['Preferred'])
	 query.addBindValue(details['Email'])
	 query.exec_()

    #CREATE ORDER
    def current_order_items_model(self):
        model = QSqlRelationalTableModel()
        print(self.db.tables())
        model.setTable(self.db.tables()[10])
        model.setRelation(8,QSqlRelation("Product","ProductID","Price"))
        return model 

        
