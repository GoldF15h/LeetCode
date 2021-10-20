class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        tail = []
        for i in range(len(arr1)) :
            if arr1[i] not in arr2 :
                tail.append(arr1[i])
        for cur in arr2 :
            for i in range(len(arr1)) :
                if arr1[i] == cur :
                    ans.append(cur)
        return ans + sorted(tail)