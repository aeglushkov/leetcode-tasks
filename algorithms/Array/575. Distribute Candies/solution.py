class Solution:
    # Solution 1
    def distributeCandies(self, candyType: List[int]) -> int:
        d = dict()
        type_num = 0
        for can_type in candyType:
            if d.get(can_type) is None:
                type_num += 1
                d[can_type] = True
        return min(type_num, len(candyType) // 2)

    # Solution 2
    def distributeCandies2(self, candyType: List[int]) -> int:
        unique_types = set(candyType)
        return min(len(unique_types), len(candyType) // 2)
