N = 1000


def length_of_cycle(d):
    memo = [0 for _ in range(N)]
    r = 10 % d
    count = 0
    while memo[r] == 0:
        count += 1
        memo[r] = count
        r = 10 * r % d
        if r == 0:
            return 0
    return count-memo[r]+1


max_length = 0
for d in range(1, N + 1):
    length = length_of_cycle(d)
    if length > max_length:
        max_length = length
        argmax = d
print(argmax)
