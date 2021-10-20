def sol (arr) :
    max_index = 0
    # check dup
    for i in range(len(arr) -1) :
        if arr[i] == arr[i+1] :
            return False
    
    # find max_index
    for i in range(len(arr)) :
        if arr[i] > arr[max_index] :
            max_index = i
    
    # check for half left and half right
    left = arr[:max_index:]
    right = arr[max_index+1::]
    if left == [] or right == [] :
        return False
    if left != sorted(left) :
        return False
    if right != sorted(right)[::-1] :
        return False
    return True
    
if __name__ == "__main__" :
    l = list(map(int,input().strip('[]').split(',')))
    print(sol(l))