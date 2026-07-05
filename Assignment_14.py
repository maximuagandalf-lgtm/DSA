#Implementing Queue using SLL Class
from sll import *

#Define a class Queue to implement queue data structure using list. Define _init_() method to create an empty list object as instance object member of Queue.
class Queue:
    def __init__(self):
        self.mylist = SLL()
        self.front = self.rear = None
        self.item_count = 0

    #Define a method is _empty to check if the queue is empty in Queue class.
    def is_empty(self):
        return self.mylist.is_empty()
    
    def set(self):
        self.front = self.mylist.start   #setting value of front

        temp = self.mylist.start
        while temp.next != None:
            temp = temp.next
        self.rear = temp        #setting value of rear
    
    #In Queue class, define enqueue() method to add data at the rear end of the queue.
    def enqueue(self, data):
        self.mylist.insert_at_last(data)
        print(f'The updated list is: {self.mylist}')
        self.set()
        self.item_count += 1
    
    #In Queue class, define dequeue() method to remove front element from the queue.
    def dequeue(self):
        self.mylist.delete_at_start()
        print("The removed element is: ", self.mylist.data)
        print(f'The updated list is: {self.mylist}')
        self.set()
        self.item_count -= 1

    #In Queue class, define get_front() method to return front element of the queue.
    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")
        else:
            return self.front
    #In Queue class, define get_rear() method to return rear element of the queue.
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