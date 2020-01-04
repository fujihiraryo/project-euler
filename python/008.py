S=input()
N=len(S)
A=0
for i in range(N-13):
    T=S[i:i+13]
    x=1
    for t in T:
        x*=int(t)
    if A<x:
        A=x
print(A)
