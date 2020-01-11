def d(n):
    S = 0
    for i in range(1, n):
        if n % i == 0:
            S += i
    return S


N = 30000

abundant_list = []
for n in range(2, N):
    if n < d(n):
        abundant_list.append(n)

print("###")

search_list = [n for n in range(1, 28123 + 1)]
ng_set = set()
for x in abundant_list:
    for y in abundant_list:
        if x + y <= 28123:
            ng_set.add(x+y)

print(sum(search_list)-sum(ng_set))
