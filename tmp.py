inp = list(map(int,input().split()))
d = {}
for cur in inp :
    if d.get(cur) :
        d[cur] += 1
    else :
        d.update({cur:1})

_max = max(list(d.values()))
for i in d.keys() :
    if d[i] == _max :
        op.append(d[i])