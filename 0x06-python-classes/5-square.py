#!/usr/bin/python3
"""defines a Square"""


class Square:
    """
    Defines a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with a given size.

        Args:
            size (int): The size of the square.

        """
        self.__size = size 

    @property
    def size(self):
        """
        Getter method for the size property.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size property.

        Args:
            value (int): The new size of the square.

        Raises:
            ValueError: If the provided size is less than 0.
            TypeError: If the provided size is not an integer.

        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size * self.__size

    def my_print(self):
        """prints a square of # based on size """
        if self.__size != 0:
            for i in range(self.size):
                for j in range(self.size):
                    print("#",end='')                   
                print()

        else:
            print()


