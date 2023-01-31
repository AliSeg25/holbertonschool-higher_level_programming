#!/usr/bin/python3
"""Write a class Node that defines a node of a singly linked list by:"""


class Node:
    """ creation du noeud data """

    def __init__(self, data, next_node=None):

        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is None or isinstance(next_node, Node):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):

        """Return data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Controle value"""

        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return next node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):

        """controle valeur"""
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Liste chainer"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """incrementation"""

        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        nodetemp = self.__head
        if nodetemp.data > value:
            new_node.next_node = nodetemp
            self.__head = new_node
            return
        while nodetemp.next_node is not None and nodetemp.next_node.data < value:
            nodetemp = nodetemp.next_node
        new_node.next_node = nodetemp.next_node
        nodetemp.next_node = new_node

    def __str__(self):
        """print list"""

        res = []
        current = self.__head
        while current:
            res.append(str(current.data))
            current = current.next_node
        return "\n".join(res)
