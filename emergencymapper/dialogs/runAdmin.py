from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSignal

from . import dzetsaka_dock
from . import settings_dock
from .selectAdminDialog import Ui_selectAdminDialog

class selectAdminDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(selectAdminDialog, self).__init__(parent)
        self.ui= Ui_selectAdminDialog()
        self.ui.setupUi(self)
#put your remaining function here

