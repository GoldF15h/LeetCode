from itertools import permutations

def sol(turnedOn) :
    if turnedOn > 8 :
        return []
    perm = [0]*(10-turnedOn) + [1]*turnedOn
    op = []
    for cur in set(permutations(perm)) :
        h = 8*cur[0] + 4*cur[1] + 2*cur[2] + 1*cur[3]
        m = 32*cur[4] + 16*cur[5] + 8*cur[6] + 4*cur[7] + 2*cur[8] + 1*cur[9]
        if h >= 12 or m >= 60 :
            continue
        if m < 10 :
            m = '0'+str(m)
        else :
            m = str(m)
        h = str(h)
        op.append(h+':'+m)
    return op

if __name__ == "__main__" :
    # n = int(input())
    for n in range(11) :
        print(sol(n))
    