class Solution:
    # Solution 1
    def missingNumber(self, nums: List[int]) -> int:
        tmp_nums = [False] * (len(nums) + 1)
        for num in nums:
            tmp_nums[num] = True
        for i in range(len(tmp_nums)):
            if tmp_nums[i] == False:
                return i
       
    # Solution 2
    def missingNumber2(self, nums: List[int]) -> int:
        n = len(nums)
        missing_num = int(n * (n + 1) / 2 - sum(nums))
        return missing_num
