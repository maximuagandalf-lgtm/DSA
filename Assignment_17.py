#Implementing Dequeue(Doubly Ended Queue) with list.
class Dequeue:
    def __init__(self):
        self.mylist = []
        self.rear = self.front = None
    
    def is_empty(self):
        return len(self.mylist) == 0
    
    def insert_front(self, data):
            self.mylist.insert(0, data)
            print(f'The updated Queue is: {self.mylist}')
    
    def insert_rear(self, data):
            self.mylist.append(data)
            print(f'The updated Queue is: {self.mylist}')
    
    def delete_front(self):
        if self.is_empty():
            raise IndexError('Queue Underflow')
        else:
            self.mylist.pop(0)
            print(f'The updated list is: {self.mylist}')
    
    def delete_rear(self):
        if self.is_empty():
            raise IndexError('Queue Underflow')
        else:
            self.mylist.pop() #pop() defaultly deletes last elem
            print(f'The updated list is: {self.mylist}')
    
    def get_front(self):
        if self.is_empty():
            raise IndexError('Queue Underflow')
        else:
            return self.mylist[0]
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError('Queue Underflow')
        else:
            return self.mylist[-1]
    
    def size(self):
        return len(self.mylist)

#driver_code
q1 = Dequeue()
print(q1.is_empty())

try:
    print(f'The front element of Queue is: {q1.get_front()}')
except IndexError as e:
    print(e.args[0])

try:
    print(f'The rear element of Queue is: {q1.get_rear()}')

except IndexError as e:
    print(e.args[0])

q1.insert_front(10)
q1.insert_front(20)
q1.insert_front(30)
q1.insert_front(40)
print(q1.is_empty())
q1.insert_rear(50)
q1.insert_rear(60)
q1.insert_rear(70)
q1.insert_rear(80)
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
    print(f'The front element of Queue is: {q1.get_front()}')
except IndexError as e:
    print(e.args[0])

try:
    print(f'The rear element of Queue is: {q1.get_rear()}')

except IndexError as e:
    print(e.args[0])

print(f'The number of elements in the Queue are: {q1.size()}')