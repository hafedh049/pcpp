import shelve

with shelve.open("test") as shelvi:
    shelvi["username"] = "Hafedh Gunichi"


with shelve.open("test") as shelvi:
    print(shelvi["username"])

"""
shelve is a module in python that acts like dictionnary but it is persistent it means that it stores data on disk you can call also sync() to synchronize the changes
it has an open method using it with the "with" keyword and it will call .close() automaticaly after the program finishes
it has all the methods of a dictionnary
3 files are created .bak,.dat,.dir
"""


"""
Serialization of Python objects using the shelve module
As you remember, the pickle module is used for serializing objects as a single byte stream. Both serializing and deserializing parties must abide by the order of all the elements placed into a file or database, or sent via a network.

There is another handy module, called shelve, that is built on top of pickle, and implements a serialization dictionary where objects are pickled and associated with a key. The keys must be ordinary strings, because the underlying database (dbm) requires strings.

Therefore, you can open your shelved data file and access your pickled objects via the keys the way you do when you access Python dictionaries. This could be more convenient for you when you’re serializing many objects.
"""
