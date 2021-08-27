def sol(s) :
    d = {}
    for cur in s :
        if d.get(cur) :
            d[cur] += 1
        else :
            d.update({cur:1})
    for key,val in d.items() :
        if val == 1 :
            return s.index(key)
    return -1

if __name__ == "__main__" :
    s = input().strip('"')
    print(sol(s))