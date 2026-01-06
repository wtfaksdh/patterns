from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def deliver(self):
        pass


class Car(Transport):
    def deliver(self):
        return "Доставка на машине"


class Bike(Transport):
    def deliver(self):
        return "Доставка на велосипеде"


class TransportFactory(ABC):

    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        return transport.deliver()


class CarFactory(TransportFactory):
    def create_transport(self) -> Transport:
        return Car()


class BikeFactory(TransportFactory):
    def create_transport(self) -> Transport:
        return Bike()


if __name__ == "__main__":
    car_factory = CarFactory()
    bike_factory = BikeFactory()

    print(car_factory.plan_delivery())
    print(bike_factory.plan_delivery())
