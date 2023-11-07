#!/usr/bin/python3
"""defines  MyInt that inherits int."""


class MyInt(int):
    """ invert int operators == and !=.   """

    def __eq__(self, value):
        """ override   ==  opeartor with !=  behavior """
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
