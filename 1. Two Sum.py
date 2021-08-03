def sol (nums,target) :
    for fir in range(0,len(nums)-1) : 
            for sec in range( fir+1,len(nums)) :
                if nums[fir] + nums[sec] == target :
                    return ([fir,sec])

if __name__ == "__main__" :
    l = list(map(int,input().strip('[]').split(',')))
    t = int(input())
    print(sol(l,t))