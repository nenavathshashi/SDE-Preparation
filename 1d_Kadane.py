class Kadane:
    def __init__(self,a):
        self.a_left=[0]*len(a)
        self.a_right=[0]*len(a)
    def Kadane(self,a):
        max_sum=a[0]
        cur_sum=a[0]
        self.a_left[0]=a[0]
        for i in range(1,len(arr)):
            cur_sum=max(a[i],a[i]+cur_sum)
            self.a_left[i]=cur_sum
            max_sum=max(max_sum,cur_sum)
        return max_sum
    def ReverseKadane(self,a):
        max_sum=a[-1]
        cur_sum=a[-1]
        self.a_right[-1]=a[-1]
        for i in range(len(a)-1,-1,-1):
            cur_sum=max(a[i],a[i]+cur_sum)
            self.a_right[i]=cur_sum
            max_sum=max(max_sum,cur_sum)
        return max_sum
    def subarray(self,a,maxi1,maxi2):
        print(self.a_left,self.a_right)
        return self.a_left.index(maxi1),self.a_right.index(maxi2)
arr=[2, -3, 4, -1, -2, 1, 5, -3]
k=Kadane(arr)
maxi1=k.Kadane(arr)
maxi2=k.ReverseKadane(arr)
start,end=k.subarray(arr,maxi1,maxi2)
print(start,end)
