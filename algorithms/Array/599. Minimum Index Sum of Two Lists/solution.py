class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = dict()
        ans = []
        i = j = 0
        least_idx_sum = 10000
        while (i < len(list1)) or (j < len(list2)):
            if i < len(list1):
                get = d.get(list1[i])
                if get is None:
                    d[list1[i]] = i
                else:
                    if i + get < least_idx_sum:
                        ans = [list1[i]]
                        least_idx_sum = i + get
                    elif i + get == least_idx_sum:
                        ans.append(list1[i])
                i += 1
            if j < len(list2):
                get = d.get(list2[j])
                if get is None:
                    d[list2[j]] = j
                else:
                    if j + get < least_idx_sum:
                        ans = [list2[j]]
                        least_idx_sum = j + get
                    elif j + get == least_idx_sum:
                        ans.append(list2[j])
                j += 1
        return ans
