class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows + 1):
            row = [1] * i
            if len(row) > 2:
                prev_row = ans[-1]
                for j in range(1, len(row) - 1):
                    row[j] = prev_row[j - 1] + prev_row[j]
            ans.append(row)
        return ans
