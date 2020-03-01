p = 10**9 + 7


def cmb(n, a):
    ans = 1
    for i in range(1, a + 1):
        ans = ans * (n - i + 1) // i
    return ans


def g(n, m):
    x = cmb(n, m)
    cnt = 0
    while x % 2 == 0:
        x = x // 2
        cnt += 1
    return cnt


def F(n):
    return max([g(n, m) for m in range(n // 2 + 1)])


def S(N):
    return sum([F(n) for n in range(1, N + 1)])


def f(k):
    # 第k群の和
    return sum([j * 2**(j - 1) for j in range(1, k + 1)])


def h(k, m):
    # 第k群のm項目までの和
    return sum([((m + 2**(k - j)) // 2**(k - j + 1)) * j
                for j in range(1, k + 1)])


def gr(n):
    # nが第何群に属するか
    k = 0
    tmp = n
    while tmp // 2 > 0:
        tmp = tmp // 2
        k += 1
    return k


def s(n):
    # 第n項までの和
    k = gr(n)
    m = n - 2**k + 1
    return sum([f(i) for i in range(1, k)]) + h(k, m)


print(s(100))
print(s(10**7))
print(s(10**16))
