class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        left_b = [0] * n
        right_b = [0] * n
        for index, height in enumerate(heights):
            while stack and stack[-1][0] >= height:
                stack.pop()
            if not stack:
                left_b[index] = 0
            else:
                top = stack[-1]
                left_b[index] = top[1] + 1
            stack.append((height, index))
        stack = []
        for index in range(n - 1, -1, -1):
            height = heights[index]
            while stack and stack[-1][0] >= height:
                stack.pop()
            if not stack:
                right_b[index] = n
            else:
                top = stack[-1]
                right_b[index] = top[1]
            stack.append((height, index))
        maximum = 0
        for i in range(n):
            maximum = max(maximum, heights[i] * (right_b[i] - left_b[i]))
        return maximum