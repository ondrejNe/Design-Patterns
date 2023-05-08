# Prototype pattern

The Prototype Design Pattern is a creational design pattern that allows you to create new objects from existing ones without the need to know their specific classes. It is used to avoid the costly creation of objects by creating copies of existing objects and modifying them as needed.

In the Prototype Pattern, there are two main components:

- Prototype: This is the interface that defines the methods for creating a new object. It specifies the clone method that allows you to create a new object from an existing one.

- ConcretePrototype: This is the class that implements the Prototype interface. It defines the methods for creating a new object and the clone method that creates a copy of an existing object.

Here's an example implementation of the Prototype Pattern in Python:

```py
import copy

class Prototype:
    def clone(self):
        pass

class ConcretePrototypeA(Prototype):
    def __init__(self, value):
        self._value = value

    def clone(self):
        return ConcretePrototypeA(self._value)

    def get_value(self):
        return self._value

class ConcretePrototypeB(Prototype):
    def __init__(self, value):
        self._value = value

    def clone(self):
        return ConcretePrototypeB(self._value)

    def get_value(self):
        return self._value

class PrototypeFactory:
    def __init__(self):
        self._prototypes = {}

    def register_prototype(self, name, prototype):
        self._prototypes[name] = prototype

    def unregister_prototype(self, name):
        del self._prototypes[name]

    def clone(self, name):
        return self._prototypes[name].clone()

# client code
factory = PrototypeFactory()

prototype_a = ConcretePrototypeA(1)
factory.register_prototype("PrototypeA", prototype_a)

prototype_b = ConcretePrototypeB(2)
factory.register_prototype("PrototypeB", prototype_b)

clone_a = factory.clone("PrototypeA")
print(clone_a.get_value())

clone_b = factory.clone("PrototypeB")
print(clone_b.get_value())
```

In this example, we have a `Prototype` abstract class that defines the clone method for creating a new object. We also have concrete `ConcretePrototypeA` and `ConcretePrototypeB` classes that implement the `Prototype` interface and provide the clone method to create a copy of an existing object.

We then have a `PrototypeFactory` class that maintains a list of prototypes and provides the clone method to create new objects from them. The client code creates a `PrototypeFactory` object and registers two `ConcretePrototype` objects with it. It then calls the clone method on the `PrototypeFactory` object to create new objects from the existing prototypes.

This demonstrates how the `Prototype` Pattern allows you to create new objects from existing ones without the need to know their specific classes. You can simply create a copy of an existing object and modify it as needed to create a new object.

---

# Example

```py
import copy

class Prototype:
    def clone(self):
        pass

class Car(Prototype):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class CarFactory:
    def __init__(self):
        self.prototypes = {}

    def register_prototype(self, name, prototype):
        self.prototypes[name] = prototype

    def unregister_prototype(self, name):
        del self.prototypes[name]

    def make_car(self, name):
        if name not in self.prototypes:
            raise ValueError(f"{name} is not a registered prototype")
        return self.prototypes[name].clone()

# client code
car_factory = CarFactory()

car1 = Car("Toyota", "Corolla", 2020)
car_factory.register_prototype("Corolla", car1)

car2 = Car("Honda", "Civic", 2019)
car_factory.register_prototype("Civic", car2)

car3 = car_factory.make_car("Corolla")
print(car3)

car4 = car_factory.make_car("Civic")
car4.year = 2021
print(car4)
```

In this example, we have a `Prototype` abstract class that defines the clone method for creating a new object. We also have a `Car` class that implements the `Prototype` interface and provides the clone method to create a copy of an existing car object.

We then have a `CarFactory` class that maintains a list of car prototypes and provides the make_car method to create new car objects from the existing prototypes. The client code creates a `CarFactory` object and registers two car prototypes with it. It then calls the `make_car` method on the `CarFactory` object to create new car objects from the existing prototypes.

This demonstrates how the `Prototype` Pattern allows you to create new car objects from existing ones without the need to know their specific classes. You can simply create a copy of an existing car object and modify it as needed to create a new car object.
