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
