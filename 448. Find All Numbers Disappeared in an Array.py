class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        _max = len(nums)
        nums = list(set(nums))
        nums.sort()
        op = []
        expect_number = 1
        while expect_number <= _max :
            # print(nums[0],expect_number)
            if nums != [] :
                if nums[0] == expect_number :
                    nums.pop(0)
                else :
                    op.append(expect_number)
            else :
                op.append(expect_number)
            expect_number+=1
        return op