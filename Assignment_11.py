#Import module containing singly linked list code in your python file.
from sll import SLL

#Define a class Stack to implement stack data structure by inheriting SLL class.
class stack(SLL):
    def __init__(self):
        super().__init__()
        self.count = 0

    #Define a method is _empty() to check if the stack is empty in Stack class.
    def is_empty(self):
        return super().is_empty()
    
    #In Stack class, define push() method to add data onto the stack.
    def push(self, data):
        self.data = data
        super().insert_at_start(self.data)
        self.count += 1
    
    #In Stack class, define pop() method to remove top element from the stack.
    def pop(self):
        super().delete_at_start()
        self.count -= 1
    
    #In Stack class, define peek() method to return top element on the stack.
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack Underflow")
        else:
            return self.start.data
    
    #In Stack class, define size() method to return size of the stack that is number of items present in the stack.
    def size(self):
        if self.is_empty():
            raise IndexError("Stack Underflow")
        else:
            return self.count
    
#driver_code
s1 = stack()
print(s1.is_empty())
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.is_empty())
s1.pop()
s1.peek()
print(s1.size())