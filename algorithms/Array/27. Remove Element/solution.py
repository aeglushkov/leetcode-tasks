class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, cur = 0, 0
        while i < len(nums):
            if nums[i] != val:
                nums[cur] = nums[i]
                cur += 1
            i += 1
        return cur
