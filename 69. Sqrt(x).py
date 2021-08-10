def sol (x) :
    sq = 0
    while (sq+1)**2 <= x:
        # print(sq)
        jump = 1 
        while (sq+ ( jump*2 ) )**2 <= x :
            jump = jump*2
        # print( sq+jump ,"=",sq,'+',jump )
        sq = sq + jump
    return sq

if __name__ == "__main__" :
    x = int(input())
    print(sol(x))