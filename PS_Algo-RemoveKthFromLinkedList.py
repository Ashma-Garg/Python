# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.

	prev=head
	rev(head,prev,k)

def rev(head,prev,k):
	h1=head
	for i in range(k):
		h1=h1.next
	if not h1:
		if(prev.value==head.value):
			prev.value=head.next.value
			prev.next=head.next.next
		else:
			prev.next=head.next
	else:
		if(head.next):
			rev(head.next,head,k)
