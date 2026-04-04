class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        maximum_area = 0
        while L < R:
            minimum = min(height[L], height[R])
            distance = R - L
            print(distance, minimum)
            maximum_area = max(maximum_area, distance * minimum)
            if height[L] > height[R]:
                R -= 1
            else:
                L += 1
        return maximum_area