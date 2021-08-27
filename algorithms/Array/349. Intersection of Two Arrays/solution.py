class Solution:
    # Solution 1
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            if nums1[i] in ans:
                continue
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    ans.append(nums1[i])
                    break
        return ans
    
    # Solution 2
    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return list(nums1_set & nums2_set)
