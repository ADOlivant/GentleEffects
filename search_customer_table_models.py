from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

def find_customer_by_id(self,values):
    model = QSqlQueryModel()
    query = QSqlQuery()
    query.prepare("""SELECT * FROM Customer WHERE CustomerID = ?""")
    query.addBindValue(values[0])
    query.exec_()
    model.setQuery(query)
    return model

def find_customer_by_name(self,values):
    model = QSqlQueryModel()
    query = QSqlQuery()
    query.prepare("""SELECT * FROM Customer WHERE FirstName = ? and LastName = ?""")
    query.addBindValue(values[0])
    query.addBindValue(values[1])
    query.exec_()
    model.setQuery(query)
    return model

def find_customer_by_postcode(self,values):
    model = QSqlQueryModel()
    query = QSqlQuery()
    query.prepare("""SELECT * FROM Customer WHERE PostCode = ?""")
    query.addBindValue(values[1])
    query.exec_()
    model.setQuery(query)
    return model
