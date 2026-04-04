class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < temperature:
                aux = stack.pop()
                j = aux[1]
                sol[j] = i - j

            
            stack.append((temperature, i))

        while len(stack) > 0:
            aux = stack.pop()
            sol[aux[1]] = 0

        return sol