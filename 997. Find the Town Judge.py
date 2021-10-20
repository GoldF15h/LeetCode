def sol (n,trust) :
    trust
    arr = []
    not_town_trust = [False]*n
    for i in range(n) :
        arr.append([])
    for cur_trust in trust :
        p , t = cur_trust
        not_town_trust[p-1] = True
        if p not in arr[t-1] :
            arr[t-1].append(p)
    for i in range(len(not_town_trust)) :
        if not not_town_trust[i] :
            if len(arr[i]) == n-1 :
                return i+1
    return -1
        

if __name__ == "__main__" :
    n = int(input())
    l = list ( list(map(int,x.split(','))) for x in input().strip('[]').split('],[') )
    print(sol(n,l))