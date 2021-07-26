class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = self.find_minimum(nums, nums[0])
        return ans
    
    def find_minimum(self, nums, minimum):
        if len(nums) == 0:
            return minimum
        if len(nums) == 1:
            return min(nums[0], minimum)
        middle = len(nums) // 2
        if nums[middle] == minimum:
            left_min = self.find_minimum(nums[:middle], minimum)
            right_min = self.find_minimum(nums[middle:], minimum)
            return min(left_min, right_min)
        if nums[middle] <= minimum:
            return self.find_minimum(nums[:middle], nums[middle])
        elif nums[middle] > minimum:
            return self.find_minimum(nums[middle:], minimum)
