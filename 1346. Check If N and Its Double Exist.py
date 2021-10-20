class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if 0 in arr :
            arr.remove(0)
            if 0 in arr :
                return True
        arr.sort()
        for i in range(len(arr)) :
            if arr[i]*2 in arr :
                return True
        return False
        