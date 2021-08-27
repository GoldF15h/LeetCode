def sol (s,t) :
    d = {}
    for cur in s :
        if d.get(cur) :
            d[cur] += 1
        else :
            d.update({cur:1})
    for cur in t :
        if d.get(cur) :
            d[cur] -= 1
            if d[cur] == 0 :
                d.pop(cur)
        else :
            return cur

if __name__ == "__main__" :
    s = input().strip('"')
    t = input().strip('"')
    print(sol(s,t))