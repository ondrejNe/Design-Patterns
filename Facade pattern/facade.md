# Facade pattern

The Facade Design Pattern is a structural design pattern that provides a simple, unified interface to a complex system, making it easier to use and understand. It is used to simplify the interaction with a complex system by providing a single entry point that hides the complexity of the system.

In the Facade Pattern, there are two main components:

- Facade: This is the class that provides a simple, unified interface to the complex system. It delegates the client requests to the appropriate subsystems.

- Subsystem: This is the set of classes that implement the functionality of the complex system. The subsystem classes are not directly accessible by the client; they are accessed through the facade.

Here's an example implementation of the Facade Pattern in Python:

```py
class Subsystem1:
    def operation1(self):
        return "Subsystem1 operation1"

    def operation2(self):
        return "Subsystem1 operation2"

class Subsystem2:
    def operation3(self):
        return "Subsystem2 operation3"

    def operation4(self):
        return "Subsystem2 operation4"

class Facade:
    def __init__(self):
        self.subsystem1 = Subsystem1()
        self.subsystem2 = Subsystem2()

    def operation(self):
        result = []
        result.append(self.subsystem1.operation1())
        result.append(self.subsystem1.operation2())
        result.append(self.subsystem2.operation3())
        result.append(self.subsystem2.operation4())
        return result

# client code
facade = Facade()
result = facade.operation()
print(result)
```

In this example, we have two subsystems, `Subsystem1` and `Subsystem2`, that each have their own set of operations. We also have a `Facade` class that provides a unified interface to the subsystems.

The client code creates a `Facade` object, which in turn creates objects for each of the subsystems. It then calls the operation method on the `Facade` object, which delegates the requests to the appropriate subsystems and returns a list of results from each subsystem operation.

This demonstrates how the `Facade` Pattern simplifies the interaction with a complex system by providing a single entry point that hides the complexity of the system. The client code does not need to know the details of how the subsystems work; it only needs to know the unified interface provided by the facade.
