# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
def j(tree,array):
	array.append(tree.name)
	i=0
	while(i<len(tree.children)):
		j(tree.children[i],array)
		i=i+1
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
		j(self,array)
		return array
