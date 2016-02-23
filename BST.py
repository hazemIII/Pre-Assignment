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
    def insert(self,item):
        if (item < self.getval()):
            if (self.left != None):
                self.left.insert(item)
            else:
                self.left = BST(item)
        else:
            if (self.right != None):
                self.right.insert(item)
            else:
                self.right = BST(item)


    def inorder (tree):
        if tree != None:
            if tree.left !=None:
                BST.inorder(tree.left)
            print(tree.getval())
            if tree.right !=None:
                BST.inorder(tree.right)

    def stepCounter (tree , counter=0 ):
        if tree != None:
            if tree.left !=None:
                counter=BST.stepCounter(tree.left , counter+1)

            if tree.right !=None:
                counter=BST.stepCounter(tree.right , counter+1)

        return counter