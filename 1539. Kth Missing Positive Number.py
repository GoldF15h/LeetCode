class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0] :
            return k
        cnt = 0
        j = 0
        for i in range(1,100000) :
            if j < len(arr) :
                if i != arr[j] :
                    cnt += 1
                else :
                    j += 1
                
            else :
                cnt += 1
            
            if cnt == k :
                return i