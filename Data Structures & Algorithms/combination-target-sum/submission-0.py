class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        curr = []
        n = len(nums)

        def dfs(i, target):
            if i == n and target == 0 and curr:
                sol.append(curr.copy())
                return None
            if i == n or target < 0:
                return None

            curr.append(nums[i])
            dfs(i, target - nums[i])
            curr.pop()
            dfs(i + 1, target)
        
        dfs(0, target)

        return sol