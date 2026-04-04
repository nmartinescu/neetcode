class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0] * len(nums1)
        index = collections.defaultdict(int)
        for i in range(len(nums2)):
            index[nums2[i]] = i
        for i in range(len(nums1)):
            ans[i] = index[nums1[i]]
        return ans