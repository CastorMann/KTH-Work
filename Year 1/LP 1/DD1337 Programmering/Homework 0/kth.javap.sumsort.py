from math import ceil
n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
s = 0
for i in range(ceil(n/2)): s += data[i]
print(s)