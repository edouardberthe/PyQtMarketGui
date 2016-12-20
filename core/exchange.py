class Exchange:

    def __init__(self, ticker: str, name: str=None):
        self.ticker = ticker
        self.name = name

    def __str__(self):
        return self.ticker
