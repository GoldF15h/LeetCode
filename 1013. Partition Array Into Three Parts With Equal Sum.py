class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        target = sum(arr)/3
        curSum = 0
        eq = 0
        for i in range(len(arr)) :
            curSum += arr[i]
            if curSum == target :
                eq += 1
                curSum = 0
            if eq == 3 :
                break
        return eq == 3