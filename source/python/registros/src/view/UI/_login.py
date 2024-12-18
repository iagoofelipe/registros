from PySide6.QtWidgets import QWidget

from ...model._model import RegistryModel
from ...backend._events import RegistryEventHandler

from .generated.ui_login import Ui_Login

class ViewLogin:
    def __init__(self, events:RegistryEventHandler, model:RegistryModel, *args, **kwargs):
        self.__ui = Ui_Login()
        self.__events = events
        self.__model = model

    def setup(self):
        wid = QWidget()
        self.__ui.setupUi(wid)

        self.__ui.btnLogin.clicked.connect(self.on_btnLogin_Clicked)
        
        return wid
    
    def on_btnLogin_Clicked(self):
        username = self.__ui.lineUsername.text()
        password = self.__ui.linePassword.text()
        data = dict(username=username, password=password)

        if not username or not password:
            print('preencha todos os campos!')
            return

        self.__events.loginRequired.emit(data)