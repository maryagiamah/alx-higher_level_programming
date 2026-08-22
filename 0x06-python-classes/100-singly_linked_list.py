#!/usr/bin/python3
"""Defines a node class """


class Node:
    """Defines a node of a singly linked list """

    def __init__(self, data, next_node=None):
        """Initialises __data variable. """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns __data val """

        return self.__data

    @data.setter
    def data(self, value):
        """Sets __data with value"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Returns __next_node val """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets __next_node with value """

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list """

    def __init__(self):
        """Initialises the list """

        self.__head = None

    def sorted_insert(self, value):
        """Inserts a node into the sorted list """

        if self.__head is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
            return

        current = self.__head

        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        current.next_node = Node(value, current.next_node)

    def __str__(self):
        """Returns a str format to print """

        rep = []
        current = self.__head

        while current is not None:
            rep.append(str(current.data))
            current = current.next_node
        return "\n".join(rep)
