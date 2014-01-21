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

        #ADD PRODUCT
        def add_new_product(self,details):
                query = QSqlQuery()
                query.prepare("""INSERT INTO Product(Name,Price,Code,SupplierID)
                                  VALUES (?,?,?,?)""")
                query.addBindValue(details['Name'])
                query.addBindValue(details['Price'])
                query.addBindValue(details['Code'])
                query.addBindValue(details['SupplierID'])
                query.exec_()

        #SEARCH PRODUCT
        def find_product_by_id(self,values):
                model = QSqlQueryModel()
                query = QSqlQuery()
                query.prepare("""SELECT * FROM Product WHERE ProductID = ?""")
                query.addBindValue(values[0])
                query.exec_()
                model.setQuery(query)
                return model

        def find_product_by_name(self,values):
                model = QSqlQueryModel()
                query = QSqlQuery()
                query.prepare("""SELECT * FROM Product WHERE Name = ?""")
                query.addBindValue(values[0])
                query.exec_()
                model.setQuery(query)
                return model

        def find_product_by_price(self,values):
                model = QSqlQueryModel()
                query = QSqlQuery()
                query.prepare("""SELECT * FROM Product WHERE Price = ?""")
                query.addBindValue(values[0])
                query.exec_()
                model.setQuery(query)
                return model

        #AMEND PRODUCT
        def get_supplier_name_from_id(self,id_value):
                query = QSqlQuery()
                query.prepare("""SELECT Name
                                 FROM Supplier
                                 WHERE SupplierID = ?""")
                query.addBindValue(id_value)
                query.exec_()
                while query.next():
                        supplier_name = query.value(0)
                return supplier_name

        def amend_product_without_supplier(self,product_id,details):
                query = QSqlQuery()
                query.prepare("""UPDATE Product
                                  SET Name = ?, Price = ?, Code = ?
                                  WHERE ProductID = ?""")
                query.addBindValue(details['Name'])
                query.addBindValue(details['Price'])
                query.addBindValue(details['Code'])
                query.addBindValue(product_id)
                query.exec_()

        #CREATE ORDER
        def current_order_items_model(self):
                model = QSqlRelationalTableModel()
                print(self.db.tables())
                model.setTable(self.db.tables()[9])
                model.setRelation(8,QSqlRelation("Product","ProductID","Price"))
                return model

        def create_order(self,details):
                query = QSqlQuery()
                query.prepare("""INSERT INTO Orders(DateOfOrder,CustomerID,OrderedFromSupplier,Delivered)
                                   VALUES (?,?,?,?)""")
                query.addBindValue(details['DateOfOrder'])
                query.addBindValue(details['CustomerID'])
                query.addBindValue(details['Ordered'])
                query.addBindValue(details['Delivered'])
                query.exec_()

        def add_product_to_order(self,details):
                query = QSqlQuery()
                query.prepare("""INSERT INTO OrderLine(ProductID,OrderID,Quantity)
                                 VALUES (?,?,?)""")
                query.addBindValue(details['ProductID'])
                query.addBindValue(details['OrderID'])
                query.addBindValue(details['Quantity'])
                query.exec_()

        def get_order_id(self,details):
                query = QSqlQuery()
                query.prepare("""SELECT OrderID
                                 FROM Orders
                                 WHERE DateOfOrder = ? AND CustomerID = ?""")
                query.addBindValue(details['DateOfOrder'])
                query.addBindValue(details['CustomerID'])
                query.exec_()
                while query.next():
                        order_id = query.value(0)
                        print (order_id)
                return order_id
                print (order_id)
                
                

        
