 #!/usr/bin/python3

''' Contains a BaseGeometry class '''


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
     """ Inherits from Rectangle """
     def __init__(self, size):
         if not self.integer_validator('size', size):
             self.__size = size
    def area(self):
        ''' Area '''
         return self.__size ** 2
     def __str__(self):
         ''' Area '''
         return "[Rectangle] {}/{}".format(self.__size, self.__size) 
