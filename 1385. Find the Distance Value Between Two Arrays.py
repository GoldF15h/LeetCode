class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for i in range(len(arr1)) :
            isPlus = True
            for j in range(len(arr2)) :
                if abs(arr1[i] - arr2[j]) <= d :
                    isPlus = False
                    break
            if isPlus :
                ans += 1
        return ans