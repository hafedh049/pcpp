"""
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
"""

# -------------------------------------------------------
"""
Class: Yfaser an idea, houwa blueprint lil instance
Instance: hia physical instantiation lil class fl memory hedhi eli treferilha el 'self'
Object: more general that instance, object treferi l particular instance of a class
-> fl memory titsama instance, w fl code titsama object
-> 1 class give unlimited instances (oo)
-> kol instance 3andha el state el 5as beha ofc (fl code houwa el variables wl objects)
"""
# --------------------------------------------------------
"""
Ay class yextendi ml 'type' hak aleh ki tji tchouf fl type ta3 class tilgeh 'type'
"""


class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def walk(self):
        pass

    """
    tnajem thot comment w texecuti code kima print w tnajm thot nafs el method kima hia martin wial akther
    maghir maysir hata error hata el oveloading yimchi lina
    """

    def quack(self):
        return print("Quack")


duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

print(Duck.__class__)
print(duckling.__class__)
print(duckling.sex.__class__)
print(duckling.quack.__class__)
print(duckling.walk.__class__)

"""
<class 'type'>
<class '__main__.Duck'>
<class 'str'>
<class 'method'>
"""
