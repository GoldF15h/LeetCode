def sol (points) :
    ans = 0
    for i in range(len(points)-1) :
        x = abs(points[i][0] - points[i+1][0])
        y = abs(points[i][1] - points[i+1][1])
        ans += min(x,y) + abs(x-y)
    return ans

if __name__ == "__main__" :
    # [[1,1],[3,4],[-1,0]]
    l = list( list(map(int,x.split(','))) for x in input().strip('[]').split('],[') )
    print(sol(l))