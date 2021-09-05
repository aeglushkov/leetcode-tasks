class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums) - 3):
            if (i > 0) and (nums[i - 1] == nums[i]):
                continue
            for j in range(i + 1, len(nums) - 2):
                if (j > i + 1) and (nums[j - 1] == nums[j]):
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if (left > j + 1) and (nums[left] == nums[left - 1]):
                        left += 1
                    elif (right < len(nums) - 1) and (nums[right] == nums[right + 1]):
                        right -= 1
                    else:
                        sum_ = nums[i] + nums[j] + nums[left] + nums[right]
                        if sum_ == target:
                            ans.append([nums[i], nums[j], nums[left], nums[right]])
                            left += 1
                            right -= 1
                        elif sum_ > target:
                            right -= 1
                        else:
                            left += 1
        return ans
