from PySide6.QtWidgets import QApplication
from typing import Sequence
import logging as log

from ._events import RegistryEventHandler
from ..model._model import RegistryModel
from ..view._view import RegistryView
from ..controller._controller import RegistryController

__all__ = ['RegistryApp']

class RegistryApp(QApplication):
    def __init__(self, args:Sequence[str]=None):
        if args is None:
            super().__init__()
        else:
            super().__init__(args)

        self.__events = RegistryEventHandler(self)
        self.__model = RegistryModel(self.__events, self)
        self.__view = RegistryView(self.__events, self.__model, self)
        self.__controller = RegistryController(self.__events, self.__model, self.__view, self)

    def on_quitRequired(self, by_user:bool):
        if not by_user:
            self.quit()

    def exec(self):
        if not self.__controller.initialize():
            return
    
        super().exec()