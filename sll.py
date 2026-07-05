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
        n = Node(data)
        if self.is_empty():
            self.start = n
            n.next = None
        
        else: 
            n.next = self.start
            self.start = n
    
    def insert_at_last(self, data):
        if self.is_empty():
            self.insert_at_start(data)
        else:
            n = Node(data)
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = n

    def delete_at_start(self):
        if self.is_empty():
            raise IndexError("Data structure Underflow")
        
        else:
            self.data = self.start.data
            self.start = self.start.next