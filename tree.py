#completely updated binary tree module, relatively simple using objects

class Node:
    def __init__(self, value = None):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def setLeftChild(self, child):
        self.left = child 
        child.parent = self
        return self.left

    def setRightChild(self, child):
        self.right = child
        child.parent = self
        return self.right

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right
    
    def getRootValue(self):
        return self.value 

    def setRootValue(self, val):
        self.value = val

    def getParent(self):
        return self.parent    