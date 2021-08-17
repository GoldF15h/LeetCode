def bestBuy(l) :
    _max = 0

    buyPrice = l[0]

    for i in range(1,len(l)) :
        
        sellPrice = l[i]

        if sellPrice - buyPrice > _max :
            _max = sellPrice - buyPrice

        if l[i] < buyPrice :
            buyPrice = l[i]
        
    return _max

def sol (prices) :
    return bestBuy(prices)

if __name__ == "__main__" :
    l = list(map(int,input().strip('[]').split(',')))
    print(sol(l))