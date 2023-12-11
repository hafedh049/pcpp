from typing import override


class Test:
    def __init__(self) -> None:
        # Define a protected instance attribute starts
        # with single _ it can be called outside the object
        # and its subclasses
        self._protected_attribute = 5

        # Private attributes start with double __ and it can' be
        # called directly from outside the object
        self.__private_attribute = 10


# Creation of an instance with type hinting
test: Test = Test()
print(test._protected_attribute)
# Causing AttributeError because it is hidden
print(test._private_attribute)

# ----------------------------------------------------


class Animal:
    def __init__(self) -> None:
        pass

    def speak(self):
        print(...)


class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()

    @override
    def speak():
        print("Hoff")


class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()

    @override
    def speak():
        print("Meow")
