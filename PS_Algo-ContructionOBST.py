# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current=self
		if(current.value>value):
			if(current.left is None):
				current.left=BST(value)
			else:
				current.left.insert(value)
		else:
			if(current.right is None):
				current.right=BST(value)
			else:
				current.right.insert(value)


    def contains(self, value):
		current=self
        if(not current):
			return
		if(current.value==value):
			return True
		else:
			if(value<current.value and current.left):
				return current.left.contains(value)
			elif(value>current.value and current.right):
				return current.right.contains(value)
			else:
				return False

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		if(self.value==value):
			if(not self.right):
				current=self.left
				if(current):
					self.value=current.value
					self.left=current.left
					self.right=current.right
				else:
					self=self.left
			else:
				current=self.right
				if(not current.left):
					self.value=current.value
					self.right=current.right
				else:
					while(current.left):
						prev=current
						current=current.left
					self.value=current.value
					prev.left=None
		else:
			if(self.value>value and self.left):
				self.left=self.left.remove(value)
			elif(self.value<value and self.right):
				self.right=self.right.remove(value)
			else:
				return
        return self
