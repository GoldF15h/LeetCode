class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        op = []
        nums1.sort()
        nums2.sort()
        while nums1 != [] and nums2 != [] :
            if nums1[0] < nums2[0] :
                nums1.pop(0)
            elif nums1[0] > nums2[0] :
                nums2.pop(0)
            else :
                op.append(nums1[0])
                nums1.pop(0)
                nums2.pop(0)
            # print('XXXXX')
            # print(nums1,'\n',nums2,sep='')
        return op