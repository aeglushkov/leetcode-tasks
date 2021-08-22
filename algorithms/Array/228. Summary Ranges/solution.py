class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) < 2:
            return map(str, nums)
        left = 0
        right = 1
        ans = []
        while right <= len(nums):
            if left == len(nums) - 1:
                ans.append(str(nums[left]))
                break
            if right == len(nums):
                ans.append(str(nums[left]) + '->' + str(nums[right - 1]))
                break
            if nums[right] - nums[left] != right - left:
                if left == right - 1:
                    ans.append(str(nums[left]))
                else:
                    ans.append(str(nums[left]) + '->' + str(nums[right - 1]))
                left = right
            right += 1
        return ans
