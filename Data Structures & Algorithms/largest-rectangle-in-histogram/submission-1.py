class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left_b, right_b = [0] * n, [n] * n
        for index in range(n):
            while stack and heights[stack[-1]] >= heights[index]:
                stack.pop()
            if stack:
                left_b[index] = stack[-1] + 1
            stack.append(index)
        stack = []
        for index in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[index]:
                stack.pop()
            if stack:
                right_b[index] = stack[-1]
            stack.append(index)
        maximum = 0
        for i in range(n):
            maximum = max(maximum, heights[i] * (right_b[i] - left_b[i]))
        return maximum