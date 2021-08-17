def sol (nums) :
    nums.sort()
    stack = []
    for cur in nums :
        if stack == [] :
            stack.append(cur)
        else :
            if cur == stack[-1] :
                stack.pop()
            else :
                return stack[-1]
    
    return stack[-1]
            

if __name__ == "__main__" :
    l = list(map(int,input().strip('[]').split(',')))
    print(sol(l))