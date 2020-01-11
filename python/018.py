N = 15
X = []
for n in range(N):
    Xn = list(map(int, input().split()))
    X.append(Xn)


def ans(X):
    N = len(X)
    if N == 1:
        return X[0][0]
    else:
        X0 = [X[n][:n] for n in range(1, N)]
        X1 = [X[n][1:] for n in range(1, N)]
        return X[0][0]+max(ans(X0), ans(X1))


print(ans(X))
