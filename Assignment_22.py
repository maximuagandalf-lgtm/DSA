#Implementing priority Queue with Linked list 
class Node:
    def __init__(self, data = None, priority = None, next = None):
        self.data = data
        self.priority = priority
        self.next = next

class Pqueue:
    def __init__(self, start = None):
        self.start = start
        self.item_count = 0
    
    def is_empty(self):
        return self.start == None
    
    def show(self):
        elements = []
        temp = self.start
        while temp != None:
            items = (temp.data, temp.priority)
            elements.append(items)
            temp = temp.next
        return elements
        
    def push(self, data, priority):
        n = Node(data, priority)
        if self.is_empty() or priority<self.start.priority:
            n.next = self.start
            self.start = n
            print(f'Element Inserted')
            self.item_count += 1
        else:
            temp = self.start
            while temp.next == None or temp.next.priority<=priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
            print("Element inserted")
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue Underflow")
        else:
            elem = self.start.data
            self.start = self.start.next
            self.item_count -= 1
            print(f'{elem} is removed')
    
    def size(self):
        return self.item_count
    
#driver_code
q1 = Pqueue()
print(q1.is_empty())
q1.push(10, 1)
q1.push(20, 2)

# print(f'number of elements: {q1.size()}')
# print(q1.show())
# q1.pop()
# print(f'number of elements: {q1.size()}')
# print(q1.show())
# print(f'number of elements: {q1.size()}')