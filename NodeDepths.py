# Node depth is sum of heights of every node element

def nodeDepths(root):
    # Write your code here.
	i=0
	add=[0]
	depth(root,i,add)
	return add[0]
    pass
def depth(root,i,add):
	if(not root):
		return
	add[0]=add[0]+i
	depth(root.left,i+1,add)
	depth(root.right,i+1,add)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
