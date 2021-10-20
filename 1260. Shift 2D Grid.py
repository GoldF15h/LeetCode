def transPost (l) :
    op = []
    for curCol in range(len(l[0])) :
        newRow = []
        for curRow in range(len(l)) :
            newRow.append(l[curRow][curCol])
        op.append(newRow)
    return op

def sol (grid,k) :
    grid = transPost(grid)
    # grid = transPost(grid)
    # print(grid)
    for i in range(k) :
        grid = [grid[len(grid)-1]]+ grid[:len(grid)-1:]
        grid[0] = [grid[0][len(grid[0])-1]] + grid[0][:len(grid[0])-1:]
    # print(grid[0])
    return transPost(grid)

if __name__ == "__main__":
    l = list( list(map(int,x.split(','))) for x in input().strip('[]').split('],[') )
    k = int(input())
    # print(l)
    print(sol(l,k))