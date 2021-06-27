# {
#   "tree": {
#     "nodes": [
#       {"id": "1", "left": "2", "right": "3", "value": 1},
#       {"id": "2", "left": "4", "right": "5", "value": 2},
#       {"id": "3", "left": "6", "right": "7", "value": 3},
#       {"id": "4", "left": "8", "right": "9", "value": 4},
#       {"id": "5", "left": "10", "right": null, "value": 5},
#       {"id": "6", "left": null, "right": null, "value": 6},
#       {"id": "7", "left": null, "right": null, "value": 7},
#       {"id": "8", "left": null, "right": null, "value": 8},
#       {"id": "9", "left": null, "right": null, "value": 9},
#       {"id": "10", "left": null, "right": null, "value": 10}
#     ],
#     "root": "1"
#   }
# }
#
# Our Code's Output
# [15, 16, 18, 10, 11]

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
	add=list()
	i=0
	ar=list()
	sumTree(root,add,ar)
	return ar
def sumTree(root,add,ar):
	if(not root):
		return

	if(root.value is not None):
		add.append(root.value)

	if(root.left is None and root.right is None):
		a=sum(add)
		ar.append(a)
	else:
		sumTree(root.left,add,ar)
		sumTree(root.right,add,ar)
	del add[-1]
