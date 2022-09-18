n, m, k = map(int, input().split())
ans = 0
for i in range(n-k+1, n+1):
    ans = (ans + m) % i
             
print(ans + 1)