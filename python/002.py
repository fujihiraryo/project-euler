A=[1,2]
while A[-1]<4000000:
    A.append(A[-1]+A[-2])
A=A[:-1]
print(sum([a for a in A if a%2==0]))
