#Complicated calculator including a recursive descent parse function
import tree
def buildParseTree(mathFormula):
    formula = list(mathFormula)
    parseTree = tree.Node()
    currentNode = parseTree
    for i in formula:
        if i == "(":
            currentNode = currentNode.setLeftChild()

        elif i in ["+", "-", "/", "*"]:
            currentNode.setRootValue(i)
            currentNode = currentNode.setRightChild()
        
        elif i == ")":
            currentNode = currentNode.getParent()
        
        else:
            try:
                currentNode.setRootValue(int(i))
                currentNode = currentNode.getParent()
            except:
                raise ValueError("incorrect value")
    return parseTree

example = buildParseTree("(3+(4*5))")
print(tree.createList(example))