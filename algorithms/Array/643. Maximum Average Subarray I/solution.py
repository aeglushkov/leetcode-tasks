class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = 0
        left = 0
        right = k
        for i in range(right):
            sum_ += nums[i]
        avg = sum_ / k
        while right < len(nums):
            sum_ -= nums[left]
            sum_ += nums[right]
            if avg < sum_ / k :
                avg = sum_ / k
            left += 1
            right += 1
        return avg
