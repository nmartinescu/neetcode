class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window, size = set(), 0
        for num in nums:
            if num in window:
                return True
            else:
                window.add(num)
                size += 1
                if size >= k:
                    window.remove(num)
                    size -= 1
        return False