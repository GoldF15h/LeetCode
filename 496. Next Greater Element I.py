def sol (nums1,nums2) :
    op = []
    i = 0 
    while i < len(nums1) :
        j=0
        isFound = False
        cur = nums1[i]
        while nums2[j] != cur and j < len(nums2):
            j+=1
        j+=1
        while j < len(nums2) :
            if nums2[j] > cur :
                op.append(nums2[j])
                isFound = True
                break
            j+=1
        if not isFound :
            # print(i)
            op.append(-1)
        i+=1
    return op

if __name__ == "__main__" :
    n1 = list(map(int,input().strip('[]').split(',')))
    n2 = list(map(int,input().strip('[]').split(',')))
    print(sol(n1,n2))