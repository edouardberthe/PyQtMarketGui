from abc import ABCMeta, abstractmethod

import numpy as np


class Payoff:

    __metaclass__ = ABCMeta

    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError


class StrikedPayoff(Payoff):

    __metaclass__ = ABCMeta

    def __init__(self, strike: float):
        self.strike = strike


class CallPayoff(StrikedPayoff):

    def __call__(self, x: np.ndarray):
        return (x - self.strike)


class PutPayoff(StrikedPayoff):

    def __call__(self, x: np.ndarray):
        return np.max(self.strike - x, 0)
