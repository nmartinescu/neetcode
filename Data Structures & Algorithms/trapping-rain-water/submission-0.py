class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix, sufix, maximum = [0] * n, [0] * n, 0
        for i in range(n):
            maximum = max(maximum, height[i])
            sufix[i] = maximum
        
        maximum = 0
        for i in range(n - 1, -1, -1):
            maximum = max(maximum, height[i])
            prefix[i] = maximum
        
        res = 0
        for i in range(n):
            res += max(min(sufix[i], prefix[i]) - height[i], 0)
        return res