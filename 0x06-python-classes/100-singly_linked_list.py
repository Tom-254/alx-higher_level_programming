#!/usr/bin/python3
"""Defines SinglyLinkedList classes"""


class Node():
    """Describes Node class for singlyLinkedList"""

    def __init__(self, data, next_node=None):
        """Initialize the Node class instance attributes
            Args:
            data (int): data that the node contains
            next_node (Node): The next node in the SinglyLinkeList
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of the in the Node
           Returns:
                int: data of the in the Node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
         Sets the data of the node
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the nextnode
           Returns:
                object: the next node in the list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
         Sets the nextnode in the list
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """
       Creates a SinglyLinkedList
    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
            Inserts the nodes in sorted order  increasingly
            Args:
                value (int): The value of the node
        """
        node = Node(value)
        tmp = self.__head

        if self.__head is None:
            self.__head = node
            return

        if node.data < tmp.data:
            node.next_node = tmp
            self.__head = node
            return

        while tmp.next_node is not None:
            if tmp.next_node.data < node.data:
                tmp = tmp.next_node
            else:
                node.next_node = tmp.next_node
                tmp.next_node = node
                return
        tmp.next_node = node

    def __str__(self):
        tmp = self.__head
        if tmp is None:
            return ("")
        while tmp.next_node is not None and tmp:
            print(tmp.data)
            tmp = tmp.next_node
        return (str(tmp.data))
