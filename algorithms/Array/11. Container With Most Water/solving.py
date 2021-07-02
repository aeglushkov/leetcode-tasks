class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left != right:
            heighest = max(height[left], height[right])
            lowest = min(height[left], height[right])
            area = (right - left) * lowest
            if area > max_area:
                max_area = area
            if height[left] == lowest:
                left += 1
            else:
                right -= 1
        return max_area