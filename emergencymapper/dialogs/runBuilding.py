from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSignal

from . import dzetsaka_dock
from . import settings_dock
from .selectBuildingDialog import Ui_Dialog

class selectBuildingDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(selectBuildingDialog, self).__init__(parent)
        self.ui= Ui_Dialog()
        self.ui.setupUi(self)
#put your remaining function here
