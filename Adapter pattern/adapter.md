# Adapter pattern

The Adapter Design Pattern is a structural design pattern that allows objects with incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces by converting the interface of one object so that it can be used by another object.

In the Adapter Pattern, there are three main components:

- Target: This is the interface that the client expects to work with. It defines the methods that the client can use to interact with the adapter.

- Adapter: This is the class that adapts the interface of the adaptee to the target interface. It implements the target interface and holds a reference to an object of the adaptee.

- Adaptee: This is the class that has the interface that needs to be adapted to the target interface.

Here's an example implementation of the Adapter Pattern in Python:

```py
class Target:
    def request(self):
        pass

class Adaptee:
    def specific_request(self):
        return "Adaptee specific request"

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: {self.adaptee.specific_request()}"

# client code
adaptee = Adaptee()
adapter = Adapter(adaptee)

result = adapter.request()
print(result)
```

In this example, we have a `Target` abstract class that defines the interface that the client expects to work with. We also have an `Adaptee` class that has a different interface than the `Target` interface. Finally, we have an `Adapter` class that adapts the `Adaptee` interface to the `Target` interface by holding a reference to an `Adaptee` object and implementing the `Target` interface.

The client code creates an `Adaptee` object and an `Adapter` object, passing the `Adaptee` object to the `Adapter` constructor. It then calls the request method on the `Adapter` object, which in turn calls the `specific_request` method on the `Adaptee` object and returns a string that is formatted to include the string returned by the `specific_request` method. The client code then prints the result of the request method (in this case, "Adapter: Adaptee specific request"), demonstrating how the `Adaptee` interface has been adapted to the `Target` interface through the `Adapter` class.
