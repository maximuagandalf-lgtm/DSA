#priority Queue using list 
class Pqueue:
    def __init__(self):
        self.mylist = []
        #we will use priority number of element as index of the element in list. 
    
    def is_empty(self):
        return len(self.mylist) == 0
    
    def push(self, data = None, pnumber = None):
        items = (data, pnumber)
        index = 0
        if self.is_empty():
            self.mylist.append(items)
        else:
            while index < len(self.mylist) and self.mylist[index][1]:
                index += 1
            self.mylist.insert(index, items)

    def pop(self):
        if self.is_empty():
            raise IndexError('Priority Queue Underflow')
        else:
            print(f'{self.mylist[0]} removed.')
            self.mylist.pop(0) #element with highest priority will allways be inserted at index 0, rearranged according to indexing logic in lists.
    
    def show(self):
        print(f'Elements: {self.mylist}')
    
    def size(self):
        return len(self.mylist)

#driver_code
q1 = Pqueue()
print(q1.is_empty())
# q1.push(10, 1)
# q1.push(20, 2)
# q1.push(30, 4)
# q1.push(40, 5)
# q1.push(60, 6)
# q1.show()

# q1.pop()
# q1.show()
# q1.pop()
# q1.show()
# q1.pop()
# q1.show()

q1.push("Amit", 4)
q1.push("Arjun", 7)
q1.push("Ashima", 2)
q1.push("Agrah", 5)
q1.push("Anant", 8)
q1.push("Ambika", 1)

while q1.is_empty() != True:
    q1.pop()
    q1.show()