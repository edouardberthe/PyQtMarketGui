import numpy as np
from numpy import random as rd

from .contract import Contract
from .model import Model


class EulerTimeStepping:

    def __init__(self, Npaths: int, Nsteps: int, contract: Contract):
        self.Npaths = Npaths
        self.Nsteps = Nsteps
        self.contract = contract

    def generate(self, model: Model):
        S = model.zero * np.ones(self.Npaths)
        dt = self.contract.T / self.Nsteps
        for i in range(self.Nsteps):
            S += model.drift(i * dt, S) * dt + model.diffusion(i * dt, S) * rd.normal(0, dt, self.Npaths)
        self.prices = np.exp(- model.mu * self.contract.T) * self.contract.payoff(S)

    def price(self) -> float:
        return self.prices.mean()

    def stderr(self) -> float:
        return self.prices.std() / np.sqrt(self.Npaths)

    def __str__(self):
        return "Euler Price: {}, Standard Error: {}".format(self.price(), self.stderr())
