
import sys
import time
import itertools


start = time.time() 
sys.stdin=open("input.txt", "r")
#import math
#n = int(sys.stdin.readline())



n ,m = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
checkArr = [False]*n
realArr = []
start = 1
idx = 0
moreChk = []

def chk(start):
  if len(realArr) == m:
    #print("real",realArr,"more1",moreChk)
    if True:
      print("real",realArr)
      moreChk.append(realArr)
      print("more",moreChk)
      #print(' '.join(map(str,realArr)))
      return

  for i in range(n):
    if checkArr[i] != False:
      continue
    
    realArr.append(arr[i])
    
    checkArr[i] = arr[i]

    chk(start+1)
    
    realArr.pop()
    checkArr[i] = False
    #for j in range(i+1,n):
      #print("j:",)
      #checkArr[j] = False

chk(start)




print("")
print("time:",time.time() - start)