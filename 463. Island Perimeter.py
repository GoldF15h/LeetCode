def sol(grid):
    ans = 0
    h = len(grid)
    w = len(grid[0])

    # เช็คแนวนอน
    for i in range(h) :
        if grid[i][0] == 1 :
            ans += 1
        if grid[i][w-1] == 1 :
            ans += 1
        for j in range(w-1) :
            if grid[i][j] != grid[i][j+1] :
                ans += 1

    # เช็คแนวตั้ง
    for i in range(w) :
        if grid[0][i] == 1:
            ans += 1
        if grid[h-1][i] == 1:
            ans += 1
        for j in range(h-1) :
            if grid[j][i] != grid[j+1][i] :
                ans += 1

    return ans
        

if __name__ == "__main__" :
    grid = [ list(map(int,x.strip('],').split(','))) for x in input().strip('[]').split('[') ]
    print(sol(grid))