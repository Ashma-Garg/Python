
def findClosestValueInBst(tree, target):
    # Write your code here.
	MAX_DIFF=9999999
	key=[-1]
	closest(tree, target , MAX_DIFF, key)
	return key[0]
# This is the class of the input tree. Do not edit.
def closest(tree, target , MAX_DIFF, key):
	if(not tree):
		return
	if(target==tree.value):
		MAX_DIFF=abs(target-tree.value)
		key[0]=tree.value
	if(MAX_DIFF>abs(target-tree.value)):
		MAX_DIFF=abs(target-tree.value)
		key[0]=tree.value
	if target < tree.value:
		closest(tree.left, target,MAX_DIFF,key)
	else:
		closest(tree.right, target,MAX_DIFF,key)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
