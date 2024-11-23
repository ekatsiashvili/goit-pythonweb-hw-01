from abc import ABC, abstractmethod
from typing import Dict
import logging

# Налаштування логування
logger = logging.getLogger("VehicleLogger")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(message)s")
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


# Абстрактний базовий клас Vehicle
class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make: str = make
        self.model: str = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


# Класи Car та Motorcycle (from Vehicle)
class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")


# Абстрактний клас VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def region_spec(self) -> str:
        pass

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} ({self.region_spec()})")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} ({self.region_spec()})")


# Конкретні фабрики для регіонів
class USVehicleFactory(VehicleFactory):
    def region_spec(self) -> str:
        return "US Spec"


class EUVehicleFactory(VehicleFactory):
    def region_spec(self) -> str:
        return "EU Spec"


class JPVehicleFactory(VehicleFactory):
    def region_spec(self) -> str:
        return "JP Spec"


# Функція для отримання фабрики за регіоном
def get_factory(region: str) -> VehicleFactory:
    factories: Dict[str, VehicleFactory] = {
        "US": USVehicleFactory(),
        "EU": EUVehicleFactory(),
        "JP": JPVehicleFactory(),
    }
    return factories.get(region.upper(), EUVehicleFactory())


if __name__ == "__main__":
    # Використання фабрик
    eu_factory = get_factory("EU")
    vehicle1 = eu_factory.create_car("Ford", "Puma")
    vehicle1.start_engine()

    us_factory = get_factory("US")
    vehicle2 = us_factory.create_car("Tesla", "Model 3")
    vehicle2.start_engine()

    vehicle3 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle3.start_engine()

    jp_factory = get_factory("JP")
    vehicle4 = jp_factory.create_car("Toyota", "Corolla")
    vehicle4.start_engine()

    # Використання фабрики за неіснуючим регіоном (за замовчуванням EU)
    unknown_factory = get_factory("AU")
    vehicle5 = unknown_factory.create_car("Hyundai", "Elantra")
    vehicle5.start_engine()
