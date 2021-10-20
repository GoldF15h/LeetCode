def split(s) :
    op = []
    cur = ''
    for i in range(len(s)) :
        if (cur + s[i]).isalpha() :
            cur += s[i]
        else :
            if cur != '' :
                op.append(cur)
                cur = ''
    if cur != '' :
        op.append(cur)
    # print(op)
    return op

def sol (paragraph,banned) :
    d = {}
    for cur in split(paragraph) :
        tmp = cur.strip(',.!').lower()
        if d.get(tmp) :
            d[tmp] += 1
        else :
            d.update({tmp:1})
    print('\n\n',d)
    ans = ''
    for cur in d.keys() :
        if cur not in banned :
            if ans == '' :
                ans = cur
            elif d[cur] > d[ans] :
                ans = cur
    return ans

if __name__ == "__main__" :
    p = input().strip('"')
    b = list ( x.strip('"') for x in input().strip('[]').split(',') )
    print("\n\n\nANS # ",sol(p,b))