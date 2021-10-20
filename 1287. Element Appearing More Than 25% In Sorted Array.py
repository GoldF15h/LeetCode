import math

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        arr.sort()
        jump = len(arr)//4 + 1  
        # print(len(arr))
        # print(jump)
        if len(arr) < 4 :
            return arr[0]
        
        for i in range(len(arr)-jump+1) :
            if arr[i] == arr[i+jump-1] :
                return arr[i]