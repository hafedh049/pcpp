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

# --------------------------------------------------------------------------------------------

import pickle

a_dict = dict()
a_dict["EUR"] = {"code": "Euro", "symbol": "€"}
a_dict["GBP"] = {"code": "Pounds sterling", "symbol": "£"}
a_dict["USD"] = {"code": "US dollar", "symbol": "$"}
a_dict["JPY"] = {"code": "Japanese yen", "symbol": "¥"}

a_list = ["a", 123, [10, 100, 1000]]

with open("multidata.pckl", "wb") as file_out:
    pickle.dump(a_dict, file_out)
    pickle.dump(a_list, file_out)


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

# ------------------------------------------------------------------

import pickle

with open("multidata.pckl", "rb") as file_in:
    data1 = pickle.load(file_in)
    data2 = pickle.load(file_in)

print(type(data1))
print(data1)
print(type(data2))
print(data2)


"""
Now it’s time to unpickle the contents of the file.

The presented code is quite simple:

we’re importing a pickle module;
the file is opened in binary mode and the file handle is associated with the file;
we consecutively read some portions of data and deserialize it with the load() function;
finally, we examine the type and contents of the objects.
Pay attention to the fact that with the 'pickle' module, you have to remember the order in which the objects were persisted and the deserialization code should follow the same order.
"""

# ----------------------------------------

import pickle

a_list = ["a", 123, [10, 100, 1000]]
bytes = pickle.dumps(a_list)
print("Intermediate object type, used to preserve data:", type(bytes))

# now pass 'bytes' to appropriate driver

# therefore when you receive a bytes object from an appropriate driver you can deserialize it
b_list = pickle.loads(bytes)
print("A type of deserialized object:", type(b_list))
print("Contents:", b_list)


"""
At the beginning of the serialization module, we mentioned that serialized objects could be persisted in a database or sent via a network. This implies another two functions corresponding to the pickle.dumps() and pickle.loads() functions:

pickle.dumps(object_to_be_pickled) – expects an initial object, returns a byte object. This byte object should be passed to a database or network driver to persist the data;
pickle.loads(bytes_object) – expects the bytes object, returns the initial object.
"""
