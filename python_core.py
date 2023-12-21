"""
The '+' operator is in fact converted to the __add__() method and the len() function is converted to the __len__() method. These methods must be delivered by a class (now it’s clear why we treat classes as blueprints) to perform the appropriate action.
"""

"""
You could ask: how can I know what magic method is responsible for a specific operation?

The answer could be: start with the dir() and help() functions.

The dir() function gives you a quick glance at an object’s capabilities and returns a list of the attributes and methods of the object. When you call dir() on integer 10, you'll get:

>>> dir(10)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__',
 '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
output

The names listed above look somehow familiar, so let's see the details delivered by Python itsel
"""

"""
Now it’s time to get familiar with Python core syntax expressions and their corresponding magic methods. The following tables will help you in situations where you'd like to implement a custom method for a Python core operation, as the tables enumerate the most popular operators and functions that own magic method counterparts. Treat it as a list from a universal map, unrelated to any special data type.

Comparison methods
Function or operator	Magic method	Implementation meaning or purpose
==	__eq__(self, other)	equality operator
!=	__ne__(self, other)	inequality operator
<	__lt__(self, other)	less-than operator
>	__gt__(self, other)	greater-than operator
<=	__le__(self, other)	less-than-or-equal-to operator
>=	__ge__(self, other)	greater-than-or-equal-to operator
Numeric methods
Unary operators and functions
Function or operator	Magic method	Implementation meaning or purpose
+	__pos__(self)	unary positive, like a = +b
-	__neg__(self)	unary negative, like a = -b
abs()	__abs__(self)	behavior for abs() function
round(a, b)	__round__(self, b)	behavior for round() function

Common, binary operators and functions
Function or operator	Magic method	Implementation meaning or purpose
+	__add__(self, other)	addition operator
-	__sub__(self, other)	subtraction operator
*	__mul__(self, other)	multiplication operator
//	__floordiv__(self, other)	integer division operator
/	__div__(self, other)	division operator
%	__mod__(self, other)	modulo operator
**	__pow__(self, other)	exponential (power) operator
Augumented operators and functions
By augumented assignment we should understand a sequence of unary operators and assignments like a += 20

Function or operator	Magic method	Implementation meaning or purpose
+=	__iadd__(self, other)	addition and assignment operator
-=	__isub__(self, other)	subtraction and assignment operator
*=	__imul__(self, other)	multiplication and assignment operator
//=	__ifloordiv__(self, other)	integer division and assignment operator
/=	__idiv__(self, other)	division and assignment operator
%=	__imod__(self, other)	modulo and assignment operator
**=	__ipow__(self, other)	exponential (power) and assignment operator

Type conversion methods
Python offers a set of methods responsible for the conversion of built-in data types.

Function	Magic method	Implementation meaning or purpose
int()	__int__(self)	conversion to integer type
float()	__float__(self)	conversion to float type
oct()	__oct__(self)	conversion to string, containing an octal representation
hex()	__hex__(self)	conversion to string, containing a hexadecimal representation
Object introspection
Python offers a set of methods responsible for representing object details using ordinary strings.

Function	Magic method	Implementation meaning or purpose
str()	__str__(self)	responsible for handling str() function calls
repr()	__repr__(self)	responsible for handling repr() function calls
format()	__format__(self, formatstr)	called when new-style string formatting is applied to an object
hash()	__hash__(self)	responsible for handling hash() function calls
dir()	__dir__(self)	responsible for handling dir() function calls
bool()	__nonzero__(self)	responsible for handling bool() function calls
Object retrospection
Following the topic of object introspection, there are methods responsible for object reflection.

Function	Magic method	Implementation meaning or purpose
isinstance(object, class)	__instancecheck__(self, object)	responsible for handling isinstance() function calls
issubclass(subclass, class)	__subclasscheck__(self, subclass)	responsible for handling issubclass() function calls

Object attribute access
Access to object attributes can be controlled via the following magic methods

Expression example	Magic method	Implementation meaning or purpose
object.attribute	__getattr__(self, attribute)	responsible for handling access to a non-existing attribute
object.attribute	__getattribute__(self, attribute)	responsible for handling access to an existing attribute
object.attribute = value	__setattr__(self, attribute, value)	responsible for setting an attribute value
del object.attribute	__delattr__(self, attribute)	responsible for deleting an attribute
Methods allowing access to containers
Containers are any object that holds an arbitrary number of other objects; containers provide a way to access the contained objects and to iterate over them. Container examples: list, dictionary, tuple, and set.

Expression example	Magic method	Implementation meaning or purpose
len(container)	__len__(self)	returns the length (number of elements) of the container
container[key]	__getitem__(self, key)	responsible for accessing (fetching) an element identified by the key argument
container[key] = value	__setitem__(self, key, value)	responsible for setting a value to an element identified by the key argument
del container[key]	__delitem__(self, key)	responsible for deleting an element identified by the key argument
for element in container	__iter__(self)	returns an iterator for the container
item in container	__contains__(self, item)	responds to the question: does the container contain the selected item?
The list of special methods built-in in Python contains more entities. For more information, refer to https://docs.python.org/3/reference/datamodel.html#special-method-names.

"""


