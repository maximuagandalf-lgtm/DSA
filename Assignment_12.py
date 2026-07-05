#Define a class Queue to implement queue data structure using list. Define _init_() method to create an empty list object as instance object member of Queue.
class Queue:
    def __init__(self):
        self.mylist = []
        self.item_count = 0
    
    #Define a method is _empty to check if the queue is empty in Queue class.
    def is_empty(self):
        return len(self.mylist) == 0
    
    #In Queue class, define enqueue() method to add data at the rear end of the queue.
    def enqueue(self, data):        
        self.mylist.append(data)
        print(f'{self.data} has been inserted')
        print(f'The updated Queue is : {self.mylist}')
        #the last of list(self.mylist[-1]) will be rear of the our queue
        self.rear = self.mylist[-1]
        self.item_count += 1
    
    #In Queue class, define dequeue() method to remove front element from the queue.
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")
        else: 
            self.front = self.mylist[0]
            self.mylist.pop(0)      
            #index of element is parsed in pop()
            print(f'{self.front} is removed from the Queue')
            print(f'The updated list is: {self.mylist}')
            self.front = self.mylist[0]
            self.item_count -= 1
        
    #In Queue class, define get_front() method to return front element of the queue.
    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")
        elif self.item_count == 1:      
            #if there is only 1 element in
            self.front = self.rear
            return self.front
        else:
            return self.front
    
    #In Queue class, define get_rear() method to return rear element of the queue.
    def get_rear(self):
        if self.is_empty(self):
            raise IndexError("Queue Underflow")
        else:
            return self.rear
    
    #In Queue class, define size method to return size of the queue that is number of items present in the queue.
    def size(self):
        #1st method(easy)
        #return len(self.mylist)

        #2nd method
        return self.item_count
    
#driver_code
Q1 = Queue()
print(Q1.is_empty())
Q1.enqueue(10)
Q1.enqueue(20)
Q1.enqueue(30)

try:                    #systematic exception handling
    print(Q1.get_front)
except IndexError as e:
    print(e.args[0])

try:
    print(Q1.get_rear)
except IndexError as e:
    print(e.args[0])

try:
    Q1.dequeue()
except IndexError as e:
    print(e.args[0])

print(f'The Front element of Queue is: {Q1.get_front}')
print(f'The Rear element of Queue is: {Q1.get_rear}')
print(f'The number of elements in this Queue are: {Q1.size()}')

try:
    Q1.dequeue()
except IndexError as e:
    print(e.args[0])
print(f'The Front element of Queue is: {Q1.get_front}')