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

    def node(self, item, next = None):
        self.item = item
        self.next = next
    
    def is_empty(self):
        if self.start == None:   #agar koi node nahi hai toh start mein koi value nahi hogi
            print("The SLL is empty.")
            return self.start == None
    
    def insert_at_start(self, firstnew_node_item, id):
        if self.start != None:
            n = node(10, self.start)  #first we have to create the next node and we store the address of next node in "next" from "start"
            self.start = n #now hum n ke andar jo node hai uski value ko start mein store karenge.
        
        elif self.start == None:
            n = node(10)
            self.start = n
    
    def insert_at_last(self, new_item):
        self.new_item = new_item
        n = node(self.new_item)
        if self.start == None: 
            self.start = n
        
        elif self.start != None:
            temp = self.start #temp will point to same address as start variable.
            while temp.next != None:
                temp = temp.next
            temp.next = n
    
    def search(self, elem):
        self.elem = elem
        if self.is_empty() == None: 
            print("The list is empty.")
            return None
        
        elif self.is_empty() != None:
            temp = self.start
            while temp.next != None:
                if temp.item == self.elem:
                    print("The required element is at ", temp)
                    return temp
                
                else :
                    temp = temp.next
        else: 
            return("An unexpected error occurred. Please! retry with valid values")
     
    def insert_after(self, data = None, elem = None):
        self.data = data
        self.elem = elem
        n = node(self.data, self.next)
        if self.is_empty() == None:
            self.start = n
        
        elif self.is_empty() != None: 
            s = self.search(self.elem)
            n.next = s.next
            s.next = n

        else:
            return("An unexpeted error occured. Please Try again with valid values.")


