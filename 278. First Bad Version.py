def isBadVersion(n) :
    global arr 
    return arr[n-1]

def sol (n):
    cur = 1

    if isBadVersion(1) == True :
        return 1

    if isBadVersion(2) == True :
        return 2

    while not( isBadVersion(cur) == False and isBadVersion(cur+1) == True )  :
        jump = 1
        print(isBadVersion(cur),isBadVersion(cur+1))
        while cur + jump <= n and isBadVersion(cur + jump) == False :
            # print(cur,'-> ',end='')
            cur += jump
            jump *= 2
            # print(cur)
        # print('reset')
    return cur + 1

if __name__ == "__main__" :
    n = int(input())
    x = int(input())
    arr = [False]*(x-1) + [True]*(n-x+1)
    print(sol(n))
    # isBadVersion()
    