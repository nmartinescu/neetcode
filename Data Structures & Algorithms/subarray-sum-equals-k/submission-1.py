class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        curr = 0
        hash_map = {0: 1}
        for num in nums:
            curr += num
            prefix = curr - k
            if prefix in hash_map:
                ans += hash_map[prefix]
            hash_map[curr] = hash_map.get(curr, 0) + 1

        return ans