def sol(s) :
    d = {}
    for cur in s :
        if d.get(cur) :
            d[cur] += 1 
        else :
            d.update({cur:1})
    l = list(d.values())
    op = 0
    isOne = False 
    for cur in l :
        if cur >= 2 :
            if cur % 2 == 1 :
                op += cur - 1
                isOne = True
            else :
                op += cur
        else :
            isOne = True
    return op + 1 if isOne else op

if __name__ == "__main__" :
    s = input().strip('"')
    print(sol(s))