# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(l1, l2):
	linkedListOne=l1
	linkedListTwo=l2
	sumN=LinkedList(0)
	sumNode=sumN
	carry=0
	while linkedListOne or linkedListTwo:
		if linkedListTwo:
			l2v=linkedListTwo.value
		else:
			l2v=0
		if linkedListOne:
			l1v=linkedListOne.value
		else:
			l1v=0
		add=l1v+l2v+carry
		print(add)
		rem=add%10
		sumNode.value=rem
		carry=int(add/10)

		if((linkedListOne and linkedListOne.next) or (linkedListTwo and linkedListTwo.next) or not carry==0):
			newNode=LinkedList(carry)
			sumNode.next=newNode
			sumNode=sumNode.next

		if linkedListOne:
			linkedListOne=linkedListOne.next
		if linkedListTwo:
			linkedListTwo=linkedListTwo.next
    return sumN
