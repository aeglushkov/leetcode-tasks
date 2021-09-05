class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        is_found = False
        while left <= right:
            i = (left + right) // 2
            if nums[i] == target:
                is_found = True
                break
            elif nums[i] > target:
                right = i - 1
            else:
                left = i + 1
        if not is_found:
            return [-1, -1]
        left = right = i
        while (left >= 0) and (nums[left] == target):
            left -= 1
        while (right < len(nums)) and (nums[right] == target):
            right += 1
        return [left + 1, right - 1]
