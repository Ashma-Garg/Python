# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
	arr=list()
	f=node.value
	prev=tree
	successor(tree,node,arr,prev)
	if(type(arr[0]) is int):
		return None
	else:
		return arr[0]
    # return arr[0]

def successor(tree,node,arr,prev):
	if(not tree):
		return
	successor(tree.left,node,arr,tree)
	if(arr):
		last=arr.pop()
		if(last==node.value):
			arr.clear()
			arr.append(tree)
		else:
			arr.append(last)
	arr.append(tree.value)
	successor(tree.right,node,arr,tree)
