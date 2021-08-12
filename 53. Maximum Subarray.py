def find_max_sum (l) :
    print(l)

    # if base case
    _len = len(l)
    if _len == 1 :
        return l[0]
    
    # find mid
    mid_index = _len // 2

    # devide
    left = find_max_sum(l[:mid_index:])
    right = find_max_sum(l[mid_index::])

    # councur
    
    print("concur -> {}".format( [left,left+right,right] ))
    return max([left,left+right,right])


def sol (nums) :
   return find_max_sum(nums)
    

if __name__ == "__main__" :
    n = list(map(int,input().strip('[]').split(',')))
    # print(n)
    print(sol(n))