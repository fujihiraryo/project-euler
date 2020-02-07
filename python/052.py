for i in range(1, 10 ** 7):
    S = set()
    S.add(tuple(sorted(list(str(i)))))
    S.add(tuple(sorted(list(str(2*i)))))
    S.add(tuple(sorted(list(str(3*i)))))
    S.add(tuple(sorted(list(str(4*i)))))
    S.add(tuple(sorted(list(str(5*i)))))
    S.add(tuple(sorted(list(str(6*i)))))
    if len(S) == 1:
        print(i, 2*i, 3*i, 4*i, 5*i, 6*i)
        exit()
