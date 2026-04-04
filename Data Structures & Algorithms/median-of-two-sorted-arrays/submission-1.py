class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        elif len(nums1) == 0:
            if len(nums2) % 2:
                return nums2[len(nums2) // 2]
            else:
                return (nums2[len(nums2) // 2 - 1] + nums2[len(nums2) // 2]) / 2
        
        l, r = 0, len(nums1)
        length = len(nums1) + len(nums2)
        half = length // 2
        while True:
            i = (l + r) // 2
            j = half - i - 2

            nums1_left = nums1[i] if i >= 0 else float("-inf")
            nums1_right = nums1[i + 1] if i + 1 < len(nums1) else float("inf")
            nums2_left = nums2[j] if j >= 0 else float("-inf")
            nums2_right = nums2[j + 1] if j + 1 < len(nums2) else float("inf")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if length % 2:
                    return min(nums1_right, nums2_right)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                r = i - 1
            else:
                l = i + 1
        