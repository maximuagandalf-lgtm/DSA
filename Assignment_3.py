#Define a class Node to describe a Node of Singly linked list. 
class node: 
    def __init__(self, start, item, next):
        self.item = item
        self.next = next

# Define a class SLL to implement Singly Linked List with __init__() method and initialise start reference variable.

class SLL:
    def __init__(self, start = None):
        self.start = start

    def node(self, item, next):
        self.item = item
        self.node = node

#Define a method is_empty) to check if the linked list is empty in SLL class.

class SLL:
    def __init__(self, start):
        self.start = start

    def node(self, item, next):
        self.item = item
        self.next = next
    
    def is_empty(self):
        if self.item is None:
            print("The SLL is empty.")
    
    def insert_at_start(self, firstnew_node_item, firstnew_node_next, id):
        self.new_node_item = firstnew_node_item
        self.new_node_next = firstnew_node_next
        self.start = self.id 

    def insert_at_last(self, lastnew_node_item, lastnew_node = None):
        self.lastnew_node_item = lastnew_node_item
        SLL[len[SLL]-1]
    
