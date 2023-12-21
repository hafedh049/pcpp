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
