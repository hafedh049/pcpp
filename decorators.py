"""
A decorator is one of the design patterns that describes the structure of related objects. Python is able to decorate functions, methods, and classes.

The decorator's operation is based on wrapping the original function with a new "decorating" function (or class), hence the name "decoration". This is done by passing the original function (i.e., the decorated function) as a parameter to the decorating function so that the decorating function can call the passed function. The decorating function returns a function that can be called later.

Of course, the decorating function does more, because it can take the parameters of the decorated function and perform additional actions and that make it a real decorating function.

The same principle is applied when we decorate classes. We'll talk about this a bit later.

So from now on, the term 'decorator' will be understood as a decorating class or a decorating function.


Decorators are used to perform operations before and after a call to a wrapped object or even to prevent its execution, depending on the circumstances. As a result, we can change the operation of the packaged object without directly modifying it.

Decorators are used in:

the validation of arguments;
the modification of arguments;
the modification of returned objects;
the measurement of execution time;
message logging;
thread synchronization;
code refactorization;
caching.
"""

"""
Function decorators
Let's analyze some examples before we get down to the next dose of theory.

So, let's create a function – simple_hello() is one of the simplest functions we could think of. We'll decorate it in a moment.

def simple_hello():
    print("Hello from simple function!")


Now let's create another function, simple_decorator(), which is more interesting as it accepts an object as a parameter, displays a __name__ attribute value of the parameter, and returns an accepted object.

def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function


The last lines are responsible for both method invocations:

decorated = simple_decorator(simple_hello)
decorated()

The whole code should look like the code presented in the right pane.

When you run the code, the result should be:

We are about to call "simple_hello"
Hello from simple function!
"""

"""
We have created a simple decorator – a function which accepts another function as its only argument, prints some details, and returns a function or other callable object.

Well … you could say … we wrote so many lines of code just to print two other lines? Where is the simplicity or convenience in this approach?

Well … we could say … you should look at the following syntactic sugar:

As you can see, the definition of the simple_hello() function is literally decorated with '@simple_decorator' – isn't that a nice syntax?

This means that:

operations are performed on object names;
this is the most important thing to remember: the name of the simple_function object ceases to indicate the object representing our simple_function() and from that moment on it indicates the object returned by the decorator, the simple_decorator.
The implementation of the decorator pattern introduces this syntax, which appears to be very important and useful to developers. That is why decorators have gained great popularity and are widely used in Python code. It should be mentioned that decorators are very useful for refactoring or debugging the code.
"""

"""
Decorators should be universal
Consider a function that accepts arguments and should also be decorated. Decorators, which should be universal, must support any function, regardless of the number and type of arguments passed. In such a situation, we can use the *args and **kwargs concepts. We can also employ a closure technique to persist arguments.

The code presented in the right pane shows how the decorator can handle the arguments of the function being decorated.

The output is:

"combiner" was called with the following arguments
    ('a', 'b')
    {'exec': 'yes'}

    Hello from the decorated function; received arguments: ('a', 'b') {'exec': 'yes'}
Decorator is still operating
output

Arguments passed to the decorated function are available to the decorator, so the decorator can print them. This is a simple example, as the arguments were just printed, but not processed further.

A nested function (internal_wrapper) could reference an object (own_function) in its enclosing scope thanks to the closure.
"""

"""
def simple_decorator(own_function):

    def internal_wrapper(*args, **kwargs):
        print('"{}" was called with the following arguments'.format(own_function.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        own_function(*args, **kwargs)
        print('Decorator is still operating')

    return internal_wrapper


@simple_decorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)

combiner('a', 'b', exec='yes')
"""

