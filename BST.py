__author__ = 'Hazem Safwat'

class BST :
    def __init__(self , root):
        self.left = None
        self.right = None
        self.root = root
    def left(self):
        return self.left
    def right(self):
        return self.right
    def setval(self,val):
        self.root = val
    def getval(self):
        return self.root
    def insert(self,val):
        if (self.root > val):self.left = BST(val)
        elif (self.root < val): self.right = BST(val)
    def inorder (tree):
        if tree != None:
            if tree.left !=None:
                BST.inorder(tree.left)
            print(tree.getval())
            if tree.right !=None:
                BST.inorder(tree.right)
