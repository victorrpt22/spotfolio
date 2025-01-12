from flask import Flask
from abc import ABC, abstractmethod


class BaseModule(ABC):
    """
    Abstract base class for all SpotFolio modules
    """
    name: str = "Unamed Module"
    version: str = "0.0.1"

    @abstractmethod
    def register_routes(self, app: Flask):
        """
        Register routes for the module
        Must be implemented by subclasses
        """
        pass

    @abstractmethod
    def initialize(self):
        """
        Optional initialization logic for the module
        Can be overridden by subclasses
        """
        print(f"{self.__class__.__name__} has no specific initialization logic.")
        pass

    def get_section_metadata(self):
        """
        Returns metadata about the module
        """
        return {
            "name": self.name,
            "description": "No description available",
            "icon": "fa fa-cube",
            'route': f'/{self.name.lower()}'
        }
