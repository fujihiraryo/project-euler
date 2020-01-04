def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True


N=600851475143
for i in range(2,int(N**0.5)+1):
    if N%i==0:
        if is_prime(i):
            p=i
print(p)
