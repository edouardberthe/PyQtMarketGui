import pandas as pd

from .security import Security


class Pair(tuple):

    def __new__(cls, security1: Security, security2: Security):
        return super().__new__(cls, tuple((security1, security2)))

    def data(self):
        return pd.DataFrame(self[0].data, self[1].data)

    def r2(self):
        return self.data
