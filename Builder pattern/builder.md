# Builder patter

The Builder Design Pattern is a creational design pattern that separates the construction of a complex object from its representation, allowing the same construction process to create different representations of the object. It is used to create objects that have many parts or properties, and where the creation process is complex and must be broken down into simpler steps.

In the Builder Pattern, there are four main components:

- Builder: This is the abstract interface that defines the steps for creating a complex object. It specifies the methods for creating and assembling the parts of the object.

- ConcreteBuilder: This is the class that implements the Builder interface. It provides the methods for creating and assembling the parts of the object. Each ConcreteBuilder can create a different representation of the object.

- Director: This is the class that controls the construction process. It uses the Builder interface to build the complex object, but it does not know the specifics of the ConcreteBuilder that is used.

- Product: This is the complex object that is created by the Builder.

Here's an example implementation of the Builder Pattern in Python:

```py
class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def build_part_c(self):
        pass

    def get_result(self):
        pass

class ConcreteBuilder1(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("Part A1")

    def build_part_b(self):
        self.product.add("Part B1")

    def build_part_c(self):
        self.product.add("Part C1")

    def get_result(self):
        return self.product

class ConcreteBuilder2(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("Part A2")

    def build_part_b(self):
        self.product.add("Part B2")

    def build_part_c(self):
        self.product.add("Part C2")

    def get_result(self):
        return self.product

class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print("Product Parts:")
        for part in self.parts:
            print(part)

class Director:
    def construct(self, builder):
        builder.build_part_a()
        builder.build_part_b()
        builder.build_part_c()

# client code
director = Director()

builder1 = ConcreteBuilder1()
director.construct(builder1)
product1 = builder1.get_result()
product1.show()

builder2 = ConcreteBuilder2()
director.construct(builder2)
product2 = builder2.get_result()
product2.show()
```

In this example, we have a `Builder` abstract class that defines the interface for building the parts of the complex object. We also have concrete `ConcreteBuilder1` and `ConcreteBuilder2` classes that implement the `Builder` interface and provide the methods for building the parts of the object.

We then have a `Product` class that represents the complex object that is being built. It has a list of parts that are added by the builders.

Finally, we have a `Director` class that controls the construction process. It uses the `Builder` interface to build the complex object, but it does not know the specifics of the `ConcreteBuilder` that is used.

The client code creates a `Director` object and two `ConcreteBuilder` objects. It passes each `ConcreteBuilder` object to the construct method of the `Director` object, which calls the appropriate methods on the builder to build the parts of the object. It then gets the resulting Product object from the builder and calls the show method to print
