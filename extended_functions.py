"""
Extended function argument syntax
When we talk about function arguments, we should recall the following facts:

some functions can be invoked without arguments;
functions may require a specific number of arguments with no exclusions; we have to pass a required number of arguments in an imposed order to follow function definition;
functions might have already defined default values for some parameters, so we do not have to pass all arguments as missing arguments, complete with defaults; parameters with default values are presented as keyword parameters;
we can pass arguments in any order if we are assigning keywords to all argument values, otherwise positional ones are the first ones on the arguments list.
"""

"""
These two special identifiers (named *args and **kwargs) should be put as the last two parameters in a function definition. Their names could be changed because it is just a convention to name them 'args' and 'kwargs', but it’s more important to sustain the order of the parameters and leading asterisks.

Those two special parameters are responsible for handling any number of additional arguments (placed next after the expected arguments) passed to a called function:

*args – refers to a tuple of all additional, not explicitly expected positional arguments, so arguments passed without keywords and passed next after the expected arguments. In other words, *args collects all unmatched positional arguments;
**kwargs (keyword arguments) – refers to a dictionary of all unexpected arguments that were passed in the form of keyword=value pairs. Likewise, **kwargs collects all unmatched keyword arguments.
In Python, asterisks are used to denote that args and kwargs parameters are not ordinary parameters and should be unpacked, as they carry multiple items.

If you’ve ever programmed in the C or C++ languages, then you should remember that the asterisk character has another meaning (it denotes a pointer) which could be misleading for you.
"""

"""
The last example in this section shows how to combine *args, a key word, and **kwargs in one definition:

def combiner(a, b, *args, c=20, **kwargs):
    super_combiner(c, *args, **kwargs)
def super_combiner(my_c, *my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_c:', my_c)
    print('my_kwargs', my_kwargs)
combiner(1, '1', 1, 1, c=2, argument1=1, argument2='1')


Result:

my_args: (1, 1)
my_c: 2
my_kwargs {'argument1': 1, 'argument2': '1'}
"""
