def d(n):
    S = 0
    for i in range(1, n):
        if n % i == 0:
            S += i
    return S


X = {}
for n in range(10000):
    X[n] = d(n)
print(X)
S = 0
for n in range(1, 10000):
    for m in range(n + 1, 10000):
        if n == X[m] and m == X[n]:
            print(X[n], X[m])
            S += X[n] + X[m]
print(S)
