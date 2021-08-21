def sol (n) :

    five = 0 
    cur = 5
    while cur <= n :

        tmp = cur
        while tmp % 5 == 0 :
            five += 1
            tmp /= 5

        cur += 5

    two = 0
    cur = 2 
    while cur <= n :

        tmp = cur
        while tmp % 2 == 0 :
            two += 1
            tmp /= 2

        cur += 2

    # print(five,two)
    return min(five,two)
    
if __name__ == "__main__" :
    n = int(input())
    print(sol(n))