from __future__ import annotations

from abc import ABC
from typing import Any


class KernelService(ABC):

    def __init__(
        self,
        name: str | None = None,
    ):
        self._name = name or self.__class__.__name__
        self.running = False


    @property
    def name(self):

        if not hasattr(self, "_name"):
            self._name = self.__class__.__name__

        return self._name


    @name.setter
    def name(
        self,
        value
    ):
        self._name = value



    def start(self):

        self.running = True



    def stop(self):

        self.running = False



    def tick(self):
        pass



    def metadata(self):

        return {
            "name": self.name,
            "version": getattr(
                self,
                "version",
                "1.0.0"
            ),
            "enabled": True,
        }