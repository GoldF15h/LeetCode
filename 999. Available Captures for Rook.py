def sol (board) :
    # for cur in board :
    #     print(''.join(cur))
    ans = 0
    # find R
    x,y = -1,-1
    for i in range(8) :
        for j in range(8) :
            if board[i][j] == 'R' :
                x, y = i, j
                break
    
    # up
    dis = 0 
    while x - dis > 0 :
        dis += 1
        print(board[dis][y])
        if board[x-dis][y] == 'B' :
            break
        if board[x-dis][y] == 'p' :
            ans += 1
            break
    # print('AFTER    UP',ans)
    
    # down
    dis = 0
    while x + dis < 7 :
        dis += 1
        if board[x+dis][y] == 'B' :
            break
        if board[x+dis][y] == 'p' :
            ans += 1
            break
    # print('AFTER  DOWN',ans)

    # left
    dis = 0
    while y - dis > 0 :
        dis += 1
        if board[x][y-dis] == 'B' :
            break
        if board[x][y-dis] == 'p' :
            ans += 1
            break
    # print('AFTER  LEFT',ans)

    # right
    dis = 0
    while y + dis < 7 :
        dis += 1
        if board[x][y+dis] == 'B' :
            break
        if board[x][y+dis] == 'p' :
            ans += 1
            break
    # print('AFTER RIGHT',ans)

    return ans

if __name__ == "__main__" :
    l = input().strip('[]').split('],[')
    l = list( x.strip('"').split('","') for x in l )
    # print('\n',l[0])
    print(sol(l)) 