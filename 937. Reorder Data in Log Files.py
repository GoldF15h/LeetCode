def isAMoreThanB (a,b) :
    cur = 0
    isMore = False
    while cur < len(a) and cur < len(b) :
        if ord(a[cur]) == ord(b[cur]) :
            cur += 1
        elif ord(a[cur]) > ord(b[cur]) :
            isMore = True
            break
        else :
            isMore = False
            break
    if not isMore :
        if cur == len(a) or cur == len(b) :
            if len(a) > len(b) :
                isMore = True
    return isMore

def sol (logs) :
    log , digit = [] , []
    for cur in logs :
        if ''.join(cur.split()[1::]).isalpha() :
            log.append(cur)
        else :
            digit.append(cur)
    # print(log)
    # print(digit)
    for i in range(len(log)) :
        for j in range(len(log)-i-1) :
            aHead , aTail = log[j].split()[0] , log[j].split()[1::]
            aTail = ' '.join(aTail)
            bHead , bTail = log[j+1].split()[0] , log[j+1].split()[1::]
            bTail = ' '.join(bTail)
            if aTail == bTail :
                if isAMoreThanB(aHead,bHead) :
                    log[j] , log[j+1] = log[j+1] , log[j]
            else :
                if isAMoreThanB(aTail,bTail) :
                    log[j] , log[j+1] = log[j+1] , log[j]
    return log + digit

if __name__ == "__main__" :
    l = list( x.strip('"') for x in input().strip('[]').split(',') )
    print(sol(l))