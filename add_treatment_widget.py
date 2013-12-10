from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import re

class AddTreatment(QWidget):
	"""Adding Treatment to Existing database"""

	def __init__(self):
		super().__init__()

		#self.db = QSqlDatabase.addDatabase("QSQLITE")
		#self.db.setDatabaseName("GentleEffects.db")
		#self.db.open()

		#self.pragma_on = QSqlQuery()
		#self.pragma_on.prepare("""PRAGMA foreign_keys = ON""")
		#self.pragma_on.exec_()

		self.setWindowTitle("Add Treatment | Gentle Effects CMS")

		self.title_label = QLabel("""<html>
					 					 <body>
					       					<p><span style=" font-size:16pt; font-weight:1000;">New Treatment</span></p>
					 					 </body>
				    				 </html>""")

		
		self.information_label = QLabel()
		self.name_label = QLabel("Name of Treatment:")
		self.cost_label = QLabel("Cost of Treatment:")
		self.duration_label = QLabel("Duration of Treatment:")

		self.name_lineedit = QLineEdit()
		self.cost_dblspinbox = QDoubleSpinBox()
		self.cost_dblspinbox.setPrefix("£")
		self.cost_dblspinbox.setSingleStep(0.5)
		self.cost_dblspinbox.setMaximum(500.00)
		self.hour_lineedit = QLineEdit("HH")
		self.hour_lineedit.setMaxLength(2)
		self.hour_lineedit.setFixedWidth(25)
		self.colon_label = QLabel(":")
		self.minuite_lineedit = QLineEdit("MM")
		self.minuite_lineedit.setMaxLength(2)
		self.minuite_lineedit.setFixedWidth(25)

		self.save_pushbutton = QPushButton("Add Treatment")
		self.reset_pushbutton = QPushButton("Reset")

		self.time_layout = QHBoxLayout()
		self.time_layout.addWidget(self.hour_lineedit)
		self.time_layout.addWidget(self.colon_label)
		self.time_layout.addWidget(self.minuite_lineedit)
		self.time_widget = QWidget()
		self.time_widget.setLayout(self.time_layout)

		self.data_layout = QGridLayout()
		self.data_layout.addWidget(self.name_label,0,0)
		self.data_layout.addWidget(self.cost_label,1,0)
		self.data_layout.addWidget(self.duration_label,2,0)
		self.data_layout.addWidget(self.name_lineedit,0,1)
		self.data_layout.addWidget(self.cost_dblspinbox,1,1)
		self.data_layout.addWidget(self.time_widget,2,1)
		self.data_widget = QWidget()
		self.data_widget.setLayout(self.data_layout)

		self.button_layout = QHBoxLayout()
		self.button_layout.addWidget(self.save_pushbutton)
		self.button_layout.addWidget(self.reset_pushbutton)
		self.button_widget = QWidget()
		self.button_widget.setLayout(self.button_layout)

		self.main_layout = QVBoxLayout()
		self.main_layout.addWidget(self.title_label)
		self.main_layout.addWidget(self.information_label)
		self.information_label.hide()
		self.main_layout.addWidget(self.data_widget)
		self.main_layout.addWidget(self.button_widget)

		self.setLayout(self.main_layout)

		#self.setCentralWidget(self.main_widget)

		#Connections
		self.save_pushbutton.clicked.connect(self.save_treatment)
		self.reset_pushbutton.clicked.connect(self.reset)

	def save_treatment(self):
		details = self.treatment_details()
		self.save_to_database = QSqlQuery()
		self.save_to_database.prepare("""INSERT INTO Treatment(Name,Cost,Duration)
										VALUES (?,?,?)""")
		self.save_to_database.addBindValue(details['Name'])
		self.save_to_database.addBindValue(details['Cost'])
		self.save_to_database.addBindValue(details['Duration'])
		self.save_to_database.exec_()
		self.save_pushbutton.setEnabled(False)
		self.information_label.setText("Treatment Added Successfully")
		self.information_label.show()

	def reset(self):
		self.name_lineedit.clear()
		self.cost_dblspinbox.setValue(0)
		self.hour_lineedit.setText("HH")
		self.minuite_lineedit.setText("MM")
		self.save_pushbutton.setEnabled(True)

	def treatment_details(self):
		self.duration = str("{0}:{1}".format(self.hour_lineedit.text(),
									  		 self.minuite_lineedit.text()))
		details = {'Name':self.name_lineedit.text(),
				   'Cost':self.cost_dblspinbox.value(),
				   'Duration':self.duration}
		return details

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = AddTreatment()
    window.show()
    window.raise_()
    application.exec_()
