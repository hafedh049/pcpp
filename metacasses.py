"""
Introduction to metaclasses
Metaprogramming is a programming technique in which computer programs have the ability to modify their own or other programs’ codes. It may sound like an idea from a science fiction story, but the idea was born and implemented in the early 1960s.

For Python, code modifications can occure while the code is being executed, and you might have already experienced it while implementing decorators, overriding operators, or even implementing the properties protocol.

It may look like syntactic sugar, because in many cases metaprogramming allows programmers to minimize the number of lines of code to express a solution, in turn reducing development time.

But the truth is that this technique could be used for tool preparation; those tools could be applied to your code to make it follow specific programming patterns, or to help you create a coherent API (Application Programming Interface).

Another example of metaprogramming is the metaclass concept, which is one of the most advanced concepts presented in this course.


Tim Peters, the Python guru who authored the Zen of Python, expressed his feelings about metaclasses in the comp.lang.python newsgroup on 12/22/2002:

[metaclasses] are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don't (the people who actually need them know with certainty that they need them, and don't need an explanation about why).

Don’t worry, we'll touch on the “deeper magic” in a benign way. Understanding Python metaclasses is worthwhile, because it leads to a better understanding of what is happening under Python's hood when classes are created.
"""


# -----------------------------


"""
In Python, a metaclass is a class whose instances are classes. Just as an ordinary class defines the behavior of certain objects, a metaclass allows for the customization of class instantiation.

The functionality of the metaclass partly coincides with that of class decorators, but metaclasses act in a different way than decorators:

decorators bind the names of decorated functions or classes to new callable objects. Class decorators are applied when classes are instantiated;
metaclasses redirect class instantiations to dedicated logic, contained in metaclasses. Metaclasses are applied when class definitions are read to create classes, well before classes are instantiated.

Metaclasses usually enter the game when we program advanced modules or frameworks, where a lot of precise automation must be provided.

The typical use cases for metaclasses:

logging;
registering classes at creation time;
interface checking;
automatically adding new methods;
automatically adding new variables.
"""

for t in (int, list, type):
    print(type(t))

"""
In Python's approach, everything is an object, and every object has some type associated with it. To get the type of any object, make use of the type() function.

Run the code in the right pane to see the type() function in action.

<class 'int'>
<class 'list'>
<class '__main__.Dog'>
<class 'type'>
output


We can see that objects in Python are defined by their inherent classes.

The example also shows that we can create our own classes, and those classes will be instances of the type special class, which is the default metaclass responsible for creating classes.

Let's perform one more experiment that will respond to the question: what type of objects are built-in classes and the metaclass type?

for t in (int, list, type):
    print(type(t))


The results are quite interesting:






These observations lead us to the following conclusions:

metaclasses are used to create classes;
classes are used to create objects;
the type of the metaclass type is type – no, that is not a typo.
"""


"""
To extend the above observations, it’s important to add:

type is a class that generates classes defined by a programmer;
metaclasses are subclasses of the type class.
Before we start creating our own metaclasses, it’s important to understand some more details regarding classes and the process of creating them.
"""

"""
We should get familiar with some special attributes:

__name__ – inherent for classes; contains the name of the class;
__class__ – inherent for both classes and instances; contains information about the class to which a class instance belongs;
__bases__ – inherent for classes; it’s a tuple and contains information about the base classes of a class;
__dict__ – inherent for both classes and instances; contains a dictionary (or other type mapping object) of the object's attributes.
The output of the code presented in the right pane:

"dog" is an object of class named: Dog

class "Dog" is an instance of: <class 'type'>
instance "dog" is an instance of: <class '__main__.Dog'>

class "Dog" is   (<class 'object'>,)

class "Dog" attributes: {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None}

object "dog" attributes: {}
"""

# ------------------------------------------------

"""
The same information stored in __class__could be retrieved by calling a type() function with one argument:

for element in (1, 'a', True):
    print(element, 'is', element.__class__, type(element))


The results are:

1 is <class 'int'> <class 'int'>
a is <class 'str'> <class 'str'>
True is <class 'bool'> <class 'bool'>
"""
