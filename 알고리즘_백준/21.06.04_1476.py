import sys
import time
import itertools
from itertools import combinations
start = time.time() 
sys.stdin=open("input.txt", "r")
#import math
#n = int(sys.stdin.readline())

E, S, M = map(int, input().split())
year = 1

while True:
  if (year - E)%15 == 0 and (year - S)%28 == 0 and (year - M)%19 == 0:
    print(year)
  year+=1











print("")
print("time:",time.time() - start)



