#!/usr/bin/python3
"""
This module contains Full Rectangle task
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Class Initialization"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area"""
        return self.__width * self.__height

    def __str__(self):
        """Return string"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
