class Contract:

    def __init__(self, strike: float, maturity: float, payoff):
        self.strike = strike
        self.maturity = maturity
        self.payoff = payoff(self.strike)

    @property
    def K(self):
        return self.strike

    @property
    def T(self):
        return self.maturity
