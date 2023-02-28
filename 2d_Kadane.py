'''# your code goes here
#queue using list
#the enque and deque operation takes o(n) time
list1=[]
list1.append(1)
list1.append(2)
list1.append(3)
print(list1)
print(list1.pop(0))
print(list1.pop(0))
print(list1.pop(0))
print(list1)

#queue using deque from collections
#the enque and deque operation takes o(1) time
from collections import deque
q=deque()
print(q)
q.append(1)
q.append(2)
q.append(3)
print(q)
print(q.popleft())

from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)'''

'''Subset Sum
#n=6
#s=8
#a=[4,10,9,3,1,3]
#i=j=0
#sums=0
#maxi=0
#while(j<n):
    #sums+=a[j]
    #j+=1
    #while(sums>s):
        #sums-=a[i]
        #i+=1
    #if(sums<=s):
        #maxi=max(maxi,j-i)
    #print(maxi,sums)
#print(maxi)
'''
#def merge(l,low,mid,high):
    #print(l[low:mid+1],l[mid+1:high+1])
    #i=low
    #j=mid+1
    #k=0
    #print(i,j)
    #while(i<=mid and j<=high):
        #if l[i]>l[j]:
            #print(l[j])
            #j+=1
        #else:
            #print(l[i])
            #i+=1
        #k+=1
    #while(i<=mid):
        #print(l[i])
        #i+=1
    #while(j<=high):
        #print(l[j])
        #j+=1
#def divide(l,low,high):
    #if low<high:
        #mid=(low+high)//2
        #divide(l,low,mid)
        #divide(l,mid+1,high)
        #merge(l,low,mid,high)

#l=[4,1,18,19,2,15,10]
#divide(l,0,len(l)-1)


#from functools import *
#def compare(x,y):
    #xsums=0
    #ysums=0
    #for i in range(len(x)):
        #xsums+=ord(x[i])
    #for i in range(len(y)):
        #ysums+=ord(y[i])
    #if xsums==ysums:
        ##print("comparision type 2")
        #return ord(x[0])>ord(y[0])
    #else:
        ##print("comparision type 1")
        #return xsums-ysums
#def compare1(x,y):
    #return len(x)-len(y)
#t=1
#for i in range(t):
    #n=8
    #l=['bat','tea','abc','tan','bac','ate','eat','nat']
    #l.sort()
    #semi=sorted(l,key=cmp_to_key(compare))
    #d={}
    #for j in range(n):
        #xsums=0
        #x=l[j]
        #for i in range(len(x)):
            #xsums+=ord(x[i])
        #if d.get(xsums)==None:
            #d[xsums]=[x]
        #else:
            #d[xsums].append(x)
    ##print(d)
    #result=list(d.values())
    ##print(result)
    #final=sorted(result,key=cmp_to_key(compare1))
    #print(final)


#def search(a,l,h,target):
    #mid=(l+h)//2
    #if target==a[mid]:
        #return mid
    #elif target>=a[l] and target<a[mid]:
        #return search(a,l,mid-1,target)
    #else:
        #return search(a,mid+1,h,target)
#print(search([4,5,6,7,0,1,2,3],0,7,0))

#import cv2
#import numpy as np

## Load the signature image
#signature = cv2.imread("signature.jpeg", cv2.IMREAD_GRAYSCALE)

## Binarize the image using adaptive thresholding
#binary = cv2.adaptiveThreshold(signature, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                #cv2.THRESH_BINARY, 25, 5)

## Reduce noise using median filtering
#median_size = 1
#binary = cv2.medianBlur(binary, median_size)

## Enhance contrast using histogram equalization
#binary = cv2.equalizeHist(binary)

## Normalize the size of the signature
#target_size = (400, 100)
#binary = cv2.resize(binary, target_size)

## Save the preprocessed image
#cv2.imwrite("preprocessed_signature.jpg", binary)
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
