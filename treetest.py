#small piece of code to test the functionality of some of the tree commands.  use as you will.
import tree

testTree = tree.Node(3)
testTree.setLeftChild(5)
testTree.setRightChild(6)
print(tree.createList(testTree))
