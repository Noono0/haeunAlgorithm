import sys
import time
import itertools


start = time.time() 
sys.stdin=open("input.txt", "r")
#import math
#n = int(sys.stdin.readline())



n ,m = map(int,input().split())

nArr = [ i+1 for i in range(n)]
checkArr = [False]*n
realArr = []
start = 1

def chk(start):
  if len(realArr) == m:
    #print(*realArr)
    print(' '.join(map(str,realArr)))
    return

  for i in range(n):
    if checkArr[i]:
      continue
    
    realArr.append(nArr[i])
    checkArr[i] = True

    chk(start+1)
    
    realArr.pop()
    #checkArr[i] = False

    # 이 부분으로 바꿔준다 print(j)로 디버깅해보면 어떻게되는지 알수있다.
    for j in range(i+1,n):
      checkArr[j] = False

chk(start)










print("")
print("time:",time.time() - start)



