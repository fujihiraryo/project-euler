def comb(n,r):
    up=1
    for i in range(r+1,n+1):
        up*=i
    down=1
    for i in range(1,r+1):
        down*=i
    return up//down

print(comb(40,20))