"""
Decorators can accept their own attributes
In Python, we can create a decorator with arguments. Let’s create a program in which the decorator will be more generic – we’ll allow you to pass the packing material in the argument.

See the code presented in the right pane.

The warehouse_decorator() function created in this way has become much more flexible and universal than 'simple_decorator', because it can handle different materials.

Note that our decorator is enriched with one more function to make it able to handle arguments at all call levels.

The pack_books function will be executed as follows:

the warehouse_decorator('kraft') function will return the wrapper function;
the returned wrapper function will take the function it is supposed to decorate as an argument;
the wrapper function will return the internal_wrapper function, which adds new functionality (material display) and runs the decorated function.
The biggest advantage of decorators is now clearly visible:

we don’t have to change every 'pack' function to display the material being used;
we just have to add a simple one liner in front of each function definition.
"""


def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print(
                "<strong>*</strong> Wrapping items from {} with {}".format(
                    our_function.__name__, material
                )
            )
            our_function(*args)
            print()

        return internal_wrapper

    return wrapper


@warehouse_decorator("kraft")
def pack_books(*args):
    print("We'll pack books:", args)


@warehouse_decorator("foil")
def pack_toys(*args):
    print("We'll pack toys:", args)


@warehouse_decorator("cardboard")
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books("Alice in Wonderland", "Winnie the Pooh")
pack_toys("doll", "car")
pack_fruits("plum", "pear")


"https://www.youtube.com/watch?v=WpF6azYAxYg"


"""
Decorator stacking
Python allows you to apply multiple decorators to a callable object (function, method or class).

The most important thing to remember is the order in which the decorators are listed in your code, because it determines the order of the executed decorators. When your function is decorated with multiple decorators:

@outer_decorator
@inner_decorator
def function():
    pass

abcd = subject_matter_function()


the call sequence will look like the following:

the outer_decorator is called to call the inner_decorator, then the inner_decorator calls your function;
when your function ends it execution, the inner_decorator takes over control, and after it finishes its execution, the outer_decorator is able to finish its job.
This routing mimics the classic stack concept.
"""

# ---------------------------------------------------------------------------------------------------------------------------------------------

"""
Decorating functions with classes
A decorator does not have to be a function. In Python, it could be a class that plays the role of a decorator as a function.

We can define a decorator as a class, and in order to do that, we have to use a __call__ special class method. When a user needs to create an object that acts as a function (i.e., it is callable) then the function decorator needs to return an object that is callable, so the __call__ special method will be very useful.

Our previous example code:

def simple_decorator(own_function):

    def internal_wrapper(*args, **kwargs):
        print('"{}" was called with the following arguments'.format(own_function.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        own_function(*args, **kwargs)
        print('Decorator is still operating')

    return internal_wrapper


could be transcribed to the code presented on the right. Run it to see the output and compare it to the output of the previously retrieved output.

A short explanation of special methods:

the __init__ method assigns a decorated function reference to the self.attribute for later use;
the __call__ method, which is responsible for supporting a case when an object is called, calls a previously referenced function.
The advantage of this approach, when compared to decorators expressed with functions, is:

classes bring all the subsidiarity they can offer, like inheritance and the ability to create dedicated supportive methods.

class SimpleDecorator:
    def __init__(self, own_function):
        self.func = own_function

    def __call__(self, *args, **kwargs):
        print('"{}" was called with the following arguments'.format(self.func.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        self.func(*args, **kwargs)
        print('Decorator is still operating')


@SimpleDecorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)


combiner('a', 'b', exec='yes')
"""

# ------------------------------------------------------------------------------------------------------------------------------------------------

"""
Decorators with arguments
Another previously discussed snippet showed that decorators can accept arguments:

def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print('
* Wrapping items from {} with {}'.format(our_function.__name__, material))
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper
@warehouse_decorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)

And this code could be transcribed to a decorator expressed as a class, presented in the right pane.

When you pass arguments to the decorator, the decorator mechanism behaves quite differently than presented in example of decorator that does not accept arguments (previous slide):

the reference to function to be decorated is passed to __call__ method which is called only once during decoration process,
the decorator arguments are passed to __init__ method


class WarehouseDecorator:
    def __init__(self, material):
        self.material = material

    def __call__(self, own_function):
        def internal_wrapper(*args, **kwargs):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(own_function.__name__, self.material))
            own_function(*args, **kwargs)
            print()
        return internal_wrapper


@WarehouseDecorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)


@WarehouseDecorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@WarehouseDecorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
"""


