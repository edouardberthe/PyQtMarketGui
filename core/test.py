from core.options import CallPayoff, Contract, EulerTimeStepping, GBMModel

contract = Contract(strike=80, maturity=1, payoff=CallPayoff)
model = GBMModel(zero=100, mu=0.05, sigma=0.3)

euler = EulerTimeStepping(Npaths=1000, Nsteps=100, contract=contract)
euler.generate(model)
print(euler)