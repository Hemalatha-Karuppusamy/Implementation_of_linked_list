# Implementation_of_linked_list
Single linked list implementation

## Description
This Python class linked_list provides a simple implementation of a singly-linked list. A singly-linked list is a data structure where each element in the list, called a node, contains two parts: data and a reference to the next node. The list is initiated with a head pointing to the first node. The class includes methods for common linked list operations such as insertion, deletion, searching, and reversing.

## Class Methods
### __init__(self)
  Initializes a new linked list with an empty head (an empty list).
### display(self)
  Displays the elements of the linked list in sequence.
### insert(self, data, position='end', node=None)
  Inserts a new node with the given data into the linked list.
  The position argument determines where the new node is inserted. Options are 'start', 'end', or 'mid'.
  When position is 'start', the new node is inserted at the beginning of the list.
  When position is 'end', the new node is inserted at the end of the list.
  When position is 'mid', the new node is inserted after the node provided.
### delete(self, data)
  Deletes a node with the specified data from the linked list.
### search(self, data)
  Searches for a node with the specified data in the linked list and prints whether the element is present or not.
### reverse(self)
  Reverses the order of nodes in the linked list.
