def is_palindrome(N):
    return str(N)==str(N)[::-1]
a=0
for i in range(1000):
    for j in range(i+1,1000):
        if is_palindrome(i*j) and a<i*j:
            a=i*j
print(a)
