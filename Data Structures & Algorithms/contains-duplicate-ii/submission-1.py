class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window, size = set(), 0
        for i in range(len(nums)):
            num = nums[i]
            if num in window:
                return True
            else:
                window.add(num)
                size += 1
                if size > k:
                    window.remove(nums[i - size + 1])
                    size -= 1
        return False