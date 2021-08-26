def reverseWordsInString(string):
	arr=list()
	word=""
	for i in range(len(string)):
		if(string[i]==" "):
			word=" "+word
			arr.append(word)
			word=""
		else:
			word=word+string[i]


	arr.append(word)
	arr.reverse()
	st="".join(arr)
    return st
