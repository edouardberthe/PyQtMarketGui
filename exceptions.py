class NoDataError(Exception):
    pass


class NoStockDataError(NoDataError):

    def __init__(self, stock):
        super().__init__()
        self.stock = stock
