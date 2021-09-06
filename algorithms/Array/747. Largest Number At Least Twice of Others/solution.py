class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1 = max2 = -float("inf")
        idx = None
        for i in range(len(nums)):
            if nums[i] > max1:
                max1, max2 = nums[i], max1
                idx = i
            elif max2 < nums[i] <= max1:
                max2 = nums[i]
        if max2 * 2 <= max1:
            return idx
        return -1
