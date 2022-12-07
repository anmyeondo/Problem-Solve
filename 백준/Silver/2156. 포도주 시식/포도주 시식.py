n = int(input())
dp = [0 for _ in range(n+1)]
wines = [0 for _ in range(n+1)]

for i in range(n):
    wines[i] = int(input())
if n == 1:
    print(wines[0])
    exit(0)

elif n == 2:
    print(wines[0] + wines[1])
    exit(0)

dp[0] = wines[0]
dp[1] = wines[0] + wines[1]
dp[2] = max(wines[2]+wines[0], wines[2]+wines[1], dp[1])

for i in range(3, n):
    dp[i] = max(wines[i]+dp[i-2], wines[i]+wines[i-1]+dp[i-3], dp[i-1])

print(dp[n-1])