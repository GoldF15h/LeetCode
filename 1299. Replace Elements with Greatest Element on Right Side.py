class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = sorted(arr)
        for i in range(len(arr)-1) :
            l.remove(arr[i])
            arr[i] = l[-1]
        arr[-1] = -1
        return arr
        