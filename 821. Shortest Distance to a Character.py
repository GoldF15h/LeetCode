def sol (s,c) :
    ChrIndexList = []
    op = []
    for i in range(len(s)) :
        if s[i] == c :
            ChrIndexList.append(i)
    # print(ChrIndexList)
    for i in range(ChrIndexList[0]) :
        op.append(ChrIndexList[0]-i)
    # print(op)
    for ChrIndex in range(len(ChrIndexList)-1) :
        for i in range(ChrIndexList[ChrIndex],ChrIndexList[ChrIndex+1]) :
            left = i - ChrIndexList[ChrIndex]
            right = ChrIndexList[ChrIndex+1] - i
            op.append(min(left,right))
    # print(op)
    for i in range(ChrIndexList[-1],len(s)) :
        op.append( i - ChrIndexList[-1] )
    # print(op)


if __name__ == "__main__" :
    s = input().strip('"')
    c = input().strip('"')
    print(sol(s,c))