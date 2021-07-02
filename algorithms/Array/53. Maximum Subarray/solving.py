class Solution:
    # # O(n)
    # def maxSubArray(self, nums: List[int]) -> int:
    #     summ = 0
    #     max_sum = -10**5
    #     for el in nums:
    #         if summ + el > 0 or max_sum < 0:
    #             if (summ < 0) and (summ < el):
    #                 summ = el
    #             else:
    #                 summ = summ + el
    #         else:
    #             summ = 0
    #         if summ > max_sum:
    #             max_sum = summ
    #     return max_sum
    
    def maxSubArray(self, nums: List[int]) -> int:
        local_max, global_max = 0, -10**5
        for num in nums:
            global_max = max(global_max, local_max+num)
            local_max = max(0, local_max+num)
        return global_max