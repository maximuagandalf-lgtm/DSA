from dll import DLL

class Dequeue(DLL):
    def __init__(self):
        super().__init__()
        self.rear = self.front = None
        self.item_count = 0
    
    def is_empty(self):
        return super().is_empty()
    
    def set(self):
        self.front = self.start
        temp = self.start
        while temp.next != None:
            temp = temp.next
        self.rear = temp
    
    def insert_front(self, data):
        super().insert_at_start(data)
        self.set()
        self.item_count += 1
        print("Element inserted")
    
    def insert_rear(self, data):
        super().insert_at_last(data)
        self.item_count += 1
        self.set()
        print("Elements inserted")
    
    def delete_front(self):
        if self.is_empty():
            raise IndexError('Queue Underflow')
        else:
            print(f'{self.front.data} is removed. ')
            super().delete_at_start()
            self.item_count -= 1
            self.set()
            print(f'The updated list is: {super().show()}')
    
    def delete_rear(self):
        if self.is_empty():
            raise IndexError('Queue Underflow')
        else:
            print(f'{self.rear.data} is removed')
            super().delete_at_last()
            self.item_count -= 1
            self.set()
            print(f'The updated list is: {self.show()}')
    
    def get_front(self):
        if self.is_empty():
            raise IndexError('Queue underflow')
        else:
            return self.front.data
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError('Queue underflow')
        else:
            return self.rear.data
    
    def size(self):
        return self.item_count
    
#driver_code
q1 = Dequeue()
print(q1.is_empty())

q1.insert_front(10)
q1.insert_front(20)
q1.insert_front(30)
q1.insert_front(40)
q1.insert_front(50)

q1.insert_rear(60)
q1.insert_rear(70)
q1.insert_rear(80)
q1.insert_rear(90)
q1.insert_rear(100)

q1.delete_front()
q1.delete_rear()

print(q1.get_front())
print(q1.get_rear())

print(f'The number of elements in thsi Dequeue are: {q1.show()}')