"""
Decorators with arguments
Another previously discussed snippet showed that decorators can accept arguments:

def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print('
* Wrapping items from {} with {}'.format(our_function.__name__, material))
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper
@warehouse_decorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)

And this code could be transcribed to a decorator expressed as a class, presented in the right pane.

When you pass arguments to the decorator, the decorator mechanism behaves quite differently than presented in example of decorator that does not accept arguments (previous slide):

the reference to function to be decorated is passed to __call__ method which is called only once during decoration process,
the decorator arguments are passed to __init__ method
"""

"""
Class decorators
Class decorators strongly refer to function decorators, because they use the same syntax and implement the same concepts.

Instead of wrapping individual methods with function decorators, class decorators are ways to manage classes or wrap special method calls into additional logic that manages or extends instances that are created.

If we consider syntax, class decorators appear just before the 'class' instructions that begin the class definition (similar to function decorators, they appear just before the function definitions).
"""

"""
Decorators – summary
A decorator is a very powerful and useful tool in Python, because it allows programmers to modify the behavior of a function, method, or class.

Decorators allow us to wrap another callable object in order to extend its behavior.

Decorators rely heavily on closures and *args and **kwargs.

Interesting note:

the idea of decorators was described in two documents – PEP 318 and PEP 3129. Don't be discouraged that the first PEP was prepared for Python 2, because what matters here is the idea, not the implementation in a specific Python.
"""

"""
The name of the parameter self was chosen arbitrarily and you can use a different word, but you must do it consistently in your code. It follows from the convention that self literally means a reference to the instance.
"""
# ----------------------------------------------------------------------------------------------------------------------------------------------------
"""
Class methods
Class methods are methods that, like class variables, work on the class itself, and not on the class objects that are instantiated. You can say that they are methods bound to the class, not to the object.

When can this be useful?

There are several possibilities, here are the two most popular:

we control access to class variables, e.g., to a class variable containing information about the number of created instances or the serial number given to the last produced object, or we modify the state of the class variables;
we need to create a class instance in an alternative way, so the class method can be implemented by an alternative constructor.
Convention

To be able to distinguish a class method from an instance method, the programmer signals it with the @classmethod decorator preceding the class method definition.
Additionally, the first parameter of the class method is cls, which is used to refer to the class methods and class attributes.
As with self, cls was chosen arbitrarily (i.e., you can use a different name, but you must do it consistently).


"""


class Example:
    __internal_counter = 0

    def __init__(self, value):
        Example.__internal_counter += 1

    @classmethod
    def get_internal(cls):
        return "# of objects created: {}".format(cls.__internal_counter)

    def get_internal(self):
        ...
        "instance method ti8lb el class method ki tibda nafs el method(ism)"


print(Example.get_internal())

example1 = Example(10)
print(Example.get_internal())

example2 = Example(99)
print(Example.get_internal())


"An exception is the __init__() method, which by definition is an instance method, so it can’t use “cls”, and as a result it references the class variable by the “Example” prefix."


"""
The code presented in the editor shows how to use the class method as an alternative constructor, allowing you to handle an additional argument.

The including_brand method is a class method, and expects a call with two parameters ('vin' and 'brand'). The first parameter is used to create an object using the standard __init__ method.

In accordance with the convention, the creation of a class object (i.e., calling the __init__ method, among other things) is done using cls(vin).

Then the class method performs an additional task – in this case, it supplements the brand instance variable and finally returns the newly created object.

The result of the presented code:

Ordinary __init__ was called for ABCD1234
Class method was called
Ordinary __init__ was called for DEF567
ABCD1234
DEF567 NewBrand
output

As you can see, for the car with vin=ABCD1234, the __init__ method has been called by default.

For the car with vin=DEF567, the class method has been called, which calls the __init__ method and then performs additional actions and returns the object.

"""


