#Implementing Queue by extending List class
class list:
    def __init__(self):
        self.mylist = []

#Define a class Queue to implement queue data structure using list. Define _init_() method to create an empty list object as instance object member of Queue.
class Queue(list):
    def __init__(self):
        super().__init__()
        self.rear = self.front = None
        self.item_count = 0
    
    #Define a method is _empty to check if the queue is empty in Queue class.
    def is_empty(self):
        return len(self.mylist) == 0
    
    #In Queue class, define enqueue() method to add data at the rear end of the queue.
    def enqueue(self, data):
        self.mylist.append(data)
        self.item_count += 1
        self.rear = self.mylist[-1]
        self.front = self.mylist[0]
        print(f'The Updated Queue is: {self.mylist}')
    
    #In Queue class, define dequeue() method to remove front element from the queue.
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue Underflow')
        else:
            self.mylist.pop(0)
            self.item_count -= 1
            self.front = self.mylist[0]
            self.rear = self.mylist[-1]
            print(f'The updated list is: {self.mylist}')
    
    #In Queue class, define get_front() method to return front element of the queue.
    def get_front(self):
        if self.is_empty():
            raise IndexError('Queue Underflow')
        else:
            return self.front
    
    #In Queue class, define get_rear) method to return rear element of the queue.
    def get_rear(self):
        if self.is_empty(self):
            raise IndexError("Queue Underflow")
        else:
            return self.rear
    
    #In Queue class, define size method to return size of the queue that is number of items present in the queue.
    def size(self):
        return self.item_count

#driver_code
q1 = Queue()
print(q1.is_empty())

try:
    print(q1.get_front)
except IndexError as e:
    print(e.args[0])

try:
    print(q1.get_rear)
except IndexError as e:
    print(e.args[0])

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)

try:
    print(q1.get_front)
except IndexError as e:
    print(e.args[0])

try:
    print(q1.get_rear)
except IndexError as e:
    print(e.args[0])

print(f'The number of elements in this Queue are: {q1.size()}')