from tools import prime_factrization
N=20
A={}
for i in range(2,N+1):
    B=prime_factrization(i)
    for key in B.keys():
        try:
            A[key]=max(A[key],B[key])
        except:
            A[key]=B[key]
ans=1
for key in A.keys():
    ans*=key**A[key]
print(ans)
