#Complicated calculator including a recursive descent parse function
import tree
def buildParseTree(mathFormula):
    formula = list(mathFormula)

    for i in formula:
        if i == "(":
            tree.insertLeft(currentNode, '')
            stack.append(currentNode)
            currentNode = tree.getLeft(currentNode)

        elif i in ["+", "-", "/", "*"]:
            tree.setRootValue(currentNode, i)
            tree.insertRight(currentNode, '')
            stack.append(currentNode)
            currentNode = tree.getRight(currentNode)
        
        elif i == ")":
            currentNode = stack.pop()
        
        else:
            try:
                tree.setRootValue(currentNode, int(i))
                currentNode = stack.pop()
            except:
                raise ValueError("incorrect value uwu")
    return parseTree

print(buildParseTree("(3+(4*5))"))