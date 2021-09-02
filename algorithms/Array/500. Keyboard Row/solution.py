class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        d = dict()
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        for char in first_row:
            d[char] = 1
        for char in second_row:
            d[char] = 2
        for char in third_row:
            d[char] = 3
        ans = []
        for word in words:
            lower_word = word.lower()
            row = d[lower_word[0]]
            flag = True
            for char in lower_word[1:]:
                if row != d[char]:
                    flag = False
                    break
            if flag:
                ans.append(word)
        return ans
