a, b = 3, 2
cnt = 0
for i in range(1000):
    a, b = a + 2 * b, a + b
    if len(str(a)) > len(str(b)):
        cnt += 1
print(cnt)
