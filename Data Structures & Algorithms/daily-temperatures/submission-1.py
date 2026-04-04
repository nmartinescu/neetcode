class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                j = stack.pop()[1]
                sol[j] = i - j  
            stack.append((temperature, i))

        while stack:
            sol[stack.pop()[1]] = 0

        return sol