class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = dict()
        max_freq = 0
        num = None
        for i in range(len(nums)):
            if d.get(nums[i]) is None:
                d[nums[i]] = (1, i, i + 1)
            else:
                freq, first_idx, _ = d[nums[i]]
                d[nums[i]] = (freq + 1, first_idx, i + 1)
            freq = d[nums[i]]
            if freq[0] > max_freq:
                max_freq = freq[0]
                num = nums[i]
            elif (freq[0] == max_freq) and (nums[i] != num):
                sub1_len = freq[2] - freq[1]
                sub2_len = d[num][2] - d[num][1]
                if sub1_len < sub2_len:
                    num = nums[i]
        most_freq = d[num]
        return most_freq[2] - most_freq[1]
