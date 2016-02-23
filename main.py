__author__ = 'Hazem Safwat'
from BST import BST
import random
from tabulate import tabulate
table = [[]]
for i in range(51):  #creating 50 different trees
    size = random.randint(50,100)
    items = random.sample(range(1,12000) , size) #random items in tree has a size = size
    tree = BST(items[0])   #Root of the tree
    for j in range(1,size):    #inserting items in the tree
        tree.insert(items[j])
    counter = BST.stepCounter(tree)
    table.append([i , size , counter , 2*counter])

print(tabulate(table[1:51] , headers= ["no." , "number of items" ,"number of calls" ,"number of steps"  ]))
