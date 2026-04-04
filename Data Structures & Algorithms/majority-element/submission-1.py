class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = None
        element_count = 0
        for num in nums:
            if element == None:
                element = num
                element_count += 1
            elif element == num:
                element_count += 1
            else:
                if element_count == 1:
                    element = num
                else:
                    element_count -= 1
        return element
                