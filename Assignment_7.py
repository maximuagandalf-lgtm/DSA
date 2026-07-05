#Define class stack to implement stack data structure using list. Define __init__() method to create an empty list object as instance object member of stack.

class stack:
    def __init__(self):
        self.l = []
    
    #Define a method is_empty() to check if the stack is empty in Stack class.
    def is_empty(self):
        return len(self.l) == 0 
    
    #In Stack class, define push() method to add data onto the stack.
    def push(self, data):
        self.data = data
        self.l.append(self.data)
        print(self.l)
    
    #In Stack class, define pop() method to remove top element from the stack.
    def pop(self):
        if self.is_empty():
            raise IndexError
        else: 
            return self.l.pop()  #pop always removes from the top of stack or end of list
    
    #In Stack class, define peek() method to return top element on the stack.
    def peek(self):
        if self.is_empty():
            raise IndexError
        else:
            return self.l[-1]   #-ve indexing cause top element of a astack will always be the last element of a list.

    #In Stack class, define size() method to return size of the stack that is number of items present in the stack.
    def size(self):
        return len(self.l)
    
#driver_code
s1 = stack()
s1.push(30)
#print(s1.pop())
print(s1.peek())
print(s1.size())
