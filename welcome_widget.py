from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys
import os

class WelcomeWidget(QWidget):
	"""The opening widget of the system"""

	def __init__(self):
		super().__init__()

		self.welcome_label = QLabel("""<html>
					             <body>
						            <p><span style="font-size:14pt; font-weight:1000;text-align:center;">Welcome to</span></p>
					             </body>
					       </html>""")
		self.logo_image = QPixmap(os.getcwd() + "\gelogo.png")
		self.logo_image.scaled(250,50,Qt.KeepAspectRatio, Qt.FastTransformation)
		self.logo = QLabel()
		self.logo.setPixmap(self.logo_image)
		self.cms_label = QLabel("""<html>
					  <body>
						   <p><span style=
    "font-size:14pt; font-weight:1000;text-align:center;">Customer Management
    System</span></p>
					  </body>
					</html>""")

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.welcome_label)
		#self.layout.addWidget(self.logo)
		self.layout.addWidget(self.cms_label)

		self.setLayout(self.layout)
