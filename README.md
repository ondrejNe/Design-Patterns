# DesignPatterns

Design patterns explanation and snippets for learning purposes

## Creational Patterns (5 base patterns)
- Object creation mechanisms that increase flexibility and reuse of existing code.

- Abstract Factory
    - Creates an instance of several families of classes
    - Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
    - `AbstractFactory` declares an interface for operations that create abstract products.
    - `ConcreteFactory` implements the operations to create concrete product objects.
    - `AbstractProduct` declares an interface for a type of product object.
    - `ConcreteProduct` defines a product object to be created by the corresponding concrete factory.
    - `Client` uses only interfaces declared by `AbstractFactory` and `AbstractProduct` classes.

- Builder
    - Separates object construction from its representation
    - Separate the construction of a complex object from its representation so that the same construction process can create different representations.
    - `Builder` specifies an abstract interface for creating parts of a Product object.
    - `ConcreteBuilder` constructs and assembles parts of the product by implementing the Builder interface.
    - `Director` constructs an object using the Builder interface.
    - `Product` represents the complex object under construction. ConcreteBuilder builds the product's internal representation and defines the process by which it's assembled. Includes classes that define the constituent parts, including interfaces for assembling the parts into the final result.

- Factory Method
    - Creates an instance of several derived classes
    - Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.
    - `Product` defines the interface of objects the factory method creates.
    - `ConcreteProduct` implements the Product interface.
    - `Creator` declares the factory method, which returns an object of type Product. Creator may also define a default implementation of the factory method that returns a default ConcreteProduct object. May call the factory method to create a Product object.
    - `ConcreteCreator` overrides the factory method to return an instance of a ConcreteProduct.

- Prototype
    - A fully initialized instance to be copied or cloned
    - Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.
    - `Prototype` declares an interface for cloning itself.
    - `ConcretePrototype` implements an operation for cloning itself.
    - `Client` creates a new object by asking a prototype to clone itself.

- Singleton
    - A class of which only a single instance can exist
    - Ensure a class only has one instance, and provide a global point of access to it.
    - `Singleton` defines an Instance operation that lets clients access its unique instance. Instance is a class operation.
    - `Singleton` may be responsible for creating its own unique instance.

## Structural Patterns (7 base patterns)
- Concerned with how classes and objects are composed to form larger structures.

- Adapter
    - Match interfaces of different classes
    - Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.
    - `Target` defines the domain-specific interface that Client uses.
    - `Client` collaborates with objects conforming to the Target interface.
    - `Adaptee` defines an existing interface that needs adapting.
    - `Adapter` adapts the interface of Adaptee to the Target interface.

- Bridge
    - Separates an object’s interface from its implementation
    - Decouple an abstraction from its implementation so that the two can vary independently.
    - `Abstraction` defines the abstraction's interface.
    - `RefinedAbstraction` extends the interface defined by Abstraction.
    - `Implementor` defines the interface for implementation classes. This interface doesn't have to correspond exactly to Abstraction's interface; in fact the two interfaces can be quite different. Typically the Implementor interface provides only primitive operations, and Abstraction defines higher-level operations based on these primitives.
    - `ConcreteImplementor` implements the Implementor interface and defines its concrete implementation.

- Composite
    - A tree structure of simple and composite objects
    - Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.
    - `Component` declares the interface for objects in the composition.
    - `Leaf` represents leaf objects in the composition. A leaf has no children.
    - `Composite` defines behavior for components having children. Stores child components. Implements child-related operations in the Component interface.
    - `Client` manipulates objects in the composition through the Component interface.

- Decorator
    - Add responsibilities to objects dynamically
    - Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.
    - `Component` defines the interface for objects that can have responsibilities added to them dynamically.
    - `ConcreteComponent` defines an object to which additional responsibilities can be attached.
    - `Decorator` maintains a reference to a Component object and defines an interface that conforms to Component's interface.
    - `ConcreteDecorator` adds responsibilities to the component.

- Facade
    - A single class that represents an entire subsystem
    - Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.
    - `Facade` knows which subsystem classes are responsible for a request. Delegates client requests to appropriate subsystem objects.
    - `Subsystem classes` implement subsystem functionality. Handle work assigned by the Facade object. Have no knowledge of the facade; that is, they keep no references to it.

- Flyweight
    - A fine-grained instance used for efficient sharing
    - Use sharing to support large numbers of fine-grained objects efficiently.
    - `Flyweight` declares an interface through which flyweights can receive and act on extrinsic state.
    - `ConcreteFlyweight` implements the Flyweight interface and adds storage for intrinsic state, if any. A ConcreteFlyweight object must be sharable. Any state it stores must be intrinsic; that is, it must be independent of the ConcreteFlyweight object's context.
    - `UnsharedConcreteFlyweight` not all Flyweight subclasses need to be shared. The Flyweight interface enables sharing, but it doesn't enforce it. It's common for UnsharedConcreteFlyweight objects to have ConcreteFlyweight objects as children at some level in the flyweight object structure (as the Row and Column classes have).
    - `FlyweightFactory` creates and manages flyweight objects. Ensures that flyweights are shared properly. When a client requests a flyweight, the FlyweightFactory object supplies an existing instance or creates one, if none exists.
    - `Client` maintains a reference to flyweight(s). Computes or stores the extrinsic state of flyweight(s).

