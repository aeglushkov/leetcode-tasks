class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max2 = max3 = -10000
        min1 = min2 = min3 = 10000
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif max1 >= num > max2:
                max2, max3 = num, max2
            elif max2 >= num > max3:
                max3 = num
            if num < min1:
                min1, min2 = num, min1
            elif min1 <= num < min2:
                min2 = num
        return max(min1 * min2 * max1, max1 * max2 * max3)
