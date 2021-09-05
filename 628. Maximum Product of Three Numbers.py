class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        l = []
        l += nums[0:3:] 
        nums = nums[3::]
        l += nums[-1:-4:-1]
        
        _max = l[0] * l[1] * l[2]
        _len = len(l)
        # print(l)
        for i in range(_len-2) :
            for j in range(i+1,_len-1):
                for k in range(j+1,_len) :
                    con = l[i] * l[j] * l[k]
                    print(con,end=' ')
                    if con > _max :
                        _max = con
        return _max
        