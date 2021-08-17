def find_max_sum (l) :
    _sum = l[0] 
    _max = l[0]

    for i in range(1,len(l)) :
        
        if _sum < 0 :
            _sum = l[i] 
        else :
            _sum = _sum + l[i]
        
        if _max < _sum :
            _max = _sum 

    return _max

def sol (nums) :
   return find_max_sum(nums)
    
if __name__ == "__main__" :
    n = list(map(int,input().strip('[]').split(',')))
    # print(n)
    print(sol(n))