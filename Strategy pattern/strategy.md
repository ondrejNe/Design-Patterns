# Strategy pattern

The Strategy Design Pattern is a behavioral design pattern that enables an object to dynamically change its behavior at runtime by encapsulating specific algorithms in separate classes and allowing objects to use these classes interchangeably.

In the Strategy Pattern, there are three main components:

- Context: This is the object that needs to change its behavior. It maintains a reference to a strategy object and delegates its behavior to the strategy.

- Strategy: This is the abstract class or interface that defines the behavior of the algorithm. It has one or more concrete implementations.

- Concrete Strategy: This is the concrete implementation of the strategy interface. It defines the actual algorithm to be executed.

Here's an example implementation of the Strategy Pattern in Python:

```py
class Strategy:
    def do_operation(self, num1, num2):
        pass

class AddStrategy(Strategy):
    def do_operation(self, num1, num2):
        return num1 + num2

class SubtractStrategy(Strategy):
    def do_operation(self, num1, num2):
        return num1 - num2

class MultiplyStrategy(Strategy):
    def do_operation(self, num1, num2):
        return num1 * num2

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, num1, num2):
        return self.strategy.do_operation(num1, num2)

# client code
context = Context(AddStrategy())
result = context.execute_strategy(5, 3)
print(result)

context.strategy = SubtractStrategy()
result = context.execute_strategy(5, 3)
print(result)

context.strategy = MultiplyStrategy()
result = context.execute_strategy(5, 3)
print(result)
```

In this example, we have a `Strategy` abstract class that defines the interface for the strategy. We also have concrete `AddStrategy`, `SubtractStrategy`, and `MultiplyStrategy` classes that implement the strategy interface with their own specific algorithms. Finally, we have a `Context` class that maintains a reference to the current strategy object and delegates its behavior to that object.

The client code creates a `Context` object and initializes it with an `AddStrategy` object. It then executes the `do_operation` method on the `Context` object, which in turn calls the `do_operation` method on the current `Strategy` object (in this case, `AddStrategy`). It prints the result of the operation (in this case, 8).

The client code then changes the `Strategy` object to a `SubtractStrategy` object and executes the operation again, printing the result of the subtraction (in this case, 2).

Finally, the client code changes the `Strategy` object to a `MultiplyStrategy` object and executes the operation again, printing the result of the multiplication (in this case, 15).
