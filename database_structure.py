#Gentle Effects Aesthetics Customer Management System
#Adam D. Olivant (24426@longroad.ac.uk)

#import sqlite3 as a DBMS
import sqlite3

#implementation of the tables in the database.
def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""SELECT name
                          FROM sqlite_master
                          WHERE name =?""",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
            if response == "y":
                keep_table = False
                print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The exisiting table was kept")
            print()
        else:
            keep_table = False 
    if not keep_table:
            cursor.execute(sql)
            db.commit()

#create customer table function
def create_customer_table():
    sql = """CREATE TABLE Customer(
             CustomerID integer,
	     FirstName text,
	     LastName text, 
	     DateOfBirth text,
	     House text,
	     Road text,
	     City text,
	     County text,
	     PostCode text,
	     MobileNum text,
	     HomeNum text, 
	     Preferred text,
	     Email text,
	     PRIMARY KEY (CustomerID))"""
    create_table(db_name,"Customer",sql)

#create medication infomration table fucntion
def create_medical_information_table():
    sql = """CREATE TABLE MedicalInformation(
	     MedicalInfoID integer,
	     CustomerID integer,
	     DateTimeStamp text,
	     MedicalInfoEntry text,
	     PRIMARY KEY (MedicalInfoID),
	     FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID))"""
    create_table(db_name,"MedicalInformation",sql)

#create allergies table function
def create_allergies_table():
    sql = """CREATE TABLE Allergies(
             AllergyID integer,
             AllergyName text,
             PRIMARY KEY (AllergyID))"""
    create_table(db_name,"Allergies",sql)

#create allergies customer table function
def create_allergies_customer_table():
    sql = """CREATE TABLE AllergiesCustomer(
             AllergiesID integer,
             CustomerID integer,
             AllergyID integer,
             PRIMARY KEY (AllergiesID),
             FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
             FOREIGN KEY (AllergyID) REFERENCES Allergies(AllergyID))"""
    create_table(db_name,"AllergiesCustomer",sql)

#create treatment table function
def create_treatment_table():
    sql = """CREATE TABLE Treatment(
             TreatmentID integer,
             Name text,
             Cost real,
             Duration text,
             PRIMARY KEY (TreatmentID))"""
    create_table(db_name,"Treatment",sql)

#create appointment table function
def create_appointment_table():
    sql = """CREATE TABLE Appointment(
             AppointmentID integer,
             AppointmentTime text,
             AppointmentDate text,
             CustomerID integer,
             TreatmentID integer,
             PRIMARY KEY (AppointmentID),
             FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
             FOREIGN KEY (TreatmentID) REFERENCES Treatment(TreatmentID))"""
    create_table(db_name,"Appointment",sql)

#create supplier table function
def create_supplier_table():
    sql = """CREATE TABLE Supplier(
             SupplierID integer,
             Name text,
             House text,
             Road text,
             City text,
             County text,
             PostCode text,
             ContactNum text,
             Email text,
             Website text,
             PRIMARY KEY (SupplierID))"""
    create_table(db_name,"Supplier",sql)

#create product table function
def create_product_table():
    sql = """CREATE TABLE Product(
             ProductID integer,
             Name text,
             Price real,
             Code text,
             SupplierID integer,
             PRIMARY KEY (ProductID),
             FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID))"""
    create_table(db_name,"Product",sql)

#create order table function
def create_order_table():
    sql = """CREATE TABLE Orders(
             OrderID integer,
             DateOfOrder text,
             CustomerID integer,
             OrderedFromSupplier boolean,
             Delivered boolean,
             PRIMARY KEY (OrderID),
             FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID))"""
    create_table(db_name,"Orders",sql)

#create orderline table function
def create_order_line_table():
    sql = """CREATE TABLE OrderLine(
             OrderLineID integer,
             ProductID integer,
             OrderID integer,
             Quantity integer,
             PRIMARY KEY (OrderLineID),
             FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
             FOREIGN KEY (OrderID) REFERENCES Orders(OrderID))"""
    create_table(db_name,"OrderLine",sql)

if __name__ == "__main__":
    db_name = "GentleEffects.db"
    create_customer_table()
    create_medical_information_table()
    create_allergies_table()
    create_allergies_customer_table()
    create_treatment_table()
    create_appointment_table()
    create_supplier_table()
    create_product_table()
    create_order_table()
    create_order_line_table()
