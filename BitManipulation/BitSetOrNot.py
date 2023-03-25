def BitSetOrNot(n,i):
     if ((n&1<<i)==0):
         return False
     else:
         return True
print(BitSetOrNot(16,4))
