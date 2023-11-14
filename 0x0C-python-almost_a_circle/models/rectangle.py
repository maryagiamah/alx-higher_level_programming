#!/usr/bin/python3
"""Modlue contains rectangle class"""
from .base import Base


class Rectangle(Base):
    ''' Rectangle class '''
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init Method"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if(value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if(value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x'''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if(value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y'''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if(value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value
