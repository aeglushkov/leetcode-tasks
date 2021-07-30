class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        div = 1
        while i >= 0:
            digit = digits[i] + div
            if digit > 9:
                digits[i] = digit % 10
                div = 1
            else:
                digits[i] += div
                div = 0
            if div == 0:
                return digits
            i -= 1
        return [1] + digits
