import shelve

with shelve.open("test") as shelvi:
    shelvi["username"] = "Hafedh Gunichi"


with shelve.open("test") as shelvi:
    print(shelvi["username"])
