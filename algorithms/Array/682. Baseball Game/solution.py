class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        for i in range(len(ops)):
            if ops[i] == "C":
                ans.pop(-1)
            elif ops[i] == "D":
                ans.append(ans[-1] * 2)
            elif ops[i] == "+":
                ans.append(ans[-2] + ans[-1])
            else:
                ans.append(int(ops[i]))
        return sum(ans)
