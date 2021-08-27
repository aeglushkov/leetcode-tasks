class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        max_cons = 0
        while i < len(nums):
            if nums[i] == 1:
                cons = 0
                while nums[i] == 1:
                    cons += 1
                    i += 1
                    if i == len(nums):
                        break
                if cons > max_cons:
                    max_cons = cons
            i += 1
        return max_cons
