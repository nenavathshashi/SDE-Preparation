import math
class prime:
	#time complexity of finding a whether the given number is prime or not is O(sqrt(n))
	def __init__(self,n):
		self.n=n
		# print(n)
		flag=0
		for i in range(2,int(math.sqrt(n))+1):
			#print(i,n%i)
			if n%i==0:
				flag=1
				break
		if flag==0:
			print(True)
		else:
			print(False)
p=prime(int(input()))
