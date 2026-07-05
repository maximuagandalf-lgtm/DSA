#Define a class Queue to implement queue data structure using list. Define _init_() method to create an empty list object as instance object member of Queue.
from sll import *
class Queue(SLL):
    def __init__(self):
        super().__init__()
        self.rear = self.front = None
        self.item_count = 0

    #Define a method is_empty() to check if the queue is empty in Queue class.
    def is_empty(self):
        return super().is_empty()
    
    def set(self):
        self.front = self.start
        
        temp = self.start
        while temp.next != None:
            temp = temp.next
        self.rear = temp
  
    #In Queue class, define enqueue() method to add data at the rear end of the queue.
    def enqueue(self, data):
        super().insert_at_last(data)
        print(f'The updated list is: {self.show()}')
        self.set()
        self.item_count += 1
    
    #In Queue class, define dequeue() method to add data at the rear end of the queue.
    def dequeue(self):
        super().delete_at_start()
        print(f'The deleted element is: {self.data}')
        print(f'The updated Queue is: {self.show()}')
        self.set()
        self.item_count -= 1
    
    #In Queue class, define get_front() method to return front element of the queue.
    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")
        else: 
            return self.get_front
    
    #In Queue class, define get_front() method to return front element of the queue.
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")
        else:
            return self.get_rear
    
    #In Queue class, define size() method to return size of the queue that is number of items present in the queue.
    def size(self):
        return self.item_count

#driver_code
q1 = Queue()
print(q1.is_empty())

try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])

try:
    print(q1.get_rear())
except IndexError as e:
    print(e.args[0])

try: #will raise error but the code still works and we don't get a big error screen due to this try and catch statement.
    q1.dequeue()
except IndexError as e:
    print(e.args[0])

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.enqueue(60)
q1.enqueue(70)
q1.enqueue(80)
q1.enqueue(90)
q1.enqueue(100)

try:
    q1.dequeue()
except IndexError as e:
    print(e.args[0])

try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])

try:
    print(q1.get_rear())
except IndexError as e:
    print(e.args[0])

print(f'The number of elemnts in this Queue are: {q1.size()}', )
