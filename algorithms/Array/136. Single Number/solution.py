class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        already_seen = dict()
        for i in range(len(nums)):
            num = nums[i]
            if already_seen.get(num) is None:
                already_seen[num] = 1
            else:
                already_seen.pop(num)
        return list(already_seen.keys())[0]
