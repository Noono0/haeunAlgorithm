
import sys
import time
import itertools


start = time.time() 
sys.stdin=open("input.txt", "r")
#import math
#n = int(sys.stdin.readline())
#d
############################


input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-1,-2), ()]

result =0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]

  if next_row >= 1 and next_row





#############################


print("")
print("time:",time.time() - start)