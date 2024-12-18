from PySide6.QtCore import Signal, QObject

from ..backend._events import RegistryEventHandler
from ..backend._database import RegistryDatabase

class RegistryModel(QObject):
    def __init__(self, events:RegistryEventHandler, parent = ...):
        super().__init__(parent)
        self.__events = events
        self.__database = RegistryDatabase(events, self)

        self.__events.loginRequired.connect(self.on_loginRequired)

        self.__userId = None

    def initialize(self) -> bool:
        return self.__database.initialize()
    
    def on_loginRequired(self, data:dict):
        username = data['username']
        password = data['username']
        remember = data.get('remember', False)

        result = self.__database.authenticate(username, password)
        success = result is not None
        
        if success:
            self.__userId = result
        
        self.__events.loginFinished.emit(success)

    def getUserData(self):
        return self.__database.getUserDataById(self.__userId)