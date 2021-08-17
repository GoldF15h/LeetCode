def sol (numRows) :
    l = [[1],[1,1]]

    # base case 
    if numRows <= 0 :
        return
    if numRows == 1 :
        return [[1]]
    if numRows == 2 :
        return [[1],[1,1]]

    
    # runloop for every row 
    for row_num in range(1,numRows-1) :

        # create middle of the row 
        _row = []

        # runloop in prev row and add to new row
        for i in range(row_num) :
            _row.append( l[row_num][i] + l[row_num][i+1] )

        # append
        l.append( [1] + _row + [1] ) 

    return l

if __name__ == "__main__" :
    n = int(input())
    x = sol(n)
    print(x)