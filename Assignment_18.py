#Implementing Dequeue using Doubly Linked List concept.
class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class Dequeue:
    def __init__(self, start = None):
        self.start = None
        self.item_count = 0
        self.rear = self.front = None
    
    def is_empty(self):
        return self.front == None
    
    def set(self):
        self.front = self.start
        temp = self.start
        while temp.next != None:
            temp = temp.next
        self.rear = temp
    
    def show(self):     
        #added an empty list and appended the node data one by one
        #before I was accessing refference by returning just temp, but now we return the values stored in those refferences.
        #instead of running the while while loop on, temp.next != None, we run it on temp != None. At the end of Dequeue, temp = None.
        if self.is_empty():
            raise IndexError('Dequeue Underflow')
        else:
            temp = self.start
            mylist = []
            while temp != None:
                mylist.append(temp.data)
                temp = temp.next
            return mylist
        
    def insert_front(self, data):
        n = Node(data)
        if self.is_empty():
            self.start = self.front = self.rear = n
            print(f'The updated Dequeue is: {self.show()}')
            self.item_count += 1
        else:
            n.next = self.start
            self.start = n
            self.front.prev = n
            self.set()
            print(f'The updated Dequeue is: {self.show()}')
            self.item_count += 1
    
    def insert_rear(self, data):
        n = Node(data)    
        if self.is_empty():
            self.insert_front(data)
        else:
            n.prev = self.rear
            self.rear.next = n
            self.item_count += 1
            self.set()
            print(f'The updated Dequeue is: {self.show()}')
    
    def delete_front(self):
        if self.is_empty():
            raise IndexError('Dequeque Underflow')
        else:
            elem = self.front.data
            self.front = self.start = self.front.next
            self.item_count -= 1
            self.set()
            print(f'{elem} is removed')
            print(f'The updated Dequeue is: {self.show()}')
    
    def delete_rear(self):
        if self.is_empty():
            raise IndexError('Dequeue Underflow')
        else:
            elem = self.rear.data
            self.rear.prev.next = None
            self.rear.prev = None
            self.item_count -= 1
            self.set()
            print(f'{elem} is removed')
            print(f'The updated dequeue is: {self.show()}')
    
    def get_front(self):
        if self.is_empty():
            raise IndexError('Dequeue Underflow')
        else:
            return self.front.data
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError('Dequeue Underflow')
        else:
            return self.rear.data
    
    def size(self):
        return self.item_count

#driver_code
q1 = Dequeue()
print(q1.is_empty())

try:
    q1.delete_front()
except IndexError as e:
    print(e.args[0])

try: 
    q1.delete_rear()
except IndexError as e:
    print(e.args[0])

try:
    print(f'The front element in Dequeue is: {q1.get_front()}')
except IndexError as e:
    print(e.args[0])
try:
    print(f'The rear element in Dequeue is: {q1.get_rear()}')
except IndexError as e:
    print(e.args[0])

q1.insert_front(10)
q1.insert_front(20)
q1.insert_front(30)
q1.insert_front(40)
q1.insert_front(50)
print(q1.is_empty())
q1.insert_rear(60)
q1.insert_rear(70)
q1.insert_rear(80)
q1.insert_rear(90)
q1.insert_rear(100)
print(q1.is_empty())

try:
    q1.delete_front()
except IndexError as e:
    print(e.args[0])

try:
    q1.delete_rear()
except IndexError as e:
    print(e.args[0])

try:
    print(f'The front element in Dequeue is: {q1.get_front()}')
except IndexError as e:
    print(e.args[0])
try:
    print(f'The rear element in Dequeue is: {q1.get_rear()}')
except IndexError as e:
    print(e.args[0])

print(f'The number of elements in the Dequeue are: {q1.item_count}')