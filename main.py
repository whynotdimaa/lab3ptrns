# main.py
from ports import Port
from ships import ShipBuilder
from containers import container_factory

def main():
    port1 = Port(1, (50.4501, 30.5234))
    port2 = Port(2, (46.4825, 30.7233))
    port3 = Port(3, (40.7128, -74.0060))

    ship1 = ShipBuilder().set_id(101).set_max_weight(10000).set_fuel_level(10).set_max_fuel(200).build()
    ship2 = ShipBuilder().set_id(102).set_max_weight(15000).set_fuel_level(50).set_max_fuel(150).build()

    container1 = container_factory(3, 1960)
    container2 = container_factory(6, 3320, 'refrigerated')
    container3 = container_factory(2, 4100, 'liquid')

    ship1.load_container(container1)
    ship1.load_container(container2)
    ship1.unload_container(container1)

    print(f"Fuel consumption for Ship {ship1.id}: {ship1.total_consumption()} units")

    port1.incoming_ship(ship1)
    port1.save_to_json('port1_data.json')

    loaded_port = Port.load_from_json('port1_data.json')
    print(f"Loaded Port {loaded_port.id} at coordinates {loaded_port.coordinates}")

    # Тепер спробуємо відправити корабель до портів
    ship1.sailTo(port2, [port1, port2, port3])  # Спроба подорожувати до порту 2
    ship1.sailTo(port3, [port1, port2, port3])  # Спроба подорожувати до порту 3

if __name__ == "__main__":
    main()
