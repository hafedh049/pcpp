"""
Serialization of Python objects using the pickle module
In this section, you will learn how to persist Python objects for later use.

Pickling is the process of preserving or extending the lifespan of food. The resulting food is called a pickle, and to prevent ambiguity, prefaced with the 'pickled' adjective.jar

Have you ever considered saving the output of your data processing for later use?

The simplest way to persist outcomes is to generate a flat text file and to write your outcomes. It’s a very simple thing to do way which is not suitable for persisting sets of different types of objects or nested structures.
"""


"""
In Python, object serialization is the process of converting an object structure into a stream of bytes to store the object in a file or database, or to transmit it via a network. This byte stream contains all the information necessary to reconstruct the object in another Python script.

This reverse process is called deserialization.

Python objects can also be serialized using a module called 'pickle', and using this module, you can 'pickle' your Python objects for later use.

The 'pickle' module is a very popular and convinient module for data serialization in the world of Pythonistas.

So, what can be pickled and then unpickled?

The following types can be pickled:

None, booleans;
integers, floating-point numbers, complex numbers;
strings, bytes, bytearrays;
tuples, lists, sets, and dictionaries containing pickleable objects;
objects, including objects with references to other objects (remember to avoid cycles!)
references to functions and classes, but not their definitions.
"""
