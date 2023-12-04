class Test:
    def __init__(self) -> None:
        # Define a protected instance attribute starts
        # with single _ it can be called outside the object
        # and its subclasses
        self._protected_attribute

        # Private attributes start with double __ and it can' be
        # called directly from outside the object
        self.__private_attribute


test: Test = Test()
