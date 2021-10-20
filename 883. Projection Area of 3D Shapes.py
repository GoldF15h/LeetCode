def sol (grid) :
    ans = 0
    
    # top
    for curRow in range(len(grid)) :
        for curCol in range(len(grid[0])) :
            if grid[curRow][curCol] > 0 :
                ans += 1

    # look from x 
    for curRow in range(len(grid)) :
        ans += max(grid[curRow])

    # look from y
    for curCol in range(len(grid[0])) :
        _max = 0
        for curRow in range(len(grid)) :
            if grid[curRow][curCol] > _max :
                _max = grid[curRow][curCol]
        ans += _max

    return ans

if __name__ == "__main__" :
    l = list( list(map(int,x.split(','))) for x in input().strip('[]').split('],[') )
    # print(l)
    print(sol(l))