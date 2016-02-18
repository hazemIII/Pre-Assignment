__author__ = 'Hazem Safwat'
from BST import BST
tree = BST(9)
tree.insert(7)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(80)
BST.inorder(tree)