class Car:
    def __init__(self, vin):
        print("Ordinary __init__ was called for", vin)
        self.vin = vin
        self.brand = ""

    @classmethod
    def including_brand(cls, vin, brand):
        print("Class method was called")
        _car = cls(vin)
        _car.brand = brand
        return _car


car1 = Car("ABCD1234")
car2 = Car.including_brand("DEF567", "NewBrand")

print(car1.vin, car1.brand)
print(car2.vin, car2.brand)

# ------------------------------------------------------------------

"""
Static methods
Static methods are methods that do not require (and do not expect!) a parameter indicating the class object or the class itself in order to execute their code.

When can it be useful?

When you need a utility method that comes in a class because it is semantically related, but does not require an object of that class to execute its code;
consequently, when the static method does not need to know the state of the objects or classes.
Convention

To be able to distinguish a static method from a class method or instance method, the programmer signals it with the @staticmethod decorator preceding the class method definition.
Static methods do not have the ability to modify the state of objects or classes, because they lack the parameters that would allow this.

"""


class Bank_Account:
    def __init__(self, iban):
        print("__init__ called")
        self.iban = iban

    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False


# ---------------------------------------------------------------------------
"""
Using static and class methods - comparison
The time has come to compare the use of class and static methods:

a class method requires 'cls' as the first parameter and a static method does not;
a class method has the ability to access the state or methods of the class, and a static method does not;
a class method is decorated by '@classmethod' and a static method by '@staticmethod';
a class method can be used as an alternative way to create objects, and a static method is only a utility method.
"""

# --------------------------------------------------------------------------------

"""
Abstract classes
Python is considered to be a very flexible programming language, but that doesn’t mean that there are no controls to impose a set of functionalities or an order in a class hierarchy. When you develop a system in a group of programmers, it would be useful to have some means of establishing requirements for classes in matters of interfaces (methods) exposed by each class.

What is an abstract class?
An abstract class should be considered a blueprint for other classes, a kind of contract between a class designer and a programmer:

the class designer sets requirements regarding methods that must be implemented by just declaring them, but not defining them in detail. Such methods are called abstract methods.
The programmer has to deliver all method definitions and the completeness would be validated by another, dedicated module. The programmer delivers the method definitions by overriding the method declarations received from the class designer.

This contract assures you that a child class, built upon your abstract class, will be equipped with a set of concrete methods imposed by the abstract class.

Why do we want to use abstract classes?
The very important reason is: we want our code to be polymorphic, so all subclasses have to deliver a set of their own method implementations in order to call them by using common method names.

Furthermore, a class which contains one or more abstract methods is called an abstract class. This means that abstract classes are not limited to containing only abstract methods – some of the methods can already be defined, but if any of the methods is an abstract one, then the class becomes abstract.

What is an abstract method?
An abstract method is a method that has a declaration, but does not have any implementation. We'll give some examples of such methods to emphasize their abstract nature.
"""

# -----------------------------------------------------------------------------------------
"""
Python has come up with a module which provides the helper class for defining Abstract Base Classes (ABC) and that module name is abc.

The ABC allows you to mark classes as abstract ones and distinguish which methods of the base abstract class are abstract. A method becomes abstract by being decorated with an @abstractmethod decorator.

To start with ABC you should:

import the abc module;
make your base class inherit the helper class ABC, which is delivered by the abc module;
decorate abstract methods with @abstractmethod, which is delivered by the abc module.
When you run the code, the output doesn’t surprise anyone:
"""
import abc


class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass


class GreenField(BluePrint):
    def hello(self):
        print("Welcome to Green Field!")


gf = GreenField()
gf.hello()


