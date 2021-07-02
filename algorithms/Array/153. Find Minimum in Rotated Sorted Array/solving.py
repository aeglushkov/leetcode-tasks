class Solution:
    # O(log(n))
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        right = len(nums)
        left = 0
        i = right // 2
        while i != left:
            num = nums[i]
            if num > minimum:
                left = i
            else:
                minimum = num
                right = i
            i = left + (right - left) // 2
        return minimum