from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal, QObject

from ..model._model import RegistryModel
from ..backend._events import RegistryEventHandler
from .UI._login import ViewLogin

class RegistryView(QObject):
    def __init__(self, events:RegistryEventHandler, model:RegistryModel, parent = ...):
        super().__init__(parent)
        self.__events = events
        self.__model = model
        self.__window = QMainWindow()
        vargs = (self.__events, self.__model)

        self.__views = {
            'login': ViewLogin(*vargs)
        }

        self.__window.setMinimumSize(1100, 600)
        self.__window.setWindowTitle('Registros')

    def initialize(self):
        self.__window.setCentralWidget(self.__views['login'].setup())
        self.__window.show()