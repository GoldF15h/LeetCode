def sol (candyType) :
    return min(len(candyType)//2,len(set(candyType)))

if __name__ == "__main__" :
    l = list(map(int,input().strip('[]').split(',')))
    print(sol(l))