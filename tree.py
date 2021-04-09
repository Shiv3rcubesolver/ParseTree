#looked at some code examples online and after a lot of meandering, decided to write a small 
# module's worth  of functions to be able to operate on a list of lists like it is a tree
#mostly based on pythonds stuff, idk if it counts as plagiarism or not, since I understand how they work

def binaryTree(value):
    return [value,[],[]]

def insertLeft(root, value):
    root[1] = [value, [], []]

def insertRight(root, value):
    root[2] = [value, [], []]

def getRootValue(root):
    return root[0]

def setRootValue(root, newValue):
    root[0] = newValue

def getLeft(root):
    return root[1]

def getRight(root):
    return root[2]