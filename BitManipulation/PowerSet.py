def PowerSet(s):
    n=len(s)
    for i in range(2**n):
        for j in range(len(s)):
            if ((i>>j)&1):
                print(s[j],end=" ")
        print()
PowerSet([1,2,3])
