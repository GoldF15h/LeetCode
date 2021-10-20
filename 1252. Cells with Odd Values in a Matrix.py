def sol (m,n,indices):
    # print(indices)
    row = []
    for i in range(m) :
        row.append(0)
    col = []
    for i in range(n) :
        col.append(0)

    for cur in indices :
        row[cur[0]] += 1
        col[cur[1]] += 1
    
    ans = 0
    for i in range(m) :
        for j in range(n) :
            if( row[i] + col[j] ) % 2 == 1 :
                ans += 1
    return ans

if __name__ == "__main__" :
    m = int(input())
    n = int(input())
    l = list( list(map(int,x.split(','))) for x in input().strip('[]').split('],[') )
    # print(l)
    print(sol(m,n,l))