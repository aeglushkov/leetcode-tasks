class Solution:
    # O(n^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ans = []
        for i in range(len(nums) - 1):
            h = {}
            for j in range(i + 1, len(nums)):
                expected = h.get(nums[j])
                if expected is not None:
                    left, right = expected
                    triplet = sorted([left, nums[j], right])
                    if triplet not in ans:
                        ans.append(triplet)
                else:
                    h[0 - nums[i] - nums[j]] = [nums[i], nums[j]]
        return ans
    
    # # O(n^3)
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) < 3:
    #         return []
    #     ans = []
    #     for i in range(len(nums) - 2):
    #         left = nums[i]
    #         for j in range(i + 1, len(nums) - 1):
    #             mid = nums[j]
    #             for k in range(j + 1, len(nums)):
    #                 right = nums[k]
    #                 if left + mid + right == 0:
    #                     summ = sorted([left, mid, right])
    #                     if summ not in ans:
    #                         ans.append(summ)
    #     return ans
    