def sol (nums1,nums2) :
    op = []
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))
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

if __name__ == "__main__" :
    n1 = list(map(int,input().strip('[]').split(',')))
    n2 = list(map(int,input().strip('[]').split(',')))
    print(sol(n1,n2))