class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums2 = [None for i in range(len(nums))]
        ans = []
        for i in range(len(nums)):
            if nums2[nums[i] - 1] is not None:
                ans.append(nums[i])
            nums2[nums[i] - 1] = nums[i]
        for i in range(len(nums2)):
            if nums2[i] is None:
                ans.append(i + 1)
        return ans
