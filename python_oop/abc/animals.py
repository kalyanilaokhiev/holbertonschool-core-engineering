#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""creating animal class with subclasses"""


class Animal(ABC):
    """Animal class inherits from ABC"""
    @abstractmethod
    def sound(self):
        pass


def Dog(Animal):
    """Dog sublasses inheriting from Animal"""
    def sound(self):
        return "Bark"


def Cat(Animal):
    """Cat sublasses inheriting from Animal"""
    def sound(self):
        return "Meow"
