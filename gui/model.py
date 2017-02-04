from abc import ABCMeta, abstractproperty
from typing import List

from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt
from PyQt5.QtCore import pyqtSignal

from database import Session


class AbstractTableModel(QAbstractTableModel):

    __metaclass__ = ABCMeta

    message_emitted = pyqtSignal(str)

    def __init__(self, session: Session=Session()):
        super().__init__()
        self.session = session
        self.entities = []
        self.refresh()

    @abstractproperty
    def entity_class(self):
        raise NotImplementedError

    @abstractproperty
    def header(self) -> List[str]:
        raise NotImplementedError

    @abstractproperty
    def cols(self) -> List[str]:
        raise NotImplementedError

    def entity(self, index: QModelIndex):
        return self.entities[index.row()]

    def refresh(self):
        self.entities = self.session.query(self.entity_class).all()

    def data(self, index: QModelIndex, role: int=None):
        if role == Qt.DisplayRole:
            return str(getattr(self.entity(index), self.cols[index.column()]))

    def setData(self, index: QModelIndex, value, role=None):
        setattr(self.entity(index), self.cols[index.column()], value)
        try:
            self.session.commit()
        except Exception as e:
            self.message_emitted.emit('Error during commit: {}'.format(str(e)))
            self.session.rollback()
            return False
        else:
            self.message_emitted.emit('Successful commit')
            return True

    def headerData(self, p_int, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[p_int]

    def columnCount(self, *args, **kwargs):
        return len(self.cols)

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.entities)

    def flags(self, index: QModelIndex):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
