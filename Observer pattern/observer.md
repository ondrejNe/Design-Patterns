# Observer pattern (Also known as the Publish-Subscribe Pattern)

The Observer Design Pattern is a behavioral design pattern that defines a one-to-many dependency between objects, so that when one object changes its state, all its dependents are notified and updated automatically. The Observer Pattern promotes loose coupling between objects, allowing for greater flexibility and extensibility in an application.

In the Observer Pattern, there are two main components:

- Subject: This is the object that is being observed. It maintains a list of its observers and notifies them when its state changes.

- Observer: This is the object that is observing the subject. It is notified when the subject's state changes, and can then take appropriate action.

Here's an example implementation of the Observer Pattern in Python:

```py
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

class TemperatureSensor(Subject):
    def __init__(self, temperature=0):
        super().__init__()
        self.temperature = temperature

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify()

class FahrenheitDisplay(Observer):
    def update(self, subject):
        if isinstance(subject, TemperatureSensor):
            temperature = subject.temperature * 1.8 + 32
            print(f"Current temperature: {temperature} F")

class CelsiusDisplay(Observer):
    def update(self, subject):
        if isinstance(subject, TemperatureSensor):
            temperature = subject.temperature
            print(f"Current temperature: {temperature} C")

# client code
temperature_sensor = TemperatureSensor()
fahrenheit_display = FahrenheitDisplay()
celsius_display = CelsiusDisplay()

temperature_sensor.attach(fahrenheit_display)
temperature_sensor.attach(celsius_display)

temperature_sensor.set_temperature(25)
temperature_sensor.set_temperature(30)
```

In this example, we have a `Subject` class that maintains a list of its observers and notifies them when its state changes. We also have an `Observer` class that defines the interface for objects that are observing the subject. We then have a `TemperatureSensor` class that is a subclass of `Subject`. It maintains a temperature value and notifies its observers when the temperature changes. Finally, we have `FahrenheitDisplay` and `CelsiusDisplay` classes that are subclasses of `Observer`. They display the temperature in either Fahrenheit or Celsius when notified of a change in the temperature.

The client code creates a `TemperatureSensor`, a `FahrenheitDisplay`, and a `CelsiusDisplay`. It attaches both displays to the temperature sensor as observers. When the temperature changes, the `TemperatureSensor` object notifies both displays, which then display the updated temperature in their respective units.
