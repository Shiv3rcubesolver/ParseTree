#Complicated calculator including a recursive descent parse function
import tree, operator
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

#evaluator function. feed it a tree and it will solve the tree.
def evaluate(node):
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

    val = node.getRootValue()
    leftC = node.getLeftChild()
    rightC = node.getRightChild()
    
    if rightC and leftC and val in ops:
        function = ops[val]
        return function(evaluate(leftC), evaluate(rightC))
    else:
         return node.getRootValue()

#example evaluation
exampleFormula = "(3+(4*5))"
print("Formula: " + exampleFormula)
example = buildParseTree(exampleFormula)
print("Parse tree: ", tree.createList(example))
print("Solution:", evaluate(example))