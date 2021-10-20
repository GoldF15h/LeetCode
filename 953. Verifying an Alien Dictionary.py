def isLessThan (a,b,d) :
    i = 0
    while i < len(a) and i < len(b) :
        if d[ a[i] ] < d[ b[i] ] :
            return True
        elif d[ a[i] ] > d[ b[i] ] :
            return False
        else :
            i += 1
    return len(a) < len(b)

def sol (words,order) :
    # print(words,order)
    d = {}
    for i in range(len(order)) :
        d.update({ order[i] : i })
    for i in range(len(words)-1) :
        if words[i] != words[i+1] :
            if not isLessThan(words[i],words[i+1],d) :
                return False
    return True

if __name__ == "__main__" :
    words = list( x.strip('"') for x in input().strip('[]').split(','))
    order = input().strip('"')
    print(sol(words,order)) 