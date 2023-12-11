import shelve

with shelve.open("test") as shelve:
    shelve["username"] = "Hafedh Gunichi"


with shelve.open("test") as shelve:
    print(shelve["username"])
