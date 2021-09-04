class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = dict()
        for char in s1:
            if s1_counter.get(char) is None:
                s1_counter[char] = 1
            else:
                s1_counter[char] += 1
        s2_counter = dict()
        i = 0
        while i < len(s2):
            if s2_counter.get(s2[i]) is None:
                s2_counter[s2[i]] = 1
            else:
                s2_counter[s2[i]] += 1
            if i > len(s1) - 2:
                if s1_counter == s2_counter:
                    return True
                s2_counter[s2[i - len(s1) + 1]] -= 1
                if s2_counter[s2[i - len(s1) + 1]] == 0:
                    s2_counter.pop(s2[i - len(s1) + 1])
            i += 1
        return False
