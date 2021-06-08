import sys
import time
import itertools


start = time.time() 
sys.stdin=open("input.txt", "r")
#import math
#n = int(sys.stdin.readline())



n = int(input())
a = list(map(int, input().split()))
sum = [a[0]]
for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
print(max(sum))

print(sum)




print("")
print("time:",time.time() - start)



