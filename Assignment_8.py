#Define a class Stack to implement stack data structure by extending list class.
class list:
    def __init__(self):
        self.l = []
        return self.l
    
    def insert(self, index = None, data = None):  #if no index is provided insert() will work as append().
        self.data = data
        self.index = index
        self.l.insert(self.index, self.data)
        return self.l
    
    def pop(self):
        return self.l.pop(0)
    
    def peek(self):
        return self.l[0]
    
    def size(self):
        return len(self.l)

class stack(list):
    def __init__(self):
        super().__init__()
        print("The stack has been created: ", self.l)

    #Define a method is_empty() to check if the stack is empty in Stack class.
    def is_empty(self):
        return len(self.l) == 0
    
    #In Stack class, define push() method to add data onto the stack.
    def push(self, data):
        self.data = data
        print("The Updated list is: ", super().insert(0, self.data))
    
    #In Stack class, define pop() method to remove top element from the stack.
    def pop(self):
        if self.is_empty():
            print("Stack underflow")
        
        else:
            super().pop()
            print("Top element has been removed from the stack. The updated list is: ", self.l)
    
    #In Stack class, define peek() method to return top element on the stack.
    def peek(self):
        if self.is_empty():
            print("Stack Underflow")
        
        else: 
            print("The topmost element in this stack is: ", 
              super().peek())
        
    #In Stack class, define size() method to return size of the stack that is number of items present in the stack.
    def size(self):
        if self.is_empty():
            print("Stack Underflow")
        
        else: 
            print("The number of items in the stack are: ", 
                super().size())

#driver_code
s1 = stack()
print(s1.is_empty())
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.pop()
s1.peek()
s1.size()