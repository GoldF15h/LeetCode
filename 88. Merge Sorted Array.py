def sol ( nums1, m, nums2, n ) :

    _nums1 = nums1[::]
    while(nums1 != []) :
        nums1.pop()
    
    for i in range(n) :
        _nums1.pop()

    # if [] []
    if _nums1 == [] and nums2 == [] :
        return

    # if [] [...]
    if _nums1 == [] :
        for i in nums2 :
            nums1.append(i)
        return
        
    # if [...] []
    if nums2 == [] :
        for i in _nums1 :
            nums1.append(i)
        return
    
    #if [...] [...]

    # merge
    while _nums1 != [] and nums2 != [] :
        # print(nums1,_nums1,nums2)
        # print(_nums1[0] < nums2[0])
        if _nums1[0] < nums2[0] :
            nums1.append(_nums1[0])
            _nums1.pop(0)
        else :
            nums1.append(nums2[0])
            nums2.pop(0)

    # re [...] and [...] []
    if _nums1 != [] :
        for i in _nums1 :
            nums1.append(i)

    # re [...] and [] [...]
    if nums2 != [] :
        for i in nums2 :
            nums1.append(i)    

if __name__ == "__main__" :
    nums1 = list(map(int,input().strip('[]').split(',')))
    m = int(input())
    nums2 = list(map(int,input().strip('[]').split(',')))
    n = int(input())
    sol(nums1,m,nums2,n)
    print(nums1)