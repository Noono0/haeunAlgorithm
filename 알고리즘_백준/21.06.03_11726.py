n = int(input())

dp = [0 for _ in range(n+1)]


for i in range(n+1):
  if i == 1:
    dp[i] = 1
  elif i == 2:
    dp[i] = 2  
  else:
    dp[i] = dp[i-2]*2 + dp[i-1]

print("dp:",dp[n] % 10007)


#input:
#      9