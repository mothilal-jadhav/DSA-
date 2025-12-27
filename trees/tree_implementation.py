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
        print(str(node.data)+ ' -> ' str(parent.data))

    for child in node.children:
        printParent(child,node)


