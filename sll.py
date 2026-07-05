class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self, start = None):
        self.start = start
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        self.data = data
        n = Node(self.data)
        if self.is_empty():
            self.start = n
            n.next = None
        
        else: 
            n.next = self.start
            self.start = n
    
    def delete_at_start(self):
        if self.is_empty():
            raise IndexError("Stack Under Flow")
        
        else:
            data = self.start.data
            self.start = self.start.next
            print("The removed element is: ", data)