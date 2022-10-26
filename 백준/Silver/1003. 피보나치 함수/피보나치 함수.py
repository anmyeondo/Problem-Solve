from sys import stdin

z = [1,0,1]
o = [0,1,1]

def fibo(n):
    l = len(z)
    if l <= n:
        for i in range(l, n+1):
            z.append(z[i-1] + z[i-2])
            o.append(o[i-1] + o[i-2])

tc = int(stdin.readline().rstrip())

for i in range(tc):
    n = int(stdin.readline().rstrip())
    fibo(n)
    
    print(z[n], o[n])
