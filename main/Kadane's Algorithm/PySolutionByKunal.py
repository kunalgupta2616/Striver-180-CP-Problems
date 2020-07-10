from sys import maxsize
class kadane:
	def __init__(self, arr):
		self.arr=arr
		meh= 0
		size=len(self.arr)
		msf= -maxsize-1
		s= e=0
		temp=0
		for i in range(0, size):
			meh=meh+arr[i]
			if msf<meh:
				msf=meh
				s=temp
				e=i
			if meh<0:
				meh=0
				temp=i+1
		self.maxsum=msf
		self.span=(s, e+1)
		return None
