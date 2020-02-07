"""
pが素数で、入力が
n r p
で与えられたときnCrをmod pで計算する
"""

n, p = 100, 10**9+7


g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range(2, n + 1):
    g1.append((g1[-1] * i) % p)
    inverse.append((-inverse[p % i] * (p//i)) % p)
    g2.append((g2[-1] * inverse[-1]) % p)

# print(g1)
# print(g2)
# print(inverse)


def cmb(n, r, p):
    if (r < 0 or r > n):
        return 0
    return g1[n] * g2[r] * g2[n-r] % p


cnt = 0
for n in range(1, 100 + 1):
    for r in range(1, n + 1):
        if cmb(n, r, p) > 1000000:
            cnt += 1
print(cnt)
