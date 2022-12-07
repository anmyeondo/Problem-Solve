n = int(input())
l = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(n):
    tmp = 0
    for j in range(i):
        if l[i]>l[j]:
            if tmp < dp[j]:
                tmp = dp[j]
    dp[i] = tmp + 1

print(max(dp))
