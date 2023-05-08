# Bridge pattern

The Bridge Design Pattern is a structural design pattern that decouples an abstraction from its implementation so that they can vary independently. It allows the abstraction and the implementation to change independently of each other.

In the Bridge Pattern, there are two main components:

- Abstraction: This is the interface that the client interacts with. It defines the high-level operations that the client needs.

- Implementation: This is the concrete class that implements the Abstraction interface. It defines the low-level operations that are needed to perform the high-level operations defined in the Abstraction.

Here's an example implementation of the Bridge Pattern in Python:

```py
class Abstraction:
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        pass

class Implementation:
    def operation_implementation(self):
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationA operation implementation"

class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationB operation implementation"

class ConcreteAbstraction(Abstraction):
    def operation(self):
        return f"ConcreteAbstraction operation with {self.implementation.operation_implementation()}"

# client code
implementation_a = ConcreteImplementationA()
abstraction_a = ConcreteAbstraction(implementation_a)
result = abstraction_a.operation()
print(result)

implementation_b = ConcreteImplementationB()
abstraction_b = ConcreteAbstraction(implementation_b)
result = abstraction_b.operation()
print(result)
```

In this example, we have an `Abstraction` abstract class that defines the high-level operations that the client needs. We also have an `Implementation` abstract class that defines the low-level operations that are needed to perform the high-level operations defined in the `Abstraction`.

We then have concrete `ConcreteImplementationA` and `ConcreteImplementationB` classes that implement the `Implementation` interface with their own specific implementations. Finally, we have a `ConcreteAbstraction` class that is a subclass of `Abstraction`. It maintains a reference to an object of the `Implementation` class and uses it to perform the high-level operations.

The client code creates a `ConcreteImplementationA` object and a `ConcreteAbstraction` object, passing the `ConcreteImplementationA` object to the `ConcreteAbstraction` constructor. It then calls the operation method on the `ConcreteAbstraction` object, which in turn calls the `operation_implementation` method on the `ConcreteImplementationA` object and returns a string that is formatted to include the string returned by the `operation_implementation` method.

The client code then creates a `ConcreteImplementationB` object and a `ConcreteAbstraction` object, passing the `ConcreteImplementationB` object to the `ConcreteAbstraction` constructor. It calls the operation method on the `ConcreteAbstraction` object again, which in turn calls the `operation_implementation` method on the `ConcreteImplementationB` object and returns a different string that is formatted to include the string returned by the `operation_implementation` method.

This demonstrates how the `Abstraction` and `Implementation` can vary independently of each other, and how the `ConcreteAbstraction` object can use different `Implementation` objects to perform the high-level operations defined in the `Abstraction`.

--- 

# Example

```py
class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API1.circle at ({x}, {y}) with radius {radius}")

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API2.circle at ({x}, {y}) with radius {radius}")

class CircleShape:
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def resize(self, radius):
        self._radius = radius

# client code
circle1 = CircleShape(1, 2, 3, DrawingAPI1())
circle1.draw()
circle1.resize(5)
circle1.draw()

circle2 = CircleShape(5, 7, 11, DrawingAPI2())
circle2.draw()
```

In this example, we have a `DrawingAPI` abstract class that defines the low-level operations for drawing a circle. We also have concrete `DrawingAPI1` and `DrawingAPI2` classes that implement the `DrawingAPI` interface with their own specific implementations for drawing a circle.

We then have a `CircleShape` class that is a subclass of `DrawingAPI`. It maintains the x, y, and radius values for the circle, and has a reference to an object of the `DrawingAPI` class to perform the low-level drawing operations.

The client code creates two `CircleShape` objects, one with `DrawingAPI1` and the other with `DrawingAPI2`. It calls the draw method on each object to draw the circle using the appropriate low-level drawing operations. It then calls the resize method on the first `CircleShape` object to resize the circle, and calls the draw method again to draw the resized circle. Finally, it calls the draw method on the second `CircleShape` object to draw a circle using the second `DrawingAPI` object.

This demonstrates how the `CircleShape` abstraction and the `DrawingAPI` implementation can vary independently of each other, and how the `CircleShape` object can use different `DrawingAPI` objects to draw a circle.
