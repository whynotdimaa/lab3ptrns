# ships.py
from containers import Container


class Ship:
    def __init__(self, id, max_weight, fuel_level, max_fuel):
        self.id = id
        self.max_weight = max_weight
        self.containers = []
        self.fuel_level = fuel_level  # Додано рівень пального
        self.max_fuel = max_fuel  # Додано максимальний запас пального

    def load_container(self, container):
        if sum(c.weight for c in self.containers) + container.weight <= self.max_weight:
            self.containers.append(container)
            print(f"Container {container.id} loaded into Ship {self.id}.")
        else:
            print(f"Cannot load container {container.id}: weight limit exceeded.")

    def unload_container(self, container):
        if container in self.containers:
            self.containers.remove(container)
            print(f"Container {container.id} unloaded from Ship {self.id}.")
        else:
            print(f"Container {container.id} not found on Ship {self.id}.")

    def total_consumption(self):
        return sum(container.consumption() for container in self.containers)

    def sailTo(self, destination, ports):
        distance = self.get_distance_to_port(destination)

        # Перевірка, чи вистачить пального для подорожі
        if self.fuel_level >= distance:
            self.fuel_level -= distance
            print(f"Sailing to Port {destination.id}... Fuel remaining: {self.fuel_level}")
        else:
            print(f"Not enough fuel to reach Port {destination.id}. Need to refuel.")
            self.refuel(ports)

    def refuel(self, ports):
        # Пошук найближчого порту для дозаправки
        nearest_port = self.find_nearest_port(ports)
        if nearest_port:
            print(f"Refueling at Port {nearest_port.id}...")
            self.fuel_level = self.max_fuel
            print(f"Ship {self.id} refueled to full capacity: {self.fuel_level}.")

    def get_distance_to_port(self, port):
        # Для простоти можна вважати, що відстань між портами є фіксованою
        return 50  # Проста відстань для прикладу

    def find_nearest_port(self, ports):
        # У реальності логіка повинна шукати найближчий порт, тут просто вибираємо перший
        return ports[0]

    def to_dict(self):
        return {"id": self.id, "max_weight": self.max_weight, "fuel_level": self.fuel_level, "max_fuel": self.max_fuel,
                "containers": [c.to_dict() for c in self.containers]}


class ShipBuilder:
    def __init__(self):
        self._ship = Ship(0, 0, 0, 0)

    def set_id(self, id):
        self._ship.id = id
        return self

    def set_max_weight(self, max_weight):
        self._ship.max_weight = max_weight
        return self

    def set_fuel_level(self, fuel_level):
        self._ship.fuel_level = fuel_level
        return self

    def set_max_fuel(self, max_fuel):
        self._ship.max_fuel = max_fuel
        return self

    def build(self):
        return self._ship
