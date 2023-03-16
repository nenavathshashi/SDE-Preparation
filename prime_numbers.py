import math
class prime:
	#time complexity of finding a whether the given number is prime or not is O(sqrt(n))
	def linearTime(self,n):
		self.n=n
		#if it is 0 or 1 in every case it is not a prime.Hence return here itself
		if n<=1:
			return "Not a Prime"
		#using a flag variable to determine if atleast 1 factor other than 1 and itself is possible or not
		flag=0
		for i in range(2,n+1):
			#if extra factor found set flag variable and break
			if n%i==0:
				flag=1
				break
		if flag==0:
			return "Is Prime"
		else:
			return "Not a Prime"
	#time complexity of finding a whether the given number is prime or not is O(sqrt(n))
	def sqrtTime(self,n):
		self.n=n
		# print(n)
		flag=0
		for i in range(2,int(math.sqrt(n))+1):
			#print(i,n%i)
			if n%i==0:
				flag=1
				break
		if flag==0:
			return "Is Prime"
		else:
			return "Not a Prime"
	#time complexity of finding a whether the given number is prime or not is O(nlog(log(n)))
	def Seive(self,n):
		self.n=n
		IsPrime=[True for i in range(10**6+1)]
		IsPrime[0]=False
		IsPrime[1]=False
		for i in range(2,int(math.sqrt(10**6+1))+1):
			if IsPrime[i]==True:
				j=2
				while(i*j<=10**6):
					IsPrime[i*j]=False
					j+=1
		if not IsPrime[n]:
			return "Not a prime"
		else:
			return "Is Prime"
	# function to calculate prime numbers in between given range
	#Enter the two input in which we have to find the prime numbers
	def between_range(self,a,b):
		self.a=a
		self.b=b
		IsPrime=[True for i in range(10**6+1)]
		IsPrime[0]=False
		IsPrime[1]=False
		for i in range(2,int(math.sqrt(10**6+1))+1):
			if IsPrime[i]==True:
				j=2
				while(i*j<=10**6):
					IsPrime[i*j]=False
					j+=1
		#print(checkprime)
		for i in range(a,b+1):
			if IsPrime[i]==True:
				print(i,end=" ")
p=prime()
n=int(input())
print(p.Seive(n))
print(p.linearTime(n))
print(p.sqrtTime(n))
p.between_range(0,100)
