def kadane(a):
    max_sum=a[0]
    cur_sum=a[0]
    for i in range(1,len(a)):
        cur_sum=max(a[i],cur_sum+a[i])
        max_sum=max(max_sum,cur_sum)
    #print(max_sum)
    return max_sum

#arr=[[1,2,-1,-4,-20],[-8,-3,4,2,1],[3,8,10,1,3],[-4,-1,1,7,-6]]
arr=[[24, -43, 3, 28, -48, 61], [-53, 37, -41, -25, 12, -59]]
#arr=[[-10,-20,-30,-40],[-10,20,-5,-10],[-10,-5,20,-10],[-10,-20,-30,-40]]
#print(arr)
gsum=float('-inf')
for left in range(len(arr[0])):
    temp=[0]*len(arr)
    for right in range(left,len(arr[0])):
        for i in range(len(arr)):
            temp[i]+=arr[i][right]
        #print(temp)
        Sum=kadane(temp)
        if Sum>gsum:
            gsum=Sum
print(gsum)
