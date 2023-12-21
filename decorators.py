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

"""
