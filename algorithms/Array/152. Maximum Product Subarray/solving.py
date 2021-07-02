class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left_local_max, left_global_max = 1, -100
        right_local_max, right_global_max = 1, -100
        for i in range(len(nums)):
            if left_local_max == 0:
                left_local_max = nums[i]
            else:
                left_local_max = left_local_max * nums[i]
            if right_local_max == 0:
                right_local_max = nums[-1 - i]
            else:
                right_local_max = right_local_max * nums[-1 - i]
            left_global_max = max(left_global_max, left_local_max)
            right_global_max = max(right_global_max, right_local_max)
        return max(left_global_max, right_global_max)
