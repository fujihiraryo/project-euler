N=1000000

def collatz_count(x):
    n=x
    a=[n]
    count=1
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        count+=1
    return count

argmax=1
m=0
for x in range(2,N+1):
    if m<collatz_count(x):
        argmax=x
        m=collatz_count(x)
print(argmax)
