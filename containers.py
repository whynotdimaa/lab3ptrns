# containers.py
from abc import ABC, abstractmethod

class Container(ABC):
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight

    @abstractmethod
    def consumption(self):
        pass

    def to_dict(self):
        return {"type": self.__class__.__name__, "id": self.id, "weight": self.weight}

    @staticmethod
    def from_dict(data):
        container_classes = {"BasicContainer": BasicContainer, "HeavyContainer": HeavyContainer,
                             "RefrigeratedContainer": RefrigeratedContainer, "LiquidContainer": LiquidContainer}
        return container_classes[data["type"]](data['id'], data['weight'])

class BasicContainer(Container):
    UNIT_CONSUMPTION = 2.5
    def consumption(self):
        return self.UNIT_CONSUMPTION * self.weight

class HeavyContainer(Container):
    UNIT_CONSUMPTION = 3.0
    def consumption(self):
        return self.UNIT_CONSUMPTION * self.weight

class RefrigeratedContainer(Container):
    UNIT_CONSUMPTION = 3.5
    def consumption(self):
        return self.UNIT_CONSUMPTION * self.weight

class LiquidContainer(Container):
    UNIT_CONSUMPTION = 4.0
    def consumption(self):
        return self.UNIT_CONSUMPTION * self.weight

def container_factory(id, weight, type_='basic'):
    container_types = {
        'refrigerated': RefrigeratedContainer,
        'liquid': LiquidContainer,
        'basic': BasicContainer if weight <= 3000 else HeavyContainer
    }
    return container_types.get(type_, BasicContainer)(id, weight)
