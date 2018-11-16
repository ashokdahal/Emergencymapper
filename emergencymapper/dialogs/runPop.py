from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSignal

from . import dzetsaka_dock
from . import settings_dock
from .selectPopDialog import Ui_Dialog

class selectPopDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(selectPopDialog, self).__init__(parent)
        self.ui= Ui_Dialog()
        self.ui.setupUi(self)

