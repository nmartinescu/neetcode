class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products_left = [1] * len(nums)
        products_right = [1] * len(nums)
        ans = [0] * len(nums)
        for i in range(1, len(nums)):
            products_left[i] = products_left[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            products_right[i] = products_right[i + 1] * nums[i + 1]
        print(products_left, products_right)
        for i in range(len(nums)):
            ans[i] = products_left[i] * products_right[i]
        return ans
