#completely updated binary tree module, relatively simple using objects

class Node:
    def __init__(self, value = None, parent = None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def setLeftChild(self, val = None):
        self.left = Node(val, self) 
        return self.left

    def setRightChild(self, val = None):
        self.right = Node(val, self)
        return self.left

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
    
#decided to make a small function to create a list or values from a tree with the current node as the root node.
#assumes that if there is only one branch from a node that that node is still considered a 
#left or right child
def createList(root):
    list = [root.value]
    if root.left is None and root.right is None:
        return list

    else: 
        list.extend([[], []])

        if root.left is not None:
            list[1] = createList(root.left)

        if root.right is not None:
            list[2] = createList(root.right)
    
    return list
    