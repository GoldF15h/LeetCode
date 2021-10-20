def sol (bills) :
    change = { 5:0,10:0,20:0 }
    for i in range(len(bills)) :
        print(change,bills[i])
        if bills[i] == 5 :
            change[5] += 1
        if bills[i] == 10 :
            if change[5] > 0 :
                change[10] += 1
                change[5] -= 1
            else :
                return False
        if bills[i] == 20 :
            if change[5] > 0 and change[10] > 0 :
                change[20] += 1
                change[5] -= 1
                change[10] -= 1
            elif change[5] >= 3 :
                change[5] -= 3
            else :
                return False
    return True

if __name__ == "__main__" :
    l = list(map(int,input().strip('[]').split(',')))
    print(sol(l))