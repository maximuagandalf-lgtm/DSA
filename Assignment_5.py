#Define a class Node to describe a node of a circular linked list.
class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        print("The node created is: ", self.data, self.next)

#Define a class CLL to implement Circular Linked List with _init_() method to create and initialise last reference variable.
class CLL:
    def __init__(self, last = None):
        self.last = last
        print("The last node in this Circular Linked List is: ", self.last)
    
    #Define a method is_empty() to check if the linked list is empty in CLL class.
    def is_empty(self):
        if self.last == None:
            return None
    
    #In class CLL, define a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_start(self, elem):
        self.elem = elem
        n = node(None, self.elem)       #we are calling a class node
        n.next = self.last.next
        self.last.next = n
    
    #In class CLL, define a method insert_at_last() to insert an element at the end of the list.
    def insert_at_last(self, elem):
        self.elem == elem
        n = node(None, self.elem)
        n.next = self.last.next
        self.last.next = n
        self.last = n

    #In class CLL, define a method search) to find the node with specified element value.
    def search(self, elem):
        self.elem = elem
        temp = self.last
        while temp.data != self.elem:
            temp = temp.next
        return temp
    
    #In class CLL, define a method insert_after() to insert a new node after a given node of the list.
    def insert_after(self, search_elem, insert_elem):
        self.search_elem = search_elem
        self.insert_elem = insert_elem
        if self.is_empty() == None:
            self.insert_at_start(self.insert_elem)
        
        else:
            n = node(None, self.insert_elem)
            s = self.search(self.search_elem)
            if s.next == self.last.next:
                self.insert_at_last(n)
            
            else:
                n.next = s.next
                s.next = n