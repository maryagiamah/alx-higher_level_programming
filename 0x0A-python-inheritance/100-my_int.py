#!/usr/bin/python3
""" Contains a  MyInt class """


class MyInt(int):
    """ MyInt class """

    def __eq__(self, other):
        """Inverted to != """
        return int(self) != other

    def __ne__(self, other):
        """Inverted to == """
        return int(self) == other
