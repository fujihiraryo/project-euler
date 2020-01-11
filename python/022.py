name_list = [name[1:-1] for name in list(input().split(','))]
name_list.sort()
alphabet_list = [chr(i) for i in range(65, 65+26)]
alphabet_map = {}
for n in range(26):
    alphabet_map[alphabet_list[n]] = n + 1

print(alphabet_map)
ans = 0
N = len(name_list)
print(N)
for n in range(N):
    name = name_list[n]
    score = 0
    for char in name:
        score += alphabet_map[char]
    if n % 100 == 0:
        print(name, score)
    ans += score * (n + 1)
print(ans)
