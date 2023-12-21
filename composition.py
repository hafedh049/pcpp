"""
Composition vs Inheritance - two ways to the same destination: Inheritance
So far we've been using and following the inheritance concept when modeling our classes to represent real-life issues. Inheritance is a great concept, one of the most important foundations of object-oriented programming that models a tight relation between two classes: the base class and the derived class, called a subclass.

The result of this relation is a subclass class that inherits all methods and all properties of the base class, and allows a subclass to extend everything that has been inherited. By extending a base class, you are creating a more specialized class. Moreover, we say that these classes are tightly coupled.

Inheritance models what is called an is a relation.
Examples:

a Laptop is a (specialized form of) Computer;
a Square is a (specialized form of) Figure;
a Hovercraft is a Vehicle.
The primary use of inheritance is to reuse the code. If two classes perform similar tasks, we can create a common base class for them, to which we transfer identical methods and properties. This will facilitate testing and potentially increase application reliability in case of changes. In case of any problems, it will also be easier to find the cause of the error.

As a result, your inheriting classes could form a tree.


tree

Note: the hierarchy grows from top to bottom, like tree roots, not branches. The most general, and the widest, class is always at the top (the superclass) while its descendants are located below (the subclasses).

What could be inherited in this “Vehicles” structure?

All classes derived from Vehicles own properties and methods responsible for informing the user of its mileage, starting and stopping the vehicle, fueling, etc. Once you inherit a “mileage” property from the base class, then it is present in all subclasses.

The same principle should apply to the tank() method responsible for fueling every vehicle object, so the polymorphism, another pillar of the OOP allowing you to call the tank() method on every “vehicle” object, is easily achieved.

The inheritance concept is a powerful one, but you should remember that with great power comes great responsibility. When you are reckless, then with the inheritance (especially multiple inheritances) you can create a huge, complex, and hierarchical structure of classes.

This hierarchy would be hard to understand, debug, and extend. This phenomenon is known as the class explosion problem, and is one of the antipatterns of programming.
"""
