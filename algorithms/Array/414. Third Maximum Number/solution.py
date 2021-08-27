class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = -2 ** 32
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif max2 < num < max1:
                max2, max3 = num, max2
            elif max3 < num < max2:
                max3 = num
        if max3 == -2 ** 32:
            return max1
        return max3
