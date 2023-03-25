#check if the given number is power of 2 or not
def isPowerOfTwo(n):
    if n==0:
        return False
    if (n & ~(n-1))==n:
        return True
    else:
        return False
print(isPowerOfTwo(int(input())))
