#!/usr/bin/python3
'''Contains Rectangle class
    that Inherits  BaseGeometry
'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """ Inherits BaseGeometry Class """
    
    def __init__(self, width, height):
        if not self.integer_validator('width', width):
            if  not self.integer_validator("height", height):
                self.__height = height
                self.__width = width
    def area(self):
        ''' Area of the rectangle '''
        
        return self.__width * self.__height
     def __str__(self):
         ''' String repr '''
         
         return "[Rectangle] {}/{}".format(self.__width, self.__height)