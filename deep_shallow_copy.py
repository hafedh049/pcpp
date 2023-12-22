"""
(Note that an assignment statement is being used, so evaluation of the right side of the clause takes precedence over the left side.)

At first, an object (a list in this example) is created in the computer's memory. Now the object has its identity;
then the object is populated with other objects. Now our object has a value;
finally a variable, which you should treat as a label or name binding, is created, and this label refers to a distinct place in the computer memory.
"""


"""
What is that object 'identity'? Why are the object value and label not enough?

The built-in id() function returns the 'identity' of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.

CPython implementation detail: This is the address of the object in the memory. Don’t treat it as an absolute memory address.
"""


"""
This function is rarely used in applications. More often you’ll use it to debug the code or to experiment while copying objects. The side effect of this infrequent use is that some developers forget about its existence and create their own variables titled id to store some kind of identity or identifier.

As a result, a variable called id shadows the genuine function and makes it unreachable in the scope in which the variable has been defined. You should remember to avoid such situations!
"""

# priority = variable -> function


"""
When you have two variables referring to the same object, the return values of the id() function must be the same.
"""


"""
(Memory Chunks)

What is the difference between the '==' and 'is' operators?

What should you do to compare two objects?

In order to compare two objects, you should start with the '==' operator as usual. This operator compares the values of both operands and checks for value equality. So here we witness a values comparison.

In fact, two distinct objects holding the same values could be compared, and the result would be 'True'. Moreover, when you compare two variables referencing the same object, the result would be also 'True'.

To check whether both operands refer to the same object or not, you should use the 'is' operator. In other words, it responds to the question: “Are both variables referring to the same identity?”
"""

# -------------------------------------------------------------

print("Part 1")
print("Let's make a copy")
a_list = [10, "banana", [997, 123]]
b_list = a_list[:]
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

print()
print("Part 2")
print("Let's modify b_list[2]")
b_list[2][0] = 112
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)


"""
When you process the data, you’ll come to the point where you may want to have distinct copies of objects that you can modify without automatically modifying the original at the same time.

Let's have a look at the following code. Its intention is to:

make a real, independent copy of a_list, (not just a copy reference). Using [:], which is an array slice syntax, we get a fresh copy of the a_list object;
modify the original object;
see the contents of both objects.
Pay attention to the code presented in the right pane, of which a_list is a compound object (an object that contains other objects, like lists, dictionaries, or class instances).

When you run the code, you get the following output:

Part 1
Let's make a copy
a_list contents: [10, 'banana', [997, 123]]
b_list contents: [10, 'banana', [997, 123]]
Is it the same object? False

Part 2
Let's modify b_list[2]
a_list contents: [10, 'banana', [112, 123]]
b_list contents: [10, 'banana', [112, 123]]
Is it the same object? False
output

So, despite the fact that b_list is a copy of a_list, modifying b_list results in a modification of the a_list object.
"""
