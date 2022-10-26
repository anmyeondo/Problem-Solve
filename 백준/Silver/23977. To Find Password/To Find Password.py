from sys import stdin

def get_gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def get_lcm(a, b):
    return (a*b)//get_gcd(a, b)

k, n = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))

lcm = get_lcm(arr[0], arr[1])
for i in range(1, len(arr)):
    lcm = get_lcm(lcm, arr[i])

print(lcm - k)