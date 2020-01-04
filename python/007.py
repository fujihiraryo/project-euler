from tools import is_prime
n=1
count=0
while count<10001:
    n+=1
    if is_prime(n):
        count+=1
print(n)