import sys
import time
import itertools
from itertools import combinations
start = time.time() 
sys.stdin=open("input.txt", "r")
#import math
#n = int(sys.stdin.readline())


a=int(input())
for i in range(a):
  n = int(input())

  dp = [0]*(n+1)
  dp[0] = 1
  dp[1] = 2
  dp[2] = 4
  for j in range(3,n+1):
    dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
  
   
  print(dp[n-1])

  

  


    







print("")
print("time:",time.time() - start)



