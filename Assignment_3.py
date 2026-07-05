class SLL:
    # Define a class SLL to implement Singly Linked List with __init__() method and initialise start reference variable.
    def __init__(self, start):
        self.start = start

    #Define a class Node to describe a Node of Singly linked list. 
    def node(self, item, next = None):
        self.item = item
        self.next = next
    #Define a method is_empty) to check if the linked list is empty in SLL class.
    def is_empty(self):
        if self.start == None:   #agar koi node nahi hai toh start mein koi value nahi hogi
            print("The SLL is empty.")
            return self.start == None

    #In class SLL, define a method insert _at_start to insert an element at the start of the list.
    def insert_at_start(self, firstnew_node_item, id):
        if self.is_empty() != None:
            n = self.node(10, self.start)  #first we have to create the next node and we store the address of next node in "next" from "start"
            self.start = n #now hum n ke andar jo node hai uski value ko start mein store karenge.
        
        elif self.is_empty() == None:
            n = self.node(10)
            self.start = n
    
    #In class SLL, define a method insert _at_last) to insert an element at the end of the list.
    def insert_at_last(self, new_item):
        self.new_item = new_item
        n = self.node(self.new_item)
        if self.is_empty() == None: 
            self.start = n
        
        elif self.is_empty() != None:
            temp = self.start #temp will point to same address as start variable.
            while temp.next != None:
                temp = temp.next
            temp.next = n
    
    #In class SLL, define a method search() to find the node with specified element value.
    def search(self, elem):
        self.elem = elem
        if self.is_empty() == None: 
            print("The list is empty.")
            return None
        
        elif self.is_empty() != None:
            temp = self.start
            while temp.next != None:
                if temp.item == self.elem:
                    print("The required element is at ", temp)
                    return temp
                
                else :
                    temp = temp.next
        else: 
            return("An unexpected error occurred. Please! retry with valid values")
    
    #In class SLL, define a method insert _after) to insert a new node after a given node of the list.
    def insert_after(self, data = None, elem = None):
        self.data = data
        self.elem = elem
        n = self.node(self.data, self.next)
        if self.is_empty() == None:
            self.start = n
        
        elif self.is_empty() != None: 
            s = self.search(self.elem)
            n.next = s.next
            s.next = n

        else:
            return("An unexpeted error occured. Please Try again with valid values.")
    
    #In class SLL, define a method to print all the elements of the list.
    def show(self):
        if self.is_empty() == None:
            print("There are no nodes in the list.")
        
        elif self.is_empty() != None:
            temp = self.start
            while temp.next != None:
                print(temp.item, end = " ")
                temp = temp.next
        else: 
            print("An unexpected error occured. Please! try again with valid input values.")

    
    #In class SLL, implement iterator for SLL to access all the elements of the list in a sequence.
    def iterator(self, elem):
        self.elem = elem
        temp = self.start
        while temp.item == self.elem:
            temp = temp.next
        return temp


    #In class SLL, define a method delete_first to delete first element from the list.
    def delete_first(self):
        if self.is_empty() == None:
            print("There are no nodes in the list.")
        
        elif self.is_empty() != None:
            temp = self.start
            self.start = temp.next
            temp.next = None
        else: 
            print("An unexpected error occured. Please! try again with valid input values.")
    
    #In class SLL, define a method delete_last) to delete last element from the list.
    def delete_last(self):
        if self.is_empty() == None:
            print("There are no nodes in the list.")

        elif self.start.next == None:
            self.start = None
        
        elif self.is_empty() != None:
            temp = self.start
            while temp.next.next != None:
                temp.next = None
            
        else: 
            print("An unexpected error occured. Please! try again with valid input values.")

    #In class SLL, define a method delete_item() to delete specified element from the list.

    def delete_item(self, elem):
        self.elem = elem
        if self.is_empty() == None:
            print("There are no nodes in the list.")
        
        elif self.is_empty() != None:
            s = self.search(self.elem)
            if self.start == s:
                self.delete_first()
            
            elif s.next == None:
                self.delete_last()
            
            else: 
                temp = self.start
                while temp.next.next == s.next:
                    temp = temp.next
                temp.next = s.next
                s.next = None

        else: 
            print("An unexpected error occured. Please! try again with valid input values.")
#driver code
mylist = SLL()
mylist.node(10)
mylist.insert_at_start(20)
mylist.insert_at_last(50)
mylist.insert_after(90, mylist.search(50))
mylist.show()
print(mylist.iterator(90))
mylist.delete_item(90)
mylist.delete_first()
mylist.delete_last()

