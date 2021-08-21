def taskAssignment(k, task):
    # Write your code here.
	arr=sorted(task)
	l=list()
	length=len(task)
	for i in range(k):
		l.append([task.index(arr[i]),task.index(arr[length-i-1])])
		task[task.index(arr[i])]=task[task.index(arr[length-i-1])]=-1
    return l
