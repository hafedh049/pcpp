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
# ----------------------------------------
"""
Instance variables
This kind of variable exists when and only when it is explicitly created and added to an object. This can be done during the object's initialization, performed by the __init__ method, or later at any moment of the object's life. Furthermore, any existing property can be removed at any time.

Each object carries its own set of variables – they don't interfere with one another in any way. The word instance suggests that they are closely connected to the objects (which are class instances), not to the classes themselves. To get access to the instance variable, you should address the variable in the following way: objectdotvariable_name.
"""

# ----------------------------------------------------------

# Another snippet shows that instance variables can be created during any moment of an object's life. Moreover, it lists the contents of each object, using the built-in __dict__ property that is present for every Python object.


class Demo:
    def __init__(self, value):
        self.instance_var = value


d1 = Demo(100)
d2 = Demo(200)

d1.another_var = "another variable in the object"

print("contents of d1:", d1.__dict__)
print("contents of d2:", d2.__dict__)

# contents of d1: {'instance_var': 100, 'another_var': 'another variable in the object'}
# contents of d2: {'instance_var': 200}

# ----------------------------------------------------------

"instance variable mayithatou fl dict ken maysirlhom el appel w tantque el init hia theni dunder(magic) method ysirlha el appel implicitement ba3ed el 'NEW' donc bch yitsan3ou el vars w bch yithatou dl __dict__ wial kif tajoutehom ba3ed explictly kima x.a = 5"

# -------------------------------------------------------------

# Class variables
# Class variables are defined within(outside init) the class construction, so these variables are available before any class instance is created. To get access to a class variable, simply access it using the class name, and then provide the variable name.


class Demo:
    class_var = "shared variable"


print(Demo.class_var)
print(Demo.__dict__)

"""
-> el dict fih el entities lkol ta3 el class kima el attribute __module__ eli ki teprintih fi nafs el fichier eli tisna3 feha l classe ta3tik __main__ sinon taatik ism el fichier(module)
-> attribute 'class_var':... houwa key value pair ta3 el class variable
-> najmou nista3mlohom mithel bch na3mlou tracking lil number of instances created
-> all class variables are shared by all class instances (ya3ni tnajm tnadih ml instance zeda) ama makch bch tilgeh fl __dict__ 5atrou mahouwa tabe3 lil instance
"""


class Demo:
    class_var = "shared variable"


d1 = Demo()
d2 = Demo()

print(Demo.class_var)
print(d1.class_var)
print(d2.class_var)

print("contents of d1:", d1.__dict__)

"""
When you want to set or change a value of the class variable, you should access it via the class, but not the class instance, as you can do for reading.

When you try to set a value for the class variable using the object (a variable referring to the object or self keyword) but not the class, you are creating an instance variable that holds the same name as the class variable. The following snippet shows such a case – remember this in order to avoid wasting time hunting for bugs!
"""

# ---------------------------------------------------------------------
