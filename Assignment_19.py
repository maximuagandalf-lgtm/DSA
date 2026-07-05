from dll import *

class Dequeue:
    def __init__(self):
        self.mylist = DLL()
        self.rear = self.front = None
        self.item_count = 0

    def is_empty(self):
        return self.mylist.is_empty()
    
    def set(self):
        self.front = self.mylist.start
        temp = self.mylist.start
        while temp.next != None:
            temp = temp.next
        self.rear = temp
    
    def show(self):
        return self.mylist.show()
    
    def insert_front(self, data):
        self.mylist.insert_at_start(data)
        self.set()
        self.item_count += 1
        print(f'The element is inserted succesfully.')
    
    def insert_rear(self, data):
        self.mylist.insert_at_last(data)
        self.item_count += 1
        self.set()
        print(f'The element is inserted succesfully.')
    
    def delete_front(self):
        if self.is_empty():
            raise IndexError('Dequeue Underflow')
        else:
            print(f'{self.front.data} is removed')
            self.mylist.delete_at_start()
            self.item_count -= 1
            self.set()
            print(f'The updated Dequeue is: {self.show()}')
    
    def delete_rear(self):
        if self.is_empty():
            raise IndexError('Dequeue Underflow')
        else:
            print(f'{self.rear.data} is removed')
            self.mylist.delete_at_last()
            self.item_count -= 1
            self.set()
            print(f'The updated Dequeue is: {self.show()}')
    
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
    print(q1.get_front())
except IndexError as e: 
    print(e.args[0])

try:
    print(q1.get_rear())
except IndexError as e:
    print(e.args[0])

print(f'The number of elements in this Dequeue are: {q1.size}')

print(f'The elements in this Dequeue are: {q1.show()}')

q1.insert_front(10)
q1.insert_front(20)
q1.insert_front(30)
q1.insert_front(40)
q1.insert_front(50)

print(q1.get_front())
print(q1.get_rear())

q1.insert_rear(60)
q1.insert_rear(70)
q1.insert_rear(80)
q1.insert_rear(90)
q1.insert_rear(100)

print(q1.get_front())
print(q1.get_rear())

print(f'The number of elements in this Dequeue are: {q1.size()}')

q1.delete_front()
q1.delete_rear()
print(q1.get_front())
print(q1.get_rear())
print(f'The number of elements in this Dequeue are: {q1.size()}')
print(f'The elements in this Dequeue are: {q1.show()}')