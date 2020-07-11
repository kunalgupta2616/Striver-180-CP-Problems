def repAndMissNums(arr):
	size= len(arr)
	sumN= (size*(size+1))//2
	miss=0
	rep=0
	sumsq= (sumN*(2*size+1)) //3
	for i in range(size):
		sumN-= arr[i]
		sumsq-=(arr[i]*arr[i]) 
		miss = (sumN+sumsq//sumN)//2
		rep = miss-sumN
	return ("Missing number = {}\nRepeating number = {}".format(miss, rep))