"""
Inheritance and polymorphism — Inheritance is a pillar of OOP
Inheritance is one of the fundamental concepts of object oriented programming, and expresses the fundamental relationships between classes: superclasses (parents) and their subclasses (descendants). Inheritance creates a class hierarchy. Any object bound to a specific level of class hierarchy inherits all the traits (methods and attributes) defined inside any of the superclasses.

This means that inheritance is a way of building a new class, not from scratch, but by using an already defined repertoire of traits. The new class inherits (and this is the key) all the already existing equipment, but is able to add some new features if needed.

Each subclass is more specialized (or more specific) than its superclass. Conversely, each superclass is more general (more abstract) than any of its subclasses. Note that we've presumed that a class may only have one superclass — this is not always true, but we'll discuss this issue more a bit later.
"""

# ------------------------------------------------------------------------------------------------------------------------------

"""
Inheritance and polymorphism — Single inheritance vs. multiple inheritance
There are no obstacles to using multiple inheritance in Python. You can derive any new class from more than one previously defined class.

But multiple inheritance should be used with more prudence than single inheritance because:

a single inheritance class is always simpler, safer, and easier to understand and maintain;
multiple inheritance may make method overriding somewhat tricky; moreover, using the super() function can lead to ambiguity;
it is highly probable that by implementing multiple inheritance you are violating the single responsibility principle;
If your solution tends to require multiple inheritance, it might be a good idea to think about implementing composition.


MRO — Method Resolution Order
The spectrum of issues possibly coming from multiple inheritance is illustrated by a classical problem named the diamond problem, or even the deadly diamond of death. The name reflects the shape of the inheritance diagram — take a look at the picture.

There is the top-most superclass named A;
there are two subclasses derived from A — B and C;
and there is also the bottom-most subclass named D, derived from B and C (or C and B, as these two variants mean different things in Python)
Can you see the diamond there?

Diamond
"""
# ------------------------------------------------------------------------------------------------------------------------------------------
"""
The ambiguity that arises here is caused by the fact that class B and class C are inherited from superclass A, and class D is inherited from both classes B and C. If you want to call the method info(), which part of the code would be executed then?

Python lets you implement such a class hierarchy. Can you guess the output of the code?

class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(B, C):
    pass

D().info()


In the multiple inheritance scenario, any specified attribute is searched for first in the current class. If it is not found, the search continues into the direct parent classes in depth-first level (the first level above), from the left to the right, according to the class definition. This is the result of the MRO algorithm.

In our case:

class D does not define the method info(), so Python has to look for it in the class hierarchy;
class D is constructed in this order:
the definition of class B is fetched;
the definition of class C is fetched;

DRAW THE DFS AND APPLY THE DIAMOND
"""

"https://www.youtube.com/watch?v=PSMYqfMP3Cs"

"ki tebda fama base class 9bal el sub classes el MRO will fail w ki yibda e5er item houwa el base class fa famch mochkla, print(A.mro()) wila A.__mro__ new method(C3 linearization = left to right the go deeper, old method DFS(go deeper then left to right))"


"""
One way to carry out polymorphism is inheritance, when subclasses make use of base class methods, or override them. By combining both approaches, the programmer is given a very convenient way of creating applications, as:

most of the code could be reused and only specific methods are implemented, which saves a lot of development time and improves code quality;
the code is clearly structured;
there is a uniform way of calling methods responsible for the same operations, implemented accordingly for the types.
Remember
You can use inheritance to create polymorphic behavior, and usually that's what you do, but that's not what polymorphism is about.

In the right pane, there is a code implementing both inheritance and polymorphism:

inheritance: class Radio inherits the turn_on() method from its superclass — that is why we see The device was turned on string twice. Other subclasses override that method and as a result we see different lines being printed;
polymorphism: all class instances allow the calling of the turn_on() method, even when you refer to the objects using the arbitrary variable element.
"""

"""
class Device:
    def turn_on(self):
        print('The device was turned on')

class Radio(Device):
    pass

class PortableRadio(Device):
    def turn_on(self):
        print('PortableRadio type object was turned on')

class TvSet(Device):
    def turn_on(self):
        print('TvSet type object was turned on')

device = Device()
radio = Radio()
portableRadio = PortableRadio()
tvset = TvSet()

for element in (device, radio, portableRadio, tvset):
    element.turn_on()

"""

"""
Summary:

polymorphism is used when different class objects share conceptually similar methods (but are not always inherited)
polymorphism leverages clarity and expressiveness of the application design and development;
when polymorphism is assumed, it is wise to handle exceptions that could pop up.

"""
