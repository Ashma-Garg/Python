def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
	array={
		'1':'1',
		'2':'abc',
		'3':'def',
		'4':'ghi',
		'5':'jkl',
		'6':'mno',
		'7':'pqrs',
		'8':'tuv',
		'9':'wxyz',
		'0':'0'
	}

	# this creates an array of phonenumber's length with 0 value of every index
	c=["0"]*len(phoneNumber)
	mf=list()
	phoneNumberMF(0,array,phoneNumber,c,mf)
	return mf
def phoneNumberMF(index,array,phoneNumber,c,mf):
	if index==len(phoneNumber):
		m="".join(c)
		mf.append(m)
	else:
		letters=array[phoneNumber[index]]
		for letter in letters:
			c[index]=letter
			phoneNumberMF(index+1,array,phoneNumber,c,mf)
