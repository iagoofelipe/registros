from PySide6.QtCore import Signal, QObject

class RegistryEventHandler(QObject):
    quitRequired = Signal()
    loginRequired = Signal(dict)
    loginFinished = Signal(bool)

    def __init__(self, parent = ...):
        super().__init__(parent)