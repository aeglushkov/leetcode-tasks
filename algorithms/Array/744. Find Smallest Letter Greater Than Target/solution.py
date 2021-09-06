class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while left <= right:
            i = (left + right) // 2
            if letters[i] == target:
                break
            if letters[i] > target:
                right = i - 1
            else:
                left = i + 1
        while (i < len(letters) - 1) and (letters[i] == target):
            i += 1
        return letters[i] if letters[i] > target else letters[(i + 1) % len(letters)]
