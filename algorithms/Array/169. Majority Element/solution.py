class Solution:
    # Solution 1, O(n * log n)
    def majorityElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        numbers = sorted(nums)
        while left <= right:
            if numbers[left] == numbers[right]:
                return numbers[left]
            left += 1
            right -= 1
    
    # Solution 2, O(n)
    def majorityElement2(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
