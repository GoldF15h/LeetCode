class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        aliceSizes = list(set(aliceSizes))
        bobSizes = list(set(bobSizes))
        aliceSizes.sort()
        bobSizes.sort()
        i = 0 
        j = 0
        while i < len(aliceSizes) and j < len(bobSizes) :
            if sumA - aliceSizes[i] + bobSizes[j] == sumB + aliceSizes[i] - bobSizes[j] :
                return [aliceSizes[i],bobSizes[j]]
            elif sumA - aliceSizes[i] + bobSizes[j] < sumB + aliceSizes[i] - bobSizes[j] :
                j += 1
            elif sumA - aliceSizes[i] + bobSizes[j] > sumB + aliceSizes[i] - bobSizes[j] :
                i +=1