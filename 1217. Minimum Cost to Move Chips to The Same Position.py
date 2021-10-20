def sol (position) :
    d = {}
    for cur in position :
        if d.get(cur) :
            d[cur] += 1
        else :
            d.update({cur:1})

    odd = 0
    even = 0
    for i in d.keys() :
        if i % 2 == 0 :
            even += d[i]
        else :
            odd += d[i]

    return min(even,odd)


if __name__ == "__main__" :
    # print(costA2B(int(input()),int(input())))
    l = list(map(int,input().strip('[]').split(',')))
    print(sol(l))