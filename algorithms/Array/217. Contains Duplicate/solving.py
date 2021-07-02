class Solution:
    # Dict
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for el in nums:
            if h.get(el) is not None:
                return True
            h[el] = 1
        return False
    
    # # Set
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     s = set()
    #     for el in nums:
    #         if el in s:
    #             return True
    #         s.add(el)
    #     return False