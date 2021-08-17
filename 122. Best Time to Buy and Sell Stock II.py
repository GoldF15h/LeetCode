def sol (prices) :
    profit = 0 
    buyIndex = 0
    sellIndex = 0
    cur_profit = 0

    for i in range(1,len(prices)) :            
        
        new_profit =    prices[i] - prices[buyIndex]
        # print(buyIndex,sellIndex,i,cur_profit,new_profit)

        if cur_profit < new_profit :
            cur_profit = new_profit
            sellIndex = i

        if cur_profit > new_profit :
            # print('set!! ',cur_profit)
            profit = profit + cur_profit
            buyIndex = i
            sellIndex = i
            cur_profit = 0
            
    profit = profit + cur_profit
    return profit

if __name__ == "__main__" :
    testcase = [[7,1,5,3,6,4],[1,2,3,4,5],[7,6,4,3,1]]
    for l in testcase :
        print('case :',l)
        print('ans :',sol(l))