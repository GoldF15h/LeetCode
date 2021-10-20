def isWin (l) :
    if ( [0,0] in l and [1,1] in l  and [2,2] in l ) :
        return True
    if ( [2,0] in l and [1,1] in l  and [0,2] in l ) :
        return True

    for curCol in range(3) :
        if [0,curCol] in l and [1,curCol] in l and [2,curCol] in l :
            return True
    
    for curRow in range(3) :
        if [curRow,0] in l and [curRow,1] in l and [curRow,2] in l :
            return True
    return False

def sol (moves) :
    A = moves[::2]
    B = moves[1::2]
    if isWin(A) :
        return "A"
    if isWin(B) :
        return "B"
    if len(moves) == 9 :
        return "Draw"
    return "Pending"

    


if __name__ == "__main__" :
    l = list ( list(map(int,x.split(','))) for x in input().strip('[]').split('],['))
    print(sol(l))
