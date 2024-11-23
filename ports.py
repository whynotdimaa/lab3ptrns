# ports.py
import json

class Port:
    def __init__(self, id, coordinates):
        self.id = id
        self.coordinates = coordinates
        self.ships = []

    def incoming_ship(self, ship):
        self.ships.append(ship)
        print(f"Ship {ship.id} has arrived at Port {self.id}.")

    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f)

    def to_dict(self):
        return {"id": self.id, "coordinates": self.coordinates, "ships": [ship.to_dict() for ship in self.ships]}

    @staticmethod
    def load_from_json(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return Port(data['id'], tuple(data['coordinates']))

    def refuel(self, ship):
        """Метод для дозаправки корабля в порту"""
        if ship.fuel_level < ship.max_fuel:
            ship.fuel_level = ship.max_fuel
            print(f"Ship {ship.id} refueled to full capacity at Port {self.id}.")
        else:
            print(f"Ship {ship.id} already has full fuel at Port {self.id}.")
