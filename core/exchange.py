class Exchange:

    def __init__(self, ticker: str, name: str=None):
        self.ticker = ticker
        self.name = name

    def __str__(self):
        return self.ticker

    def __repr__(self):
        return "<Exchange {:s}>".format(str(self))

    def __eq__(self, other):
        return self.ticker == other.ticker
