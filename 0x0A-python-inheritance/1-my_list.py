#!/usr/bin/python3
"""
provides a custom list class that allows sorting and printing of lists.
"""


class MyList(list):
    """
    A custom list class that inherits the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
