M = 0
for a in range(1, 100 + 1):
    for b in range(1, 100 + 1):
        X = sum([int(_) for _ in str(a ** b)])
        if X > M:
            M = X
