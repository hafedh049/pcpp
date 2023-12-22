"""
(Note that an assignment statement is being used, so evaluation of the right side of the clause takes precedence over the left side.)

At first, an object (a list in this example) is created in the computer's memory. Now the object has its identity;
then the object is populated with other objects. Now our object has a value;
finally a variable, which you should treat as a label or name binding, is created, and this label refers to a distinct place in the computer memory.
"""


"""
What is that object 'identity'? Why are the object value and label not enough?

The built-in id() function returns the 'identity' of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.

CPython implementation detail: This is the address of the object in the memory. Don’t treat it as an absolute memory address.
"""


"""
This function is rarely used in applications. More often you’ll use it to debug the code or to experiment while copying objects. The side effect of this infrequent use is that some developers forget about its existence and create their own variables titled id to store some kind of identity or identifier.

As a result, a variable called id shadows the genuine function and makes it unreachable in the scope in which the variable has been defined. You should remember to avoid such situations!
"""

# priority = variable -> function
