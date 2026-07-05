class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self, start = None):
        self.start = start
        self.rear = self.front = None
        self.item_count = 0
    
    def is_empty(self):
        return self.start == None
    
    def set(self):
        self.front = self.start
        temp = self.start
        while temp.next != None:
            temp = temp.next
        self.rear = temp
    
    def show(self):
        if self.is_empty():
            raise IndexError('Queue Underflow')
        else:
            temp = self.start
            while temp.next != None:
                print(temp)
                temp = temp.next

    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.start = n
            self.set()
            self.item_count += 1
        else:
            self.rear.next = n
            self.set()
            self.item_count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue Underflow')
        else:
            elem = self.front.data
            self.start = self.front.next
            self.front.next = None
            self.set()
            self.item_count -= 1
            print(f'The element removed is: {elem}')
    
    def get_front(self):
        if self.is_empty():
            raise IndexError('Queue Underflow')
        else:
            return self.front.data
    
    def get_rear(self):
        if self.is_empty(self):
            raise IndexError('Queue Underflow')
        else:
            return self.rear.data
    
    def size(self):
        return self.item_count

#driver_code
q1 = Queue()
print(q1.is_empty())

try:
    print(q1.show()) #try and except statement doesn't throw error and rest of the code still continues to execute despite an error.
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
    print(q1.show())
except IndexError as e:
    print(e.args[0])

q1.dequeue()

try: 
    print(q1.show())
except IndexError as e:
    print(e.args[0])

try: 
    print(q1.get_front)
except IndexError as e:
    print(e.args[0])

try: 
    print(q1.get_rear)
except IndexError as e:
    print(e.args[0])

print(f'The number of elements in Queue are: {q1.size()}.')