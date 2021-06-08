import sys
import time

start = time.time() 
sys.stdin=open("input.txt", "r")
#import math
#n = int(sys.stdin.readline())

s = []
for i in range(9):
    s.append(int(input()))
sum_s = sum(s)
one = 0
two = 0
for i in range(8):
    for j in range(i + 1, 9):
        if sum_s - (s[i] + s[j]) == 100:
            one = s[i]
            two = s[j]
s.remove(one)
s.pop(two)
s.sort()
for i in s:
    print(i)

# combination 을 쓰지않고 for문으로만 풀어보았다.
# 핵심은 sum(list) 에서 2개를 빼 100을 맞추는것!




print("")
print("time:",time.time() - start)



