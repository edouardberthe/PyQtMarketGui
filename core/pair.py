import pandas as pd

from .security import Security


class Pair(tuple):

    def __init__(self, security1: Security, security2: Security):
        super().__init__((security1, security2))

    def data(self):
        return pd.DataFrame(self[0].data, self[1].data)

    def r2(self):
        return self.data
