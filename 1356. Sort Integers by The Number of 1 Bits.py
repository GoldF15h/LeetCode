def cntBit (n) :
    op = 0
    while n > 0 :
        if n % 2 == 1 :
            op += 1
        n //= 2
    return op

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)) :
            arr[i] = [cntBit(arr[i]),arr[i]]
        arr.sort()
        return list( x[1] for x in arr )