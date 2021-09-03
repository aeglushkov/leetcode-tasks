class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_length = length = 1
        i = 1
        while i < len(nums):
            if nums[i] > nums[i - 1]:
                length += 1
            else:
                length = 1
            if length > max_length:
                max_length = length
            i += 1
        return max_length
