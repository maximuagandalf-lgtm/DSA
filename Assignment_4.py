#Define a class Node to describe a node of a doubly linked list.
class node:
    def __init__(self, prev = None, data = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next
        print("The values in node are: ", self.prev, " ", 
              self.data, " ", self.next)

new_node  = node(30, 40, 50)