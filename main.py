import sys
import time
import itertools


start = time.time() 
sys.stdin=open("input.txt", "r")
#import math
#n = int(sys.stdin.readline())



n ,m = map(int,input().split())
#print(n,m)
arr = list(map(int,input().split()))

tmp =[]
def chk(start):
  if len(tmp) == m:
    print(' '.join(map(str,tmp)))
    return

  for i in range(start,n+1):
      tmp.append(arr[i])
      chk(i)
      #print("t",tmp)
      tmp.pop()
      


chk(1)












print("")
print("time:",time.time() - start)



