import sys
import time
import itertools
from itertools import combinations
start = time.time() 
sys.stdin=open("input.txt", "r")
#import math
#n = int(sys.stdin.readline())
a=[]
res=''
for i in range(9):
  a.append(int(input()))

comb = list(combinations(a,7))

for i in comb:
  if sum(i) == 100:
    res=sorted(i)
  
for j in res:
  print(int(j))

# combination 으로 풀어봤다 
# 근데 검색해보니 combination 도 2중for 문으로 푸는방식이라
# 시간복잡도가 더 심하다는 말이있는데.. 자세히는 잘안나온다..

print("")
print("time:",time.time() - start)



