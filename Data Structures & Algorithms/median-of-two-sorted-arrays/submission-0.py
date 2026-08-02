class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        leni = len(nums1)
        lenj = len(nums2)
        merged = nums1 + nums2
        merged.sort()

        total = len(merged)
        if total % 2 == 0:
            return (merged[total // 2 -1] + merged[total // 2]) / 2
        else: 
            return merged[total //2]