from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSignal

from . import dzetsaka_dock
from . import settings_dock
from .selectHazardDialog import Ui_Dialog

class selectHazardDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(selectHazardDialog, self).__init__(parent)
        self.ui= Ui_Dialog()
        self.ui.setupUi(self)
#put your remaining function here
