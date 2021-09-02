class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [None] * len(score)
        sorted_score = sorted([(score[i], i) for i in range(len(score))], reverse=True)
        for i in range(len(sorted_score)):
            sc, idx = sorted_score[i]
            if i == 0:
                ans[idx] = "Gold Medal"
            elif i == 1:
                ans[idx] = "Silver Medal"
            elif i == 2:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(i + 1)
        return ans
