class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ansIndexSum = 2**31-1
        ans = []
        # for i in list1 :
        #     print(i)
        for i in range(len(list1)) :
            for j in range(len(list2)) :
                if list1[i] == list2[j] :
                    if i + j < ansIndexSum :
                        ansIndexSum = i + j 
                        ans = [list1[i]]
                    if i + j == ansIndexSum and list1[i] not in ans:
                        ans.append(list1[i])
        # print(type(ans),ans)
        return ans
                        