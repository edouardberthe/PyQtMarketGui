from abc import ABCMeta, abstractmethod

from .process import CIR


class Model:

    __metaclass__ = ABCMeta

    @abstractmethod
    def drift(self, t: float, state) -> float:
        raise NotImplementedError

    @abstractmethod
    def diffusion(self, t: float, state) -> float:
        raise NotImplementedError


class GBMModel(Model):

    def __init__(self, zero: float, mu:float, sigma: float):
        self.zero = zero
        self.mu = mu
        self.sigma = sigma

    def drift(self, *args, **kwargs):
        return self.mu

    def diffusion(self, *args, **kwargs):
        return self.sigma


class Heston(Model):

    def __init__(self, zero: float, sigma: CIR):
        self.zero = zero
        self.sigma = sigma
