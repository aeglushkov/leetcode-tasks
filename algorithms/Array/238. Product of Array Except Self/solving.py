class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize both with 1, cuz multiplication
        left_to_right = [1]
        right_to_left = [1]
        for i in range(len(nums) -1):
            # accumulate while iterating
            left_to_right.append(left_to_right[i] * nums[i])
            right_to_left.append(right_to_left[i] * nums[-1 - i])
        res = []
        # pick forward from left_to_right list and backward from right_to_left
        for j in range(len(nums)):
            res.append(left_to_right[j] * right_to_left[-1 - j])
        return res
