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

def prime_sieve(N):
    if N < 2:
        return []
    search_list = list(range(2, N + 1))
    prime_list = []
    while search_list[0] <= N ** 0.5:
        prime_list.append(search_list[0])
        tmp = search_list[0]
        search_list = [i for i in search_list if i % tmp != 0]
    prime_list.extend(search_list)
    return prime_list
