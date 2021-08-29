def sol (g,s) :
    g.sort()
    s.sort()
    op = 0
    len_g = len(g)
    len_s = len(s)
    cur_g = 0
    cur_s = 0
    while cur_g < len_g and cur_s < len_s :
        if g[cur_g] <= s[cur_s] :
            cur_g+=1
            cur_s+=1
            op += 1
        else :
            cur_s+=1
    return op

if __name__ == "__main__" :
    g = list(map(int,input().strip('[]').split(',')))
    s = list(map(int,input().strip('[]').split(',')))
    print(sol(g,s))