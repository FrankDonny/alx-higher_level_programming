#!/usr/bin/python3
"""A node Class"""


class Node:
    """initializing the Node"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    """Node data property"""
    def data(self):
        return self.__data

    @data.setter
    """Node data Setter"""
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    """Node next_node property"""
    def next_node(self):
        return self.__next_node

    @next_node.setter
    """Node next_node Setter"""
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

        
"""A linked list class below"""
        
        
class SinglyLinkedList:
    """initializing the linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """sort method to sort the values and inser
        nodes
        """
        newNode = Node(value)
        temp = self.__head
        if self.__head is None:
            self.__head = newNode
            return

        if newNode.data < temp.data:
            newNode.next_node = temp
            self.__head = newNode
            return

        while temp.next_node is not None:
            if temp.next_node.data < newNode.data:
                temp = temp.next_node
            else:
                newNode.next_node = temp.next_node
                temp.next_node = newNode
                return
        temp.next_node = newNode

    def __str__(self):
        temp = self.__head
        if temp is None:
            return ("")
        while temp.next_node is not None and temp:
            print(temp.data)
            temp = temp.next_node
        return (str(temp.data))
