from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Signal, QObject
import logging as log

from ..backend._events import RegistryEventHandler
from ..model._model import RegistryModel
from ..view._view import RegistryView

class RegistryController(QObject):
    def __init__(self, events:RegistryEventHandler, model:RegistryModel, view:RegistryView, app:QApplication):
        super().__init__(app)
        self.__events = events
        self.__model = model
        self.__view = view
        self.__app = app

        # conectando signals e slots
        self.__app.aboutToQuit.connect(self.__events.quitRequired.emit)
        self.__events.loginFinished.connect(lambda x: print(f'login finalizado com {"sucesso" if x else "falha"}'))

    def initialize(self) -> bool:
        if not self.__model.initialize():
            log.error("não foi possível inicializar a aplicação")
            return False
        
        self.__view.initialize()
        return True