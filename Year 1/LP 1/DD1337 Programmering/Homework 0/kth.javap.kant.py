R, K = map(int, input().split())
for r in range(R):
    for k in range(K):
        s = min([r, k, R-r-1, K-k-1]) + 1
        print(s if s < 10 else ".", end="")
    print()