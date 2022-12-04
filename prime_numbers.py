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
	
	# function to calculate prime numbers in between given range
	#Enter the two input in which we have to find the prime numbers
	def between_range(self,a,b):
		self.a=a
		self.b=b
		checkprime=[0]*(10**5+1)
		for i in range(b+1):
			checkprime[i]=1
		#print(checkprime)
		for i in range(2,10**5+1):
			if checkprime[i]==1:
				for j in range(2,10**5+1):
					if i*j<10**5:
						checkprime[i*j]=0
		#print(checkprime)
		for i in range(a,b+1):
			if checkprime[i]==1:
				print(i,end=" ")
p=prime(int(input()))
