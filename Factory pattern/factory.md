# Factory design pattern

The Factory Design Pattern is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. The Factory Pattern encapsulates the object creation logic, making it easier to manage object creation and ensuring that objects are created with the correct configuration and dependencies.

There are several variations of the Factory Pattern, including:

- Simple Factory Pattern: In this pattern, a factory class has a method that creates and returns objects based on a set of inputs. The client class uses the factory method to create objects, but is not responsible for knowing how to create them.

- Method Factory Pattern: In this pattern, the factory method is an abstract method defined in a superclass. Each subclass of the superclass provides its own implementation of the factory method to create objects specific to that subclass.

- Abstract Factory Pattern: In this pattern, a factory class creates objects that belong to a family of related objects. The factory class provides an interface for creating objects, but the specific type of object created depends on the concrete factory subclass that is used.

Here's an example of each type of factory pattern:

## Simple Factory Pattern:

```py
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Invalid animal type: {animal_type}")

# client code
animal_factory = AnimalFactory()
dog = animal_factory.create_animal("dog")
cat = animal_factory.create_animal("cat")
print(dog.speak())
print(cat.speak())
```

In this example, we have an abstract `Animal` class and concrete `Dog` and `Cat` subclasses. We also have an `AnimalFactory` class that creates `Dog` and `Cat` objects based on a string input. The client code uses the `AnimalFactory` class to create `Dog` and `Cat` objects without knowing the specific details of their creation.

## Method Factory Pattern:

```py
class Document:
    def create_pages(self):
        pass

class Resume(Document):
    def create_pages(self):
        return [ExperiencePage(), EducationPage(), SkillsPage()]

class Report(Document):
    def create_pages(self):
        return [IntroductionPage(), ResultsPage(), ConclusionPage()]

# client code
class DocumentCreator:
    def create_document(self):
        document = self.create_document_type()
        pages = document.create_pages()
        return (document, pages)

class ResumeCreator(DocumentCreator):
    def create_document_type(self):
        return Resume()

class ReportCreator(DocumentCreator):
    def create_document_type(self):
        return Report()

resume_creator = ResumeCreator()
resume, resume_pages = resume_creator.create_document()
report_creator = ReportCreator()
report, report_pages = report_creator.create_document()
```

In this example, we have an abstract `Document` class and concrete `Resume` and `Report` subclasses. Each subclass provides its own implementation of the `create_pages` method to create a specific type of document. We also have an abstract `DocumentCreator` class with an abstract `create_document_type` method. Each concrete `DocumentCreator` subclass provides its own implementation of the `create_document_type` method to create a specific type of document. The client code uses the `ResumeCreator` and `ReportCreator` classes to create `Resume` and `Report` objects without knowing the specific details of their creation.

## Abstract Factory Pattern:

```py
class AbstractShapeFactory:
    def create_circle(self):
        pass

    def create_rectangle(self):
        pass

class RedShapeFactory(AbstractShapeFactory):
    def create_circle(self):
        return RedCircle()

    def create_rectangle(self):
        return RedRectangle()

class BlueShapeFactory(AbstractShapeFactory):
    def create_circle(self):
        return BlueCircle()

    def create_rectangle(self):
        return BlueRectangle()

class Circle:
    def draw(self):
        pass

class Rectangle:
    def draw(self):
        pass

class RedCircle(Circle):
    def draw(self):
        return "Drawing red circle"

class BlueCircle(Circle):
    def draw(self):
        return "Drawing blue circle"

class RedRectangle(Rectangle):
    def draw(self):
        return "Drawing red rectangle"

class BlueRectangle(Rectangle):
    def draw(self):
        return "Drawing blue rectangle"

# client code
red_factory = RedShapeFactory()
red_circle = red_factory.create_circle()
red_rectangle = red_factory.create_rectangle()
print(red_circle.draw())
print(red_rectangle.draw())

blue_factory = BlueShapeFactory()
blue_circle = blue_factory.create_circle()
blue_rectangle = blue_factory.create_rectangle()
print(blue_circle.draw())
print(blue_rectangle.draw())
```

In this example, we have an abstract `AbstractShapeFactory` class that provides an interface for creating circles and rectangles. We also have two concrete `RedShapeFactory` and `BlueShapeFactory` subclasses that create red and blue shapes respectively. Each concrete subclass provides its own implementation of the `create_circle` and `create_rectangle` methods to create the specific type of shape. We also have abstract `Circle` and `Rectangle` classes, and concrete `RedCircle`, `BlueCircle`, `RedRectangle`, and `BlueRectangle` subclasses that provide implementations of the draw method to draw a specific type of shape. The client code uses the `RedShapeFactory` and `BlueShapeFactory` classes to create `Circle` and `Rectangle` objects without knowing the specific details of their creation.
