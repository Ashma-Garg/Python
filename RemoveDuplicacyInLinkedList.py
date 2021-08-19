# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
	def get_prev_node(self, ref_node):
        current = self
        while (current and current.next != ref_node):
            current = current.next
        return current
	def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self = self.next
        else:
            prev_node.next = node.next


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	# print(linkedList.value)
	l1=linkedList
	while(l1 is not None and l1.next is not None):
		l2=l1
		while(l2 is not None and l2.next is not None):
			print(l2.value)
			if(l1.value == l2.next.value):
				dup=l2.next
				l2=l2.next
				linkedList.remove(dup)
			else:
				l2=l2.next
		l1=l1.next
    return linkedList
