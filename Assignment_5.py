#Define a class Node to describe a node of a circular linked list.
class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        print("The node created is: ", self.data, self.next)

#Define a class CLL to implement Circular Linked List with _init_() method to create and initialise last reference variable.
class CLL:
    def __init__(self, last = None):
        self.last = last
        print("The last node in this Circular Linked List is: ", self.last)
    
    #Define a method is_empty() to check if the linked list is empty in CLL class.
    def is_empty(self):
        if self.last == None:
            return None
    
    #In class CLL, define a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_start(self, elem):
        self.elem = elem
        n = node(None, self.elem)       #we are calling a class node
        n.next = self.last.next
        self.last.next = n
    
    #In class CLL, define a method insert_at_last() to insert an element at the end of the list.
    def insert_at_last(self, elem):
        self.elem == elem
        n = node(None, self.elem)
        n.next = self.last.next
        self.last.next = n
        self.last = n

    #In class CLL, define a method search) to find the node with specified element value.
    def search(self, elem):
        self.elem = elem
        temp = self.last
        while temp.data != self.elem:
            temp = temp.next
        return temp
    
    #In class CLL, define a method insert_after() to insert a new node after a given node of the list.
    def insert_after(self, search_elem, insert_elem):
        self.search_elem = search_elem
        self.insert_elem = insert_elem
        if self.is_empty() == None:
            self.insert_at_start(self.insert_elem)
        
        else:
            n = node(None, self.insert_elem)
            s = self.search(self.search_elem)
            if s.next == self.last.next:
                self.insert_at_last(n)
            
            else:
                n.next = s.next
                s.next = n
    
    #In class CLL, define a method to print all the elements of the list.
    def show(self):
        temp = self.last.next
        while temp != self.last:
            print(temp)
            temp = temp.next
    
    #In class CLL, define a method delete_first() to delete first element from the list.
    def delete_first(self):
        temp = self.last.next
        self.last.next = temp.next
        temp.next = None
    
    #In class CLL, define a method delete_last() to delete last element from the list.
    def delete_last(self):
        temp = self.last.next
        while temp.next != temp:
            temp = temp.next
        temp.next = temp
    
    #In class CLL, define a method delete_item() to delete specified element from the list.
    def delete_item(self, elem):
        self.elem = elem 
        s = self.search(self.elem)
        temp = self.last 
        while temp.next != s.next:
            temp = temp.next
        temp.next = s.next
        s.next == None
    
    #In class CLL, implement iterator for CLL to access all the elements of the list in a sequence.
    def __iter__(self):
        return CLL_iterable(self.last)

class CLL_iterable:
    def __init__(self, start):
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
CLL1 = CLL(1000)
try_node = node(10, 10000)
CLL1.is_empty()
CLL1.insert_at_start(5)
CLL1.insert_at_last(15)
CLL1.insert_after(15, 20)
CLL1.search(10)
CLL1.show()
CLL1.delete_first()
CLL1.show()
CLL1.delete_last()
CLL1.show()
CLL1.delete_item(10)
CLL1.show()
for x in CLL1:
    print(x, end = " ")