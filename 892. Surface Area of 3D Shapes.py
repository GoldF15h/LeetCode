def sol (grid) :
    ans = 0

    # top 
    for curRow in range(len(grid)) :
        for curCol in range(len(grid[curRow])) :
            if grid[curRow][curCol] > 0 :
                ans += 2

    # rowSum
    # print('ROW RUN')
    for curRow in range(len(grid)) :
        cur = 0
        add = 0
        for curCol in range(len(grid[0])) :
            # print('add',abs(cur-grid[curRow][curCol]))
            add += abs(cur-grid[curRow][curCol])
            cur = grid[curRow][curCol]
        # print('add',cur)
        ans += (add+cur)

    # colSum
    # print('COL RUN')
    for curCol in range(len(grid[0])) :
        cur = 0
        add = 0
        for curRow in range(len(grid)) :
            # print('add',abs(cur-grid[curRow][curCol]))
            add += abs(cur-grid[curRow][curCol])
            cur = grid[curRow][curCol]
        # print('add',cur)
        ans += (add+cur)

    return ans

if __name__ == "__main__" :
    l = list( list(map(int,x.split(','))) for x in input().strip('[]').split('],['))
    print(sol(l))