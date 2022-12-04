import math
class prime:
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
