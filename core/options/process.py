from abc import ABCMeta, abstractmethod

import numpy as np


class Process:

    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_step(self, dW: np.array) -> float:
        raise NotImplementedError


class GBM(Process):

    def __init__(self, zero: float, mu: float, sigma: float):
        self.mu = mu
        self.sigma = sigma


class OU(Process):

    def __init__(self, zero: float, kappa: float, theta: float, sigma: float):
        self.kappa = kappa
        self.theta = theta
        self.sigma = sigma
        self.zero = zero
        self.current = zero

    def generate_step(self, dW: np.array) -> float:
        return self.kappa * (self.theta - self.current) + self.sigma * dW


class CIR(Process):

    def __init__(self, zero: float, kappa: float, theta: float, sigma: float):
        self.kappa = kappa
        self.theta = theta
        self.sigma = sigma
        self.zero = zero
        self.current = zero

    def generate_step(self, dW: np.array) -> float:
        return self.kappa * (self.theta - self.current) + self.sigma * np.sqrt(self.current) * dW