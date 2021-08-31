def sol (words) :
    rows = ['qwertyuiop','asdfghjkl','zxcvbnm']
    op = []
    for i in words :
        curWord = i.lower()
        for curRow in rows :
            # print(curWord,curRow)
            isAns = True
            for curChr in curWord :
                # print(curChr,end= ' ')
                if curChr not in curRow :
                    isAns = False
                    break
            # print()
            if isAns :
                op.append(i)
    return op


if __name__ == "__main__" :
    l = list( x.strip('"') for x in input().strip('[]').split(',')  )
    print(sol(l))