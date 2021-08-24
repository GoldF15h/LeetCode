def sol (nums) :
    if nums == [] :
        return []
    op = []
    cur_list = [nums[0]]
    i = 1
    while i < len(nums) :
        if nums[i] - cur_list[-1] == 1 :
            cur_list.append(nums[i])
        else :
            op.append(cur_list)
            cur_list = [nums[i]]
            # i += 1
        i += 1
    op.append(cur_list)
    st = []
    for cur in op :
        if len(cur) == 1 :
            st.append("{}".format(cur[0]))
        else :
            st.append("{}->{}".format(cur[0],cur[-1]))

    return st

if __name__ == "__main__" :
    l = list(map(int,input().strip('[]').split(',')))
    print(sol(l))