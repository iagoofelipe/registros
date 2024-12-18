from PySide6.QtCore import QObject, Signal
from mysql.connector import connect, Error as MysqlConnectorError
from sqlite3 import connect as sqlite_connect
import os
import logging as log
from typing import  Any

from ._events import RegistryEventHandler

class RegistryDatabase(QObject):
    def __init__(self, events:RegistryEventHandler, parent = ...):
        super().__init__(parent)
        self.__events = events
        self.__conn = None
        self.__cursor = None


    def initialize(self) -> bool:
        self.__sqlite_mode = 'REGISTRY_SQLITE' in os.environ
        self.__param = '?' if self.__sqlite_mode else '%s'

        try:
            if self.__sqlite_mode:
                self.__conn = sqlite_connect('database.sqlite3')
            else:
                self.__conn = connect(host='localhost', user='test', password='1234', database='registry')

            self.__cursor = self.__conn.cursor()
        except MysqlConnectorError:
            return False
        
        return True
    
    def authenticate(self, username:str, password:str) -> Any | None:
        self.__cursor.execute(f'SELECT id FROM user WHERE cpf={self.__param} AND password={self.__param}', (username, password))
        result = self.__cursor.fetchone()

        return result[0] if (result is not None) else None

    def getUserDataById(self, userId) -> str | None:
        
        self.__cursor.execute(f'SELECT firstName, lastName FROM user WHERE id={self.__param}', (userId, ))
        result = self.__cursor.fetchone()

        if result is None:
            log.error(f'não foi possível retornar os dados do usuário com id="{userId}"')
            return
        
        return ' '.join(result)