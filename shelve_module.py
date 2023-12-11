import shelve

with shelve.open("test") as shelve:
    shelve["username"] = "Hafedh Gunichi"
