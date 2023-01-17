import abc
import logging
import pickle

import numpy as np

from myproject.utils import get_logger


class Base(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self._logger = get_logger(self.name, level="info")

    @abc.abstractproperty
    def name(self) -> str:
        """Class name"""

    @property
    def log(self) -> logging.Logger:
        """Access the logger."""
        return self._logger

    @abc.abstractmethod
    def fit(self, X: np.ndarray) -> None:
        """Fit to the data"""

    @abc.abstractmethod
    def transform(self, X: np.ndarray) -> np.ndarray:
        """Transform the data"""

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        return self.fit(X).transform(X)

    def save(self, out: str) -> None:
        """Save the class instance using pickle."""
        with open(out, "wb") as file:
            pickle.dump(self, file, protocol=pickle.HIGHEST_PROTOCOL)
        self.log.info(f"Saved {self.name} to {out}.")

    @classmethod
    def load(cls, inp: str):
        with open(inp, "rb") as file:
            return pickle.load(file)


class StandardScaler(Base):
    def __init__(self) -> None:
        super().__init__()
        self._mean, self._std = None, None

    @property
    def name(self) -> str:
        return "StandardScaler"

    def fit(self, X: np.ndarray) -> "StandardScaler":
        self.log.debug("Fit data")
        self._mean = X.mean()
        self._std = X.std()
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        self.log.debug("Transform data")
        return (X - self._mean) / self._std
