class Node:
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST():
    def __init__(self, root = None):
        self.root = root
    
    def insert(self, data):
        self.root = self.rinsert(self.root, data)
        print("Element Inserted")
    
    def rinsert(self, root, data):
        if root == None:
            return Node(data)
        elif data>root.item:
            root.right = self.rinsert(root.right, data)
        elif data<root.item:
            root.left = self.rinsert(root.left, data)
        return root
    
    def search(self, data):
        temp = self.root
        return self.rsearch(data, temp)
    
    def rsearch(self, data, temp):
        if data==temp.item:
            return temp
        elif data>temp.item:
            self.rsearch(data, temp.right)
        elif data<temp.item:
            self.rsearch(data, temp.left)
        else:
            print("Search Failed")
            return None
    
    def inorder(self):
        output = []
        self.rinorder(output,  self.root.left, self.root)
        return output
    def rinorder(self, output = None, child = None, parent = None):
        if child.left == None:
            output.append(child.item)
            if child.right == None:
                output.append(parent.item)
            elif child.right != None:
                parent = parent.right
                self.rinorder(output, parent.left, parent)
        elif child.left != None:
            self.rinorder(output, child.left, parent.left)
#driver_code
t1 = BST()
t1.insert(50)
t1.insert(60)
t1.insert(70)
t1.insert(80)
t1.insert(90)
t1.insert(100)
t1.insert(40)
t1.insert(30)
t1.insert(20)
t1.insert(10)
print(t1.search(50))
print(t1.inorder())
