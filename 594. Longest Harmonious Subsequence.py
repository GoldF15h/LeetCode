def sol (nums) :
    d = {}
    for cur in nums :
        if d.get(cur) :
            d[cur] += 1
        else :
            d.update({cur:1})
    # print(d)
    l = list(d.keys())
    l.sort()
    # print(l)
    _len = len(l)
    _max = 0
    for i in range(0,_len-1) :
        if l[i+1]-l[i] == 1 :
            con = d[l[i]] + d[l[i+1]]
            if con > _max :
                # print(l[i],l[i+1],'con ->',con,d[l[i]],d[l[]])
                _max = con 
    return _max

if __name__ == "__main__" :
    l = list(map(int,input().strip('[]').split(',')))
    print(sol(l))