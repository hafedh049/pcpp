"""
What are chained exceptions?
Python 3 introduced a very interesting feature called 'Exception chaining' to effectively deal with exceptions.

Imagine a situation where you are already handling an exception and your code incidentally triggers an additional exception. Should your code lose the information about the previous exception? Of course not. So the information should be available to the code following the erroneous code. This is an example of implicit chaining.

Another case pops up when we knowingly wish to handle an exception and translate it to another type of exception. Such a situation is typical when you have a good reason for the unifying behavior of one piece of code to act similarly to another piece of code, like a legacy code. In this situation it would also be nice to keep the details of the former exception. This is an example of explicit chaining.


This chaining concept introduces two attributes of exception instances:

the __context__ attribute, which is inherent for implicitly chained exceptions;
the __cause__ attribute, which is inherent for explicitly chained exceptions.
Those attributes help the programmer to keep a reference to the original exception object in a handy and consistent way for later processing like logging, etc.
"""

# -------------------------------------------

"""

Advanced exceptions - explicitly chained exceptions
This time we'd like to convert an explicit type of exception object to another type of exception object at the moment when the second exception is occurring.

Imagine that your code is responsible for the final checking process before the rocket is launched. The list of checks is a long one, and different checks could result in different exceptions.

But as it is a very serious process, you should be sure that all checks are passed. If any fails, it should be marked in the log book and re-checked next time.
"""

# -------------------------------------------
"""
Advanced exceptions - the traceback attribute
Each exception object owns a __traceback__ attribute.

Python allows us to operate on the traceback details because each exception object (not only chained ones) owns a __traceback__ attribute.
"""

# --------------------------------------------
