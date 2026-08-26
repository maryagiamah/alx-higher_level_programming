#!/usr/bin/python3
""" Contains a Square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Inherits Rectangle """

    def __init__(self, size):
        """ size vslidator """
        self.integer_validator('size', size)
        self.__size = size
              
    def area(self):
        """ Area implementation """
        return self.__size ** 2

    def __str__(self):
        """ str implementation """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
