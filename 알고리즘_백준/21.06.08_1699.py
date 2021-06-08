import sys
import time
import itertools


start = time.time() 
sys.stdin=open("input.txt", "r")
#import math
#n = int(sys.stdin.readline())



n = int(input())
dp = [0 for i in range(n + 1)]
square = [i * i for i in range(1, 317)]
for i in range(1, n + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j])
    dp[i] = min(s) + 1
print(dp[n])



print("")
print("time:",time.time() - start)



