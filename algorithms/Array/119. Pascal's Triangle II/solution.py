class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex + 2):
            prev_row = row
            row = [1] * i
            if len(row) > 2:
                for j in range(1, len(row) - 1):
                    row[j] = prev_row[j - 1] + prev_row[j]
        return row
