# strucutre of tree 

class Node:
    def __init__(self,data):
        self.data = data
        self.children = []

 # function to add child to node   
def addChild(parent,child):
    parent.children.append(child)


