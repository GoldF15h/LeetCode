class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minAbs = min( abs(arr[x+1] - arr[x]) for x in range(len(arr)-1)  )
        l = []
        for i in range(len(arr)-1) :
            if abs(arr[i] - arr[i+1]) == minAbs :
                l.append([arr[i],arr[i+1]])
        # print(l)
        return l
        