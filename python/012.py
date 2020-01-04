from tools import prime_factrization
X=0
N=1
while X<500:
    N+=1
    A=sum(range(1,N+1))
    prime_factors=prime_factrization(A)
    divisors_count=1
    for i in prime_factors.values():
        divisors_count*=(i+1)
    if X<divisors_count:
        X=divisors_count
print(A)
