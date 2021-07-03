class Solution:
    # def climbStairs(self, n: int) -> int:
    #     start = [1, 2]
    #     if n < 3:
    #         return start[n-1]
    #     for i in range(2, n):
    #         start.append(start[i-1] + start[i-2])
    #     return start[-1]
    
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2
        if n == 1:
            return first
        elif n == 2:
            return second
        ans = 0
        for i in range(2, n):
            ans = first + second
            if first < second:
                first = ans
            else:
                second = ans
        return ans