- Proxy
    - An object representing another object
    - Provide a surrogate or placeholder for another object to control access to it.
    - `Subject` defines the common interface for RealSubject and Proxy so that a Proxy can be used anywhere a RealSubject is expected.
    - `Proxy` maintains a reference that lets the proxy access the real subject. Proxy may refer to a Subject if the RealSubject and Subject interfaces are the same.
    - `RealSubject` defines the real object that the proxy represents.

## Behavioral Patterns (11 base patterns)
- Concerned with algorithms and the assignment of responsibilities between objects.

- Chain of Responsibility
    - A way of passing a request between a chain of objects
    - Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.
    - `Handler` defines an interface for handling requests.
    - `ConcreteHandler` handles requests it is responsible for. Can access its successor. If the ConcreteHandler can handle the request, it does so; otherwise it forwards the request to its successor.
    - `Client` initiates the request to a ConcreteHandler object on the chain.

- Command
    - Encapsulate a command request as an object
    - Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.
    - `Command` declares an interface for executing an operation.
    - `ConcreteCommand` defines a binding between a Receiver object and an action. Implements Execute by invoking the corresponding operation(s) on Receiver.
    - `Client` creates a ConcreteCommand object and sets its receiver.
    - `Invoker` asks the command to carry out the request.
    - `Receiver` knows how to perform the operations associated with carrying out a request. Any class may serve as a Receiver.

- Interpreter
    - A way to include language elements in a program
    - Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.
    - `AbstractExpression` declares an abstract Interpret operation that is common to all nodes in the abstract syntax tree.
    - `TerminalExpression` implements an Interpret operation associated with terminal symbols in the grammar.
    - `NonterminalExpression` one such class is required for every rule R ::= R1R2...Rn in the grammar. Maintains instance variables of type AbstractExpression for each of the symbols R1 through Rn. Implements an Interpret operation for nonterminal symbols in the grammar. Interpret typically calls itself recursively on the variables representing R1 through Rn.
    - `Context` contains information that's global to the interpreter.

- Iterator
    - Sequentially access the elements of a collection
    - Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
    - `Iterator` defines an interface for accessing and traversing elements.
    - `ConcreteIterator` implements the Iterator interface. Keeps track of the current position in the traversal of the aggregate.
    - `Aggregate` defines an interface for creating an Iterator object.
    - `ConcreteAggregate` implements the Iterator creation interface to return an instance of the proper ConcreteIterator.

- Mediator
    - Defines simplified communication between classes
    - Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.
    - `Mediator` defines an interface for communicating with Colleague objects.
    - `ConcreteMediator` implements cooperative behavior by coordinating Colleague objects. Knows and maintains its colleagues.
    - `Colleague` defines an interface for communicating with other Colleague objects through its Mediator.
    - `ConcreteColleague` each Colleague class knows its Mediator object. Each colleague communicates with its mediator whenever it would have otherwise communicated with another colleague.

- Memento
    - Capture and restore an object's internal state
    - Without violating encapsulation, capture and externalize an object's internal state so that the object can be restored to this state later.
    - `Memento` stores internal state of the Originator object. The memento may store as much or as little of the originator's internal state as necessary at its originator's discretion.
    - `Originator` creates a memento containing a snapshot of its current internal state.
    - `Caretaker` is responsible for the memento's safekeeping. Never operates on or examines the contents of a memento.

- Observer
    - A way of notifying change to a number of classes
    - Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
    - `Subject` knows its observers. Any number of Observer objects may observe a subject.
    - `Observer` defines an updating interface for objects that should be notified of changes in a subject. 
    - `ConcreteSubject` stores state of interest to ConcreteObserver objects. Sends a notification to its observers when its state changes.
    - `ConcreteObserver` maintains a reference to a ConcreteSubject object. Stores state that should stay consistent with the subject's. Implements the Observer updating interface to keep its state consistent with the subject's.
    - `Client` creates ConcreteSubject and ConcreteObserver objects. Registers observers with subjects.

- State
    - Alter an object's behavior when its state changes
    - Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
    - `Context` defines the interface of interest to clients. Maintains an instance of a ConcreteState subclass that defines the current state.
    - `State` defines an interface for encapsulating the behavior associated with a particular state of the Context.
    - `ConcreteState` each subclass implements a behavior associated with a state of Context.

- Strategy
    - Encapsulates an algorithm inside a class
    - Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
    - `Strategy` declares an interface common to all supported algorithms. Context uses this interface to call the algorithm defined by a ConcreteStrategy.
    - `ConcreteStrategy` implements the algorithm using the Strategy interface.
    - `Context` is configured with a ConcreteStrategy object. Maintains a reference to a Strategy object. May define an interface that lets Strategy access its data.

- Template Method
    - Defer the exact steps of an algorithm to a subclass
    - Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
    - `AbstractClass` defines abstract primitive operations that concrete subclasses define to implement steps of an algorithm. Implements a template method defining the skeleton of an algorithm. The template method calls primitive operations as well as operations defined in AbstractClass or those of other objects.
    - `ConcreteClass` implements the primitive operations ot carry out subclass-specific steps of the algorithm.

- Visitor
    - Defines a new operation to a class without change
    - Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.
