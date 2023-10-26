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
<<<<<<< HEAD
         Initializes a new Square instance with a given size.

         Args:
            size (int): The size of the square.

        """

        self.__size = size
=======
        Initializes a new Square instance with a given size.

        Args:
            size (int): The size of the square.

        """
        self.__size = size 
>>>>>>> 7c5b186bd62425b1f4c0cef2376faafb8dc7d987

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
<<<<<<< HEAD
            Setter method for the size property.
=======
        Setter method for the size property.
>>>>>>> 7c5b186bd62425b1f4c0cef2376faafb8dc7d987

        Args:
            value (int): The new size of the square.

        Raises:
            ValueError: If the provided size is less than 0.
            TypeError: If the provided size is not an integer.

        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
<<<<<<< HEAD
        else:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        def area(self):
            """
            Calculates the area of the square.
=======
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Calculates the area of the square.
>>>>>>> 7c5b186bd62425b1f4c0cef2376faafb8dc7d987

        Returns:
            int: The area of the square.

<<<<<<< HEAD
            """
            return self.__size * self.__size

        def my_print(self):
            """prints a square of # based on size """
            if self.__size != 0:
                for i in range(self.size):
                    for j in range(self.size):
                        print("#", end='')
                    print()

                    else:
                        print()
=======
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


>>>>>>> 7c5b186bd62425b1f4c0cef2376faafb8dc7d987
