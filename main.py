
import sys
import time
import itertools


start = time.time() 
sys.stdin=open("input.txt", "r")
#import math
#n = int(sys.stdin.readline())
#d
############################

n = int(input())

array = list(map(int,input().split()))

d = [0] * 100001

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
  d[i] = max(d[i-1], d[i-2]+array[i])

  print(d[n-1])
  














#############################


print("")
print("time:",time.time() - start)