def is_Lychrel(n):
    a = n+int(str(n)[::-1])
    for i in range(50):
        b = int(str(a)[::-1])
        if a == b:
            return False
        else:
            a = a + b
    return True


print(is_Lychrel(349))
print(is_Lychrel(4994))
print(sum([int(is_Lychrel(n)) for n in range(1, 10000)]))
