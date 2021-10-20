def sol (n) :
    if n == 1 :
        return False
    data_set = [0]
    for curNum in range(2,n+1) :
        # print('curNum',curNum)
        stat = 0
        for i in range(1,curNum) :
            # print(i,data_set[i-1])
            if curNum % i == 0 and data_set[curNum-i-1] == 0 :
                # print('WIN!')
                stat = 1
                break
        data_set.append(stat)
    # print(data_set)
    return data_set[-1] == 1
    

if __name__ == "__main__" :
    n = int(input())
    print(sol(n))
        