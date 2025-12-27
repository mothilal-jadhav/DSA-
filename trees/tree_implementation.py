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
        print(str(node.data) + ' -> ' + str(parent.data))

    for child in node.children:
        printParent(child,node)

# function to print children of node

def printChildren(node):
    children_str = " ".join(str(child.data) for child in node.children)
    print(str(node.data) + " -> " + children_str)
    for child in node.children:
        printChildren(child)


# function to print leadnodes

def leafNodes(node):
    if not node.children:
        print(str(node.data))
        return
    
    for child in node.children:
        leafNodes(child)


# degree of nodes

def degree(node,parent=None):
    deg = len(node.children)

    if parent is not None:
        deg += 1

    print(str(node.data) + " -> " + str(deg))

    for child in node.children:
        degree(child,node)

root = Node(1)
child1 = Node(2)
child2 = Node(3)
child3 = Node(4)

addChild(root, child1)
addChild(root, child2)
addChild(child1, child3)

printParent(root,None)
print("\nLeaf Nodes:")
leafNodes(root)
print("\nchildren of Nodes:")
printChildren(root)
print("\nDegrees:")
degree(root)
