def CountSetBits(n):
    count=0
    while(n!=0):
        print(n)
        count+=1
        n=n&(n-1)
    return count
print(CountSetBits(20))
