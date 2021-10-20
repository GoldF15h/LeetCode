class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        for cur in nums :
            if d.get(cur) :
                d[cur] += 1
            else :
                d.update({cur:1})
        op = []
        for cur in nums :
            tmp = 0
            for i in d.keys() :
                if i < cur :
                    tmp += d[i] 
            op.append(tmp)
        return op
            