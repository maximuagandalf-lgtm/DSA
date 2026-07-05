#Define a class Stack to implement stack data structure using singly linked list concept. Define _init__ method to initialise start reference variable and item_count variable to keep track of number of elements in the stack.

class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class stack:
    def __init__(self, start = None):
        self.start = start
        self.item_count = 0
    
    #Define a method is_empty() to check if the stack is empty in Stack class.
    def is_empty(self):
        return self.start == None
    
    #In Stack class, define push() method to add data onto the stack.
    def push(self, data):
        self.data = data
        n = node(self.data)
        if self.is_empty():
            self.start = n
        else: 
            n.next = self.start
            self.start = n
            self.item_count += 1
    
    #In Stack class, define pop() method to remove top element from the stack.
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow")
        
        else: 
            print("The element removed is: ", self.start.data)
            self.start = self.start.next
            self.item_count -= 1

    #In Stack class, define peek() method to return top element on the stack.
    def peek(self):
        return self.start.data
    
    #In Stack class, define size() method to return size of the stack that is number of items present in the stack.
    def size(self):
        return self.item_count

#driver_code
s1 = stack()
s1.is_empty()
s1.push(10)
s1.push(20)
s1.push(30)
s1.pop()
print(s1.peek())
print(s1.size())