# SOLID principles

SOLID is an acronym for a set of design principles used in software engineering to create robust and maintainable software. The five principles are:

- Single Responsibility Principle (SRP): A class should have only one reason to change. In other words, a class should have only one responsibility or job to do.

- Open-Closed Principle (OCP): Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification. This means that you should be able to extend the behavior of a software entity without modifying its source code.

- Liskov Substitution Principle (LSP): Subtypes must be substitutable for their base types. This means that if you have a class hierarchy, you should be able to use any subclass in place of its superclass without causing any problems.

- Interface Segregation Principle (ISP): Clients should not be forced to depend on interfaces they do not use. This means that you should design interfaces that are specific to the needs of each client, instead of creating one large interface that is used by all clients.

- Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions. This means that you should design your software so that high-level modules depend on interfaces or abstract classes, instead of depending on the implementation details of low-level modules.

These principles are guidelines that help developers create software that is modular, testable, and easy to maintain over time. By following these principles, developers can create software that is easier to modify, extend, and refactor, which can save time and money over the lifetime of the software.

---

# Examples

Single Responsibility Principle (SRP):

```py
class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
```
In this example, the `Calculator` class has a single responsibility, which is to perform mathematical operations. Each method in the class is focused on a single operation, so if we need to change the behavior of one operation, we don't have to change the entire class.

---

Open-Closed Principle (OCP):

```py
class PaymentProcessor:
    def process_payment(self, payment):
        raise NotImplementedError()

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, payment):
        # process credit card payment
        pass

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, payment):
        # process PayPal payment
        pass
```
In this example, the `PaymentProcessor` class is open for extension because we can create new payment processors that inherit from it and implement the `process_payment` method. However, the class is closed for modification because we don't have to modify its source code to add new payment processors.

---

Liskov Substitution Principle (LSP):

```py
class Vehicle:
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        # start car engine
        pass

class ElectricCar(Car):
    def start_engine(self):
        raise NotImplementedError("Electric cars do not have engines")
```

In this example, the `ElectricCar` class is a subclass of `Car`, which is a subclass of `Vehicle`. The `ElectricCar` class can be used in place of `Car` because it has the same behavior (it can start its engine), even though it doesn't actually have an engine.

---

Interface Segregation Principle (ISP):

```py
class Printable:
    def print_document(self, document):
        pass

class Scanner:
    def scan_document(self):
        pass

class Printer(Printable):
    def print_document(self, document):
        # print the document
        pass

class Copier(Printable, Scanner):
    def print_document(self, document):
        # print the document
        pass
    
    def scan_document(self):
        # scan the document
        pass
```

In this example, we have separate interfaces for printing and scanning. The `Printer` class only implements the `Printable` interface, while the `Copier` class implements both the `Printable` and `Scanner` interfaces.

---

Dependency Inversion Principle (DIP):

```py
class Database:
    def get_data(self):
        pass

class DataProcessor:
    def __init__(self, database):
        self.database = database
    
    def process_data(self):
        data = self.database.get_data()
        # process the data
```

In this example, the `DataProcessor` class depends on an abstraction (`Database`), rather than on the implementation details of a specific database. This allows us to easily switch to a different database implementation without modifying the `DataProcessor` class.
