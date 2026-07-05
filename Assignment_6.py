#Define a class Node to describe a node of a circular doubly linked list.
class Node:
    def __init__(self, prev = None, data = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next
        print("The node created is: ", self.prev, self.data, self.next)

#Define a class CDLL to implement Circular Doubly Linked List with to create and initialise last reference variable _init__() method.
class CDLL:
    def __init(self, last = None):
        self.last = last
    
    #Define a method is _empty() to check if the linked list is empty in CDLL class.
    def is_empty(self):
        if self.last == None:
            return None
    
    #In class CDLL, define a method insert_at_start to insert an element at the starting of the list.
    def insert_at_start(self, elem):
        self.elem = elem
        n = Node(None, self.elem)
        if self.is_empty() == None:
            j = Node()
            self.last = j
            j.next = n
            n.prev = j
            print("Two nodes are inserted: ", j, "at last and ", n, "at start")

        else: 
            self.last.next.prev = n
            n.next = self.last.next
            n.prev = self.last
    
    #In class CDLL, define a method insert_at_last() to insert an element at the end of the list.
    def insert_at_last(self, elem):
        self.elem = elem
        n = Node(None, self.elem)
        if self.is_empty() == None:
            self.last = n
        
        else: 
            n.next = self.last.next
            self.last.next.prev = n
            n.prev = self.last
            self.last.next = n
            self.last = n

    #In class CDLL, define a method search() to find the node with specified element value.
    def search(self):
        #traversal through next variable
        temp = self.last
        while temp.next != self.last:
            temp = temp.next
        return temp
        
        #traversal through prev variable
        # temp = self.last
        # while temp.prev != self.last:
        #     temp = temp.prev
        #return temp
    
    #In class CDLL, define a method insert_after() to insert a new node after a given node of the list.
    def insert_after(self, searchelem, insertelem):
        self.searchelem = searchelem
        self.insertelem = insertelem
        s = self.search(self.searchelem)
        n = Node(None, self.insertelem)
        s.next.prev = n
        n.next = s.next
        s.next = n
        n.prev = s
    
    #In class CDLL, define a method to print all the elements of the list.
    def show(self):
        temp = self.last
        print("The nodes in the CDLL are:")
        while temp.next != self.last:
            temp = temp.next
            print(temp)
    
        #traversal through prev variable
        # temp = self.last
        # print("The nodes in CDLL reverse ordered are: ")
        # while temp.prev != self.last:
        #     temp = temp.prev
        #     print(temp)
    
    #In class CDLL, implement iterator for CDLL to access all the elements of the list in a sequence.
    def __iter__(self):
        return CDLL_iterable(self.last)
    
    #In class CDLL, define a method delete _first() to delete first element from the list.
    def delete_first(self):
        self.last.next = self.last.next.next
        self.last.next.next.prev = self.last
        self.last.next = self.last.next.prev = None
    
    #In class CDLL, define a method delete_last() to delete last element from the list.
    def delete_last(self):
        self.last.prev.next = self.last.next
        self.last.next.prev = self.last.prev
        self.last = self.last.prev

    #In class CDLL, define a method delete_item() to delete specified element from the list.
    def delete_item(self, elem):
        self.elem = elem
        s = self.search(self.elem)
        if s.next == self.last.next:
            self.delete_last()
        elif s.data == self.last.next.data:
            self.delete_first()
        else: 
            s.next.prev = s.prev
            s.prev.next = s.next
            s.next = s.prev = None

class CDLL_iterable:
    def __init__(self, last):
        self.current = last
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data