__author__ = 'Hazem Safwat'
class Stack :
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def getSize(self):
        return len(self.items)
    def multiPop(self , times=1):
        i = min(times,self.getSize())
        while (times != 0):
            return self.items.pop()
            times=times-1

