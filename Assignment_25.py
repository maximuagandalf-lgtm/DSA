#learn delete method once more -
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
        return self.rsearch(data, self.root)
    
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
        self.rinorder(output, self.root)
        return output
    def rinorder(self, output, root):
        if root != None:
            self.rinorder(output, root.left)
            output.append(root.item)
            self.rinorder(output, root.right)
    
    def preorder(self):
        output = []
        self.rpreorder(self, output, self.root)
        return output
    def rpreorder(self, output, root):
        if root != None:
            output.append(root.item)
            self.rinorder(output, root.left)
            self.inorder(output, root.right)
    
    def postorder(self):
        output = []
        self.rpostorder(output, self.root)
        return output
    def rpostorder(self, output, root):
        if root != None:
            self.rpostorder(output, root.left)
            self.rpostorder(output, root.right)
            output.append(root.item)
    
    def min(self):
        temp = self.root
        while temp.left != None:
            temp = temp.left
        return temp.item
    
    def max(self):
        temp = self.root
        while temp.right != None:
            temp = temp.right
        return temp.item
    
    def delete(self, data):
        self.root = self.rdelete(self.root, data)
        print(f'{data} deleted')
    
    def rdelete(self, root, data):
        if root is None:
            return root
        elif data<root.item:
            root.left = self.rdelete(root.left, data)
        elif data>root.item:
            root.right = self.rdelete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                root.item = self.min(root.right)
                self.rdelete(root.right, root.item)
            return root

    def size(self):
        elem = self.inorder()
        return len(elem)
        
#driver_code
t1 = BST()
t1.insert(50)
t1.insert(60)
t1.insert(30)
t1.insert(70)
t1.insert(80)
t1.insert(40)
t1.insert(10)
t1.insert(100)
t1.insert(130)
t1.insert(90)
t1.insert(20)
t1.insert(5)
t1.insert(0)
print(t1.search(50))
print("Inorder Output -- ", t1.inorder())
print("Preorder Output -- ", t1.inorder())
print("Postorder Output -- ", t1.postorder())
print("The minimum node value is: ", t1.min())
print("The maximum node value is: ", t1.max())
print("The size of the BST is: ", t1.size())