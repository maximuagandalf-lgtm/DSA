class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self, start = None):
        self.start = start
    
    def is_empty(self):
        return self.start == None
    
    def show(self):
        elements =[]
        temp = self.start
        while temp != None:
            elements.append(temp.data)
            temp = temp.next
        return elements
    
    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            self.start = n
        else:
            self.start.prev = n
            n.next = self.start
            self.start = n
    
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            self.insert_at_start()
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            n.prev = temp
            temp.next = n
    
    def delete_at_start(self):
        if self.is_empty():
            raise IndexError('Doubly Linked List Undeflow')
        else:
            self.start = self.start.next
    
    def delete_at_last(self):
        if self.is_empty():
            raise IndexError('Doubly Linked List Underflow')
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.prev.next = None
            temp.prev = None