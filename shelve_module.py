import shelve

with shelve.open("test") as shelvi:
    shelvi["username"] = "Hafedh Gunichi"


with shelve.open("test") as shelvi:
    print(shelvi["username"])

"""
shelve is a module in python that acts like dictionnary but it is persistent it means that
"""
