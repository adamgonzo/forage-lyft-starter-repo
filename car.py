
from abc import ABC, abstractmethod
from servicable import Servicable
from battery import Battery
from engine import Engine


class Car(Servicable):
    def __init__(self, engine, battery):
        super().__init__()
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
    