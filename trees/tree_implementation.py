# strucutre of tree 

class Node:
    def __init__(self,data):
        self.data = data
        self.children = []

 # function to add child to node   
def addChild(parent,child):
    parent.children.append(child)


# function to print parents of each node

def printParent(node,parent):
    if parent is None:
        print((str(node.data)) + ' -> Null')

    else:
        print((str(node.data))+ ' -> ' (str(parent.data)))

    for child in node.children:
        printParent(child,node)


# function to print leadnodes

def leafNodes(node):
    if not node.children:
        print(str(node.data))
        return
    
    for child in node.children:
        leafNodes(child)


# degree of nodes

def degree(node,parent):
    deg = len(node.children)

    if parent is not None:
        deg += 1

    print(str(node.data) + " -> " + str(deg))

    for child in node.children:
        degree(child,node)

        