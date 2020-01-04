def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

def prime_factrization(N):
    result={}
    tmp=N
    for i in range(2,int(N**0.5)+1):
        result[i]=0
        while tmp%i==0:
            tmp//=i
            result[i]+=1
        if result[i]==0:
            result.pop(i)
    if tmp!=1:
        result[tmp]=1
    if result=={}:
        result[N]=1
    return result
