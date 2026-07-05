#Import module containing singly linked list code in your python file.
from sll import SLL
#Define a class Stack to implement stack data structure. Define _init_() method to create Singly Linked List (SLL) object.
class stack:
    def __init__(self):
            self.mylist = SLL()
            self.item_count = 0
    
    #Define a method is _empty() to check if the stack is empty in Stack class.
    def is_empty(self):
        return self.mylist.is_empty()
    
    #In Stack class, define push() method to add data onto the stack.
    def push(self, data):
        self.data = data
        self.mylist.insert_at_start(self.data)
        self.item_count += 1
    
    #In Stack class, define pop() method to remove top element from the stack.
    def pop(self):
         self.mylist.delete_at_start()
         self.item_count -= 1
    
    #In Stack class, define peek() method to return top element on the stack.
    def peek(self):
         return self.mylist.start.data
    
    #In Stack class, define size() method to return size of the stack that is number of items present in the stack.
    def size(self):
         return self.item_count
         

#driver_code:
s1 = stack()
print(s1.is_empty())
s1.push(10)
s1.push(20)
s1.push(30)
s1.pop()
print("The top element in this stack is: ", s1.peek())
print("The no. of elements in this stack is: ", s1.size())