"""
Multiple inheritance
When you plan to implement a multiple inheritance from abstract classes, remember that an effective subclass should override all abstract methods inherited from its super classes.

Summary:
Abstract Base Class (ABC) is a class that cannot be instantiated. Such a class is a base class for concrete classes;
ABC can only be inherited from;
we are forced to override all abstract methods by delivering concrete method implementations.

A note:

It’s tempting to call a module “abc” and then try to import it, but by doing so Python imports the module containing the ABC class instead of your local file. This could cause some confusion – why does such a common name as “abc” conflict with my simple module “abc”?

Run your own experiment to become familiar with the error messages you would encounter in such a situation.
"""

"""
Attribute encapsulation
Encapsulation is one of the fundamental concepts in object-oriented programming (amongst inheritance, polymorphism, and abstraction). It describes the idea of bundling attributes and methods that work on those attributes within a class.

Encapsulation is used to hide the attributes inside a class like in a capsule, preventing unauthorized parties' direct access to them. Publicly accessible methods are provided in the class to access the values, and other objects call those methods to retrieve and modify the values within the object. This can be a way to enforce a certain amount of privacy for the attributes.

This picture presents the idea: direct access to the object attribute should not be possible, but you can always invoke methods, acting like proxies, to perform some actions on the attributes.

Python introduces the concept of properties that act like proxies to encapsulated attributes.

This concept has some interesting features:

the code calling the proxy methods might not realize if it is "talking" to the real attributes or to the methods controlling access to the attributes;
in Python, you can change your class implementation from a class that allows simple and direct access to attributes to a class that fully controls access to the attributes, and what is most important –consumer implementation does not have to be changed; by consumer we understand someone or something (it could be a legacy code) that makes use of your objects.
"""


"""
Python allows you to control access to attributes with the built-in property() function and corresponding decorator @property.

This decorator plays a very important role:

it designates a method which will be called automatically when another object wants to read the encapsulated attribute value;
the name of the designated method will be used as the name of the instance attribute corresponding to the encapsulated attribute;
it should be defined before the method responsible for setting the value of the encapsulated attribute, and before the method responsible for deleting the encapsulated attribute.
Let's have look at the code in the editor.

We see that every Tank class object has a __level attribute, and the class delivers the methods responsible for handling access to that attribute.

The @property decorated method is a method to be called when some other code wants to read the level of liquid in our tank. We call such a read method getter.

Pay attention to the fact that the method following the decorator gives the name (tank) to the attribute visible outside of the class. Moreover, we see that two other methods are named the same way, but as we are using specially crafted decorators to distinguish them, this won’t cause any problems:

@tank.setter() – designates the method called for setting the encapsulated attribute value;
@tank.deleter() – designates the method called when other code wants to delete the encapsulated attribute.

"""


class TankError(Exception):
    pass


class Tank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__level = 0

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, amount):
        if amount > 0:
            # fueling
            if amount <= self.capacity:
                self.__level = amount
            else:
                raise TankError("Too much liquid in the tank")
        elif amount < 0:
            raise TankError("Not possible to set negative liquid level")

    @level.deleter
    def level(self):
        if self.__level > 0:
            print("It is good to remember to sanitize the remains from the tank!")
        self.__level = None


"""
As those attribute name repetitions could be misleading, let's explain the naming convention:

the getter method is decorated with '@property'. It designates the name of the attribute to be used by the external code;
the setter method is decorated with '@name.setter'. The method name should be the attribute name;
the deleter method is decorated with '@name.deleter'. The method name should should be the attribute name.
Let's instantiate the class and perform some operations on the object's attribute:

As you can see, access to the __level attribute is handled by the designated methods by allowing the other code accessing the 'level' attribute. We can also react to operations when someone wants to break some constraints associated with the tank capacity.

The other code can make use of the 'level' attribute in a convenient way, without even knowing about the logic hidden behind it. So, whenever you'd like to control access to an attribute, you should prepare dedicated properties, because properties control only designated attributes.

It’s worth mentioning another useful and interesting feature of properties: properties are inherited, so you can call setters as if they were attributes.
"""
