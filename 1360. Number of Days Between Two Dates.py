def cntFrom1971 (n) :
    y,m,d = list(map(int,n.split('-')))
    # print(y,m,d)
    op = -1
    for curYear in range(1971,y) :
        if  (curYear % 4 == 0 and curYear % 100 != 0 ) or (curYear % 400 == 0) :
            op += 366
        else :
            op += 365
    # print(op)
    if (y % 4 == 0 and y % 100 != 0 ) or (y % 400 == 0) :
        mSet = [31,29,31,30,31,30,31,31,30,31,30,31]
    else :
        mSet = [31,28,31,30,31,30,31,31,30,31,30,31]
    op += sum(mSet[:m-1:])
    # print(op)
    op += d
    return op

def sol (date1,date2) :
    return abs(cntFrom1971(date1)-cntFrom1971(date2))

if __name__ == "__main__" :
    d1 = input().strip('"')
    d2 = input().strip('"')
    print(sol(d1,d2))