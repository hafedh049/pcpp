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
