class Solution:
    def countElements(self, arr: List[int]) -> int:
        seen = set()
        for num in arr:
            seen.add(num)
        ans = 0
        for num in arr:
            if num + 1 in seen:
                ans += 1
        return ans