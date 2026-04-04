class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        el1, cnt1, el2, cnt2 = None, 0, None, 0
        n = len(nums)
        for num in nums:
            if el1 == num:
                cnt1 += 1
            elif el2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                el1 = num
                cnt1 = 1
            elif cnt2 == 0:
                el2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        if el1 != None and nums.count(el1) > n // 3:
            ans.append(el1)
        if el2 != None and nums.count(el2) > n // 3:
            ans.append(el2)

        return ans