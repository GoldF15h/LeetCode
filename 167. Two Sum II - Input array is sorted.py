def sol (numbers: list, target: int) :
    _len = len(numbers)
    head = 0
    tail = _len - 1

    cur = 0
    jump = 1

    if numbers[tail] > target and numbers[tail] != 0 and target != 0:
        while cur < _len :
            if ( numbers[cur] <= target or numbers[cur] == 0 ) and numbers[cur+1] > target :
                tail = cur
                break
            
            if cur+jump < _len :
                if numbers[cur + jump] <= target or numbers[cur + jump] == 0 :
                    cur = cur + jump
                    jump = jump*2
                else :
                    jump = 1
            else :
                jump = 1

    numbers = numbers[:tail+1:]
    # print(numbers)
    secL = numbers[::]
    for i in range(tail) :
        try :
            secL.pop(0)
            secNum = target - numbers[i]
            return [ i+1, i + 2 + secL.index(secNum) ]
        except :
            pass
        
if __name__ == "__main__" :
    l = list(map(int,input().strip('[]').split(',')))
    n = int(input())
    print(sol(l,n))