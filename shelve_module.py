import shelve

with shelve.open("test") as shelvi:
    shelvi["username"] = "Hafedh Gunichi"


with shelve.open("test") as shelvi:
    print(shelvi["username"])

"""
shelve is a module in python that acts like dictionnary but it is persistent it means that it stores data on disk you can call also sync() to synchronize the changes
it has an open method using it with the "with" keyword and it will call .close() automaticaly after the program finishes
"""
