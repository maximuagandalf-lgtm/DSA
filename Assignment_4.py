#Define a class Node to describe a node of a doubly linked list.
class node:
    def __init__(self, prev = None, data = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next
        print("The values in node are: ", self.prev, " ", 
              self.data, " ", self.next)

#Define a class DLL to implement Doubly Linked List with _init_() method to create and initialise start reference variable.

class DLL:
    def __init__(self, start = None):
        self.start = start
        print("This is the starting address of node: ", self.start)
    
    #Define a method is_empty() to check if the linked list is empty in DLL class.
    def is_empty(self):
        if self.start == None:
            print("The list is Empty")
            return None
    
    #In class DLL, define a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_start(self, elem):
        self.elem = elem
        if self.is_empty() == None: 
            n = node(None, self.elem)
            self.start = n
            n.prev = self.start
            print("The node inserted is: ", n)
            
        elif self.is_empty() != None:
            n = node(None, self.elem)
            n.next = self.start
            self.start = n
            n.prev = self.start
            print("The node inserted is: ", n)
    
    #In class DLL, define a method insert_at_last() to insert an element at the end of the list.
    def insert_at_last(self, elem) :
        self.elem = elem
        if self.is_empty() == None:
            self.insert_at_start(self.elem)
        
        else:
            temp = self.start
            while temp != None:
                temp = temp.next
            n = node(None, self.elem)
            temp.next = n
            n.prev = temp
    
    #In class DLL, define a method search () to find the node with specified element value.
    def search(self, elem):
        self.elem = elem
        if self.is_empty() == None:
            print("The list is Empty")
        
        elif self.is_empty() != None:
            temp = self.start
            while temp.item == self.elem:
                temp = temp.next
            return temp
        
        else: 
            print("An unexpected error occured. Please try again with valid values.")
    
    #In class DLL, define a method insert_after() to insert a new node after a given node of the list.

    def insert_after(self, elem):
        self.elem = elem
        if self.is_empty() == None:
            print("The list is Empty. Element is being inserted as the first element.")
            self.insert_at_start(self.elem)
        
        elif self.is_empty() != None:
            s = self.search(self.elem)
            if s.next == None:
                self.insert_at_last(self.elem)
            
            elif s.next != None:
                n = node(None, 30, None)
                s.next.prev = n
                n.next = s.next
                n.prev = s
                s.next = n
                
        else: 
            print("An unexpected error occured. Please! try again with valid input values.")
    
    #In class DLL, define a method to print all the elements of the list.
    def print_DLL(self):
        temp = self.start
        while temp.next != None:
            print("The Doubly linked list is: ", temp)
            temp = temp.next
    
    #In class DLL, define a method delete_first() to delete first element from the list.
    def delete_first(self):
        if self.is_empty() == None:
            print("There are no nodes in the list. The list is empty")
            raise ValueError
        
        elif self.is_empty() != None:
            if self.start.next == None:
                self.start == None
                self.start.prev = None
            else:
                temp = self.start
                self.start = temp.next
                temp.next.prev = self.start
                temp.next = temp.prev = None
        else: 
            print("An unexpected error occured. Please! try again with valid input values.")
    
    #In class DLL, define a method delete_last() to delete last element from the list.
    def delete_last(self):
        if self.is_empty() == None:
            print("There are no nodes in the list.")
        
        elif self.is_empty() != None:
            if self.start.next == None:
                self.delete_first()
            
            else:
                temp = self.start
                while temp.next != None:
                    temp = temp.next
                temp.prev == None
                temp.prev.next == None
            
        else: 
            print("An unexpected error occured. Please! try again with valid input values.")

    #In class DLL, define a method delete_item() to delete specified element from the list.
    def delete_item(self, elem):
        self.elem = elem
        if self.is_empty() == None:
            print("There are no nodes in the list.")
        
        elif self.is_empty() != None:
            if self.start.next == None:
                if self.start.data == self.elem:
                    self.delete_first()
                
                else:
                    s = self.search(self.elem)
                    if s.next == None:
                        self.delete_last()
                    
                    else: 
                        s.prev.next = s.next
                        s.next.prev = s.prev
                        s.next = s.prev = None
        
        else: 
            print("An unexpected error occured. Please! try again with valid input values.")
        
    #In class DLL, implement iterator for DLL to access all the elements of the list in a sequence.
    def iterator(self):
        return DLL_iterable(self.start)

class DLL_iterable:
    def __init__(self,start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

#driver code
new_node  = node(30, 40, 50)

my_DLL = DLL()

my_DLL.is_empty()

my_DLL.insert_at_start(10)

my_DLL.insert_at_last(100)

my_DLL.insert_after(10)

my_DLL.search(30)

my_DLL.print_DLL()

for i in my_DLL:
    print(i, end= " ")

my_DLL.delete_first()

my_DLL.delete_last()

my_DLL.delete_item(30)