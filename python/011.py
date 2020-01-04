grid=[list(map(int,input().split())) for _ in range(20)]
A=0
for h in range(20-4):
    for w in range(20-4):
        tate1=grid[h][w]*grid[h+1][w]*grid[h+2][w]*grid[h+3][w]
        tate2=grid[h][w+1]*grid[h+1][w+1]*grid[h+2][w+1]*grid[h+3][w+1]
        tate3=grid[h][w+2]*grid[h+1][w+2]*grid[h+2][w+2]*grid[h+3][w+2]
        tate4=grid[h][w+3]*grid[h+1][w+3]*grid[h+2][w+3]*grid[h+3][w+3]
        yoko1=grid[h][w]*grid[h][w+1]*grid[h][w+2]*grid[h][w+3]
        yoko2=grid[h+1][w]*grid[h+1][w+1]*grid[h+1][w+2]*grid[h+1][w+3]
        yoko3=grid[h+2][w]*grid[h+2][w+1]*grid[h+2][w+2]*grid[h+2][w+3]
        yoko4=grid[h+3][w]*grid[h+3][w+1]*grid[h+3][w+2]*grid[h+3][w+3]
        naname1=grid[h][w]*grid[h+1][w+1]*grid[h+2][w+2]*grid[h+3][w+3]
        naname2=grid[h][w+3]*grid[h+1][w+2]*grid[h+2][w+1]*grid[h+3][w]
        B=max(tate1,tate2,tate3,tate4,yoko1,yoko2,yoko3,yoko4,naname1,naname2)
        if A<B:
            A=B
print(A)
