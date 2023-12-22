"""
Introduction to metaclasses
Metaprogramming is a programming technique in which computer programs have the ability to modify their own or other programs’ codes. It may sound like an idea from a science fiction story, but the idea was born and implemented in the early 1960s.

For Python, code modifications can occure while the code is being executed, and you might have already experienced it while implementing decorators, overriding operators, or even implementing the properties protocol.

It may look like syntactic sugar, because in many cases metaprogramming allows programmers to minimize the number of lines of code to express a solution, in turn reducing development time.

But the truth is that this technique could be used for tool preparation; those tools could be applied to your code to make it follow specific programming patterns, or to help you create a coherent API (Application Programming Interface).

Another example of metaprogramming is the metaclass concept, which is one of the most advanced concepts presented in this course.


Tim Peters, the Python guru who authored the Zen of Python, expressed his feelings about metaclasses in the comp.lang.python newsgroup on 12/22/2002:

[metaclasses] are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don't (the people who actually need them know with certainty that they need them, and don't need an explanation about why).

Don’t worry, we'll touch on the “deeper magic” in a benign way. Understanding Python metaclasses is worthwhile, because it leads to a better understanding of what is happening under Python's hood when classes are created.
"""


# -----------------------------


"""
In Python, a metaclass is a class whose instances are classes. Just as an ordinary class defines the behavior of certain objects, a metaclass allows for the customization of class instantiation.

The functionality of the metaclass partly coincides with that of class decorators, but metaclasses act in a different way than decorators:

decorators bind the names of decorated functions or classes to new callable objects. Class decorators are applied when classes are instantiated;
metaclasses redirect class instantiations to dedicated logic, contained in metaclasses. Metaclasses are applied when class definitions are read to create classes, well before classes are instantiated.

Metaclasses usually enter the game when we program advanced modules or frameworks, where a lot of precise automation must be provided.

The typical use cases for metaclasses:

logging;
registering classes at creation time;
interface checking;
automatically adding new methods;
automatically adding new variables.
